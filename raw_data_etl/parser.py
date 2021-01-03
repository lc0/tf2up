"""Read files from TensorFlow converter"""

import argparse
import re

from collections import namedtuple
from typing import NamedTuple, List, Tuple

class ParseException(Exception):
    def __init__(self, line):
        self._line = line

        super(ParseException, self).__init__(f"Format of file has been changed: {self._line}")


class ReportLine(NamedTuple):
    line: int
    position: int
    severity: str
    message: str
    ops: List[str]


class FileMeta(NamedTuple):
    date: str
    file_hash: str


def parse_filename(filename: str) -> FileMeta:
    """
    Parse filename into - FileMeta: file hash and date of conversion

    >> parse_filename('gs://tf2up/reports/2019-05-12_56526374885474bea6b420728c7b92bf_report.txt')
    """
    prefix, file_hash, *_ = filename.split('_')
    conversion_date = prefix[-len('2019-01-01'):]

    return FileMeta(conversion_date, file_hash)


def _parse_line(line: str) -> ReportLine:
    """
    Parse line into ReportLine

    >>> parse_line("5:0: INFO: Renamed 'tf.logging.set_verbosity' to 'tf.compat.v1.logging.set_verbosity'")
    ReportLine(line=5, position=0, severity='INFO',
    message="Renamed 'tf.logging.set_verbosity' to 'tf.compat.v1.logging.set_verbosity'",
    ops=['tf.logging.set_verbosity', 'tf.compat.v1.logging.set_verbosity'])

    """

    positions, level, *message_list = line.split(' ')
    line_number, position, _ = positions.split(':')
    level = level[:-1]
    message = ' '.join(message_list)

    ops = re.findall(r'(tf.[^\'\s\()]+)', message)

    return ReportLine(line=int(line_number),
                      position=int(position),
                      severity=level,
                      message=message,
                      ops=list(set(ops)))

def parse_file(lines: List[str]) -> List[ReportLine]:
    """Parse file"""

    for idx, line in enumerate(lines):
        if line.startswith('Processing file'):
            report_start_line = idx + 4
            break
    else:
        raise ParseException("Can not find the start of report")

    parsed_lines : List[ReportLine] = []
    # converter failure, could be a result of python2 code
    if 'ERROR: Failed to parse.' == lines[report_start_line]:
        parsed_lines.append(ReportLine(line=0,
                                        position=0,
                                        severity='ERROR',
                                        message='ERROR: Failed to parse.',
                                        ops=[]))

        return parsed_lines


    for idx, line in enumerate(lines[report_start_line:]):
        line = line.strip()

        if not line:
            break

        # end of report part
        if line.startswith('----'):
            break

        try:
            parsed_line = _parse_line(line)
            parsed_lines.append(parsed_line)
        except ValueError:
            # sometimes TensorFlow has multi-line comments
            # https://github.com/tensorflow/tensorflow/blob/master/tensorflow/tools/compatibility/tf_upgrade_v2.py#L671
            next_line = lines[report_start_line + idx + 1]
            if re.match(r'\d+:\d+', next_line):
                parsed_lines[-1] = parsed_lines[-1]._replace(
                    message=parsed_line.message + " " + line)
            else:
                raise ParseException(f"Failed with following line: '{line}'")

    else:
        raise ParseException("Can not find the end of report")

    return parsed_lines


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=argparse.FileType('r'))
    args = parser.parse_args()

    lines = args.input.readlines()
    parsed_lines = parse_file(lines)
    for line in parsed_lines:
        print(line)


    # TODO: add structured output to TF2 converter script
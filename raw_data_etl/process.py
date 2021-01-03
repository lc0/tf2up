"""A word-counting workflow."""

from __future__ import absolute_import

import argparse
import logging

from parser import parse_file, parse_filename

import apache_beam as beam
from apache_beam.io import WriteToText
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import SetupOptions


class MetaAndContent(beam.DoFn):
  """Parse each line of input text into words."""

  def process(self, element):
    file_meta, content = element

    file_dict = file_meta._asdict()
    for line in content:
      # yield file_meta.date, file_meta.file_hash, line.line, line.position, line.severity, line.message, line.ops
      file_dict.update(line._asdict())
      yield file_dict


def run(argv=None):
  """Main entry point; defines and runs the wordcount pipeline."""
  parser = argparse.ArgumentParser()
  parser.add_argument('--input',
                      dest='input',
                      default='gs://dataflow-samples/shakespeare/kinglear.txt',
                      help='Input file to process.')
  parser.add_argument('--output',
                      dest='output',
                      required=True,
                      help='Output file to write results to.')
  known_args, pipeline_args = parser.parse_known_args(argv)

  # We use the save_main_session option because one or more DoFn's in this
  # workflow rely on global context (e.g., a module imported at module level).
  pipeline_options = PipelineOptions(pipeline_args)
  pipeline_options.view_as(SetupOptions).save_main_session = True
  p = beam.Pipeline(options=pipeline_options)


  from apache_beam.io import fileio

  with beam.Pipeline(options=PipelineOptions()) as p:
    output = (p
              | "match" >> fileio.MatchFiles(known_args.input)
              | "read match" >> fileio.ReadMatches()
              | "read_file" >> beam.Map(lambda x: (x.metadata.path,
                                                   x.read_utf8()))
              | "parse file" >> beam.Map(lambda x: (parse_filename(x[0]),
                                                    parse_file(x[1].split('\n'))
                                                   ))
              | "unfold" >> beam.ParDo(MetaAndContent())
              # | "debug" >> beam.FlatMap(lambda x: print(x))
    )

    table_spec = 'brainscode-140622:tf2up.conversions'
    table_schema = {'fields': [
        {'name': 'date', 'type': 'DATE'},
        {'name': 'file_hash', 'type': 'STRING'},
        {'name': 'line', 'type': 'INT64'},
        {'name': 'position', 'type': 'INT64'},
        {'name': 'severity', 'type': 'STRING'},
        {'name': 'message', 'type': 'STRING'},
        {'name': 'ops', 'type': 'STRING', 'mode': 'REPEATED'}
    ]}


    # two different setups for create_disposition CREATE_IF_NEEDED
    # and write_disposition - WRITE_TRUNCATE
    output | 'store to BQ' >> beam.io.WriteToBigQuery(
                          table_spec,
                          schema=table_schema,
                          write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND,
                          create_disposition=beam.io.BigQueryDisposition.CREATE_NEVER,
                          method="STREAMING_INSERTS"
                        )



    # Write the output using a "Write" transform that has side effects.
    # pylint: disable=expression-not-assigned
    output | 'write' >> WriteToText(known_args.output)


if __name__ == '__main__':
  logging.getLogger().setLevel(logging.INFO)
  run()
from nbdime.webapp import nbdiffweb
from nbdime.webapp.nbdimeserver import NbdimeHandler

NbdimeHandler.prepare = lambda _: None

args = nbdiffweb.build_arg_parser().parse_args(['original.ipynb', 'original.ipynb'])

args.ip = '0.0.0.0'
args.port = 81
args.allow_remote_access = True
args.base_url = '/d/'

# THE BIGGEST HACK EVER
nbdiffweb.main_diff(args)
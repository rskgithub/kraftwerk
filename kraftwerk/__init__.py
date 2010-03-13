import logging
from os.path import join, dirname

__version__ = '0.0'

templates_dir = join(dirname(__file__), 'templates')

default_formatter = logging.Formatter(
    u'%(name)s: %(levelname)s: %(message)s')

console_handler = logging.StreamHandler() # By default, outputs to stderr.
console_handler.setFormatter(default_formatter)
console_handler.setLevel(logging.DEBUG)

logging.getLogger('kraftwerk').addHandler(console_handler)
logging.getLogger('kraftwerk').setLevel(logging.INFO) # Default level.
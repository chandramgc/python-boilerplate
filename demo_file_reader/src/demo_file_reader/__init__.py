# __init__.py for demo_file_reader
from .compressed.bzipped import opener as bz2_open
from .compressed.gzipped import opener as gzip_open
from .util import writer

__all__ = ['bz2_open', 'gzip_open']

print("__init__.py executed...")

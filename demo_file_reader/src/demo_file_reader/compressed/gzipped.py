import gzip

from .. import util


opener = gzip.open

if __name__ == '__main__':
    util.writer.main(opener)

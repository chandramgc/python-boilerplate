import os.path

from demo_file_reader.compressed import bzipped, gzipped

extension_map = {
    '.gz': gzipped.opener,
    '.bz2': bzipped.opener
}


class MultiReader:
    def __init__(self, filename):
        ext = os.path.splitext(filename)[1]
        opener = extension_map.get(ext, open)
        self.f = opener(filename, 'rt')

    def read(self):
        return self.f.read()

    def close(self):
        self.f.close()

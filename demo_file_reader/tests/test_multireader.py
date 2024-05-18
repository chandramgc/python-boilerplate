import unittest

from demo_file_reader.multireader import MultiReader as MR


class Test_MultiReader(unittest.TestCase):
    def test_init(self):
        MR('test_file.txt')

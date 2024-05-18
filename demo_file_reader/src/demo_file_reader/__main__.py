import sys

from demo_file_reader.multireader import MultiReader

f = MultiReader(sys.argv[1])
print(f.read())
f.close()


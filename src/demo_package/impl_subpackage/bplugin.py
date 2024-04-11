"""Module providing a plugin 'b' msg"""

from ..util_subpackage import printer
MSG = "Call from plugin b.py"

if __name__ == "__main__":
    printer.main(MSG)

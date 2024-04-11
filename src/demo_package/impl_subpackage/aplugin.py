"""Module providing a plugin 'a' msg"""


from ..util_subpackage import printer
MSG = "Call from plugin a.py"

if __name__ == "__main__":
    printer.main(MSG)

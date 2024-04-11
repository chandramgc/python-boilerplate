"""Module providing a main class."""
import importlib
import pkgutil

from .impl_subpackage import aplugin,bplugin

extension_map = {
    'a': aplugin.MSG,
    'b': bplugin.MSG
}

# import demo_package.impl_subpackage

# def iter_namespace(ns_pkg) :
#     """
#         Namespace package argument ns_pkg
#         Finds all sub packages
#     """
#     return pkgutil.iter_modules(
#             ns_pkg.__path__,
#             ns_pkg.__name__+ ".")

# # Build set of module objects
# # import them with importlib
# # Find modules to import with iter_namespace
# compression_plugins = {
#     importlib.import_module(module_name)
#     for _, module_name, _
#     in iter_namespace(demo_package.impl_subpackage)
# }

# # Build extension_map dict comperhension
# # Look for module-level attributes
# # Get modules from compression_plugins
# extension_map = {
#     module.extension: module.opener
#     for module in compression_plugins
# }

class Main:
    """Class representing a main"""

    def __init__(self, plugin):
        print("Main __init__ method call")
        msg = extension_map.get(plugin, open)
        print("Printing args msg: " + str(msg))

    def close(self):
        """Function representing a close"""
        print("Main close method call")

    def read(self):
        """Function representing a read"""
        print("Main read method call")

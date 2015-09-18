# # # # # # # # # # # # # #
# CAPTAINHOOK IDENTIFIER  #
# # # # # # # # # # # # # #
from .utils import bash


CHECK_NAME = 'pep8radius'
DEFAULT = 'off'
NO_PEP8RADIUS_MSG = (
    "pep8radius is required for the pep8radius plugin.\n"
    "`pip install pep8radius` or turn it off in your tox.ini file.")


def run(files, temp_folder, argstring=''):
    "Check PEP-8 errors, but only in the diff."

    try:
        import pep8radius  # NOQA
    except ImportError:
        return NO_PEP8RADIUS_MSG

    return bash(
        # Argument may contain unicode, i.e. in config file name.
        u'pep8radius --diff --no-color {}'.format(argstring)
    ).value()

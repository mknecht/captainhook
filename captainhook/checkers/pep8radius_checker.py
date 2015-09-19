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
    """Check PEP-8 errors, but only in the diff.

    Arguments are passed verbatim to pep8radius.

    See pep8radius on GitHub: https://github.com/hayd/pep8radius

    """
    try:
        import pep8radius  # NOQA
    except ImportError:
        return NO_PEP8RADIUS_MSG

    return bash(
        # unicode because argument string may contain unicode,
        # i.e. in config file name.
        # --no-color because the color reset did not work when I tried it,
        # screwing up the colors after the diff, too.
        u'pep8radius --diff --no-color {}'.format(argstring)
    ).value()

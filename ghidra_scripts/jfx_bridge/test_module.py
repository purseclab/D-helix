""" Module purely for testing that we can remoteify a module """

import sys


def run():
    # make sure we can handle different string types inside the module
    print("Doubles")
    print('Singles say "hi"')
    print(
        """Multis
    are fine
    """
    )

    # check that imports are in the module globals (accessible inside definitions)
    return sys.version_info[0]

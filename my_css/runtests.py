#!/usr/bin/env python

import sys

from tests.config import configure


def run_tests(*test_args):
    from django_nose import NoseTestSuiteRunner
    test_runner = NoseTestSuiteRunner(verbosity=1)
    test_runner.run_tests(test_args)


if __name__ == '__main__':
    args = sys.argv[1:]
    if not args:
        args.extend(['--with-coverage', '--cover-package=my_css'])
    configure()
    run_tests(*args)

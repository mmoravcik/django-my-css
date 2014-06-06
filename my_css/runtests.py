#!/usr/bin/env python

import logging

from tests.config import configure

# No logging
logging.disable(logging.CRITICAL)


def run_tests(verbosity, *test_args):
    from django_nose import NoseTestSuiteRunner
    test_runner = NoseTestSuiteRunner()
    test_runner.run_tests(test_args)


if __name__ == '__main__':
    configure()
    run_tests(1)

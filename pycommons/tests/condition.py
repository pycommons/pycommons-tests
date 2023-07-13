import functools
import logging
import unittest

__all__ = ["fails", "skip", "skip_if", "skip_unless", "flaky"]

from typing import Callable, Optional
from unittest import TestCase

fails = unittest.expectedFailure

skip = unittest.skip
skip_if = unittest.skipIf
skip_unless = unittest.skipUnless


def flaky(reason: Optional[str] = None, run_times: int = 2):  # pylint: disable=W0613
    def decorator(f: Callable):
        @functools.wraps(f)
        def wrapped(self: TestCase, *args, **kwargs):
            for i in range(run_times):
                try:
                    f(self, *args, **kwargs)
                    logging.debug("Run %d passed", i)
                except AssertionError as e:
                    logging.debug("Run %d failed; exception: %s", i, e)

        return wrapped

    return decorator

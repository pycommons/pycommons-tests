import unittest

__all__ = ["fails", "skip", "skip_if"]

fails = unittest.expectedFailure

skip = unittest.skip
skip_if = unittest.skipIf
skip_unless = unittest.skipUnless

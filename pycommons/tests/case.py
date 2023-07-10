import unittest
from typing import Any, Optional

from pycommons.tests.matcher import Matcher


class TestCase(unittest.TestCase):
    def assertSame(self, expected: Any, actual: Any, msg: Optional[str] = None):
        if id(expected) != id(actual):
            self.fail(msg)

    def assertNotSame(self, expected: Any, actual: Any, msg: Optional[str] = None):
        if id(expected) == id(actual):
            self.fail(msg)

    def assertThat(self, matcher: Matcher[Any], actual: Any, msg: Optional[str] = None):
        if not matcher.match(actual):
            self.fail(msg)

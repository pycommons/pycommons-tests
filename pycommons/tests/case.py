import unittest
from typing import Any, Optional

from pycommons.tests.matcher import Matcher


class TestCase(unittest.TestCase):
    """
    Extensions to python's `unittest.TestCase` class. Provides additional
    assertion methods and helper methods.
    """

    def assertSame(self, expected: Any, actual: Any, msg: Optional[str] = None) -> None:
        """
        Assert if the expected object is same as the actual object, i.e. their ids match.

        Args:
            expected: Expected object
            actual: Actual object
            msg: message

        Returns:
            None
        """
        if id(expected) != id(actual):
            self.fail(msg)

    def assertNotSame(self, expected: Any, actual: Any, msg: Optional[str] = None):
        """
       Assert if the expected object is not the same as the actual object, i.e. their ids do not match.

       Args:
           expected: Expected object
           actual: Actual object
           msg: message

       Returns:
           None
       """
        if id(expected) == id(actual):
            self.fail(msg)

    def assertThat(self, matcher: Matcher[Any], actual: Any, msg: Optional[str] = None):
        """
        Provides matcher type assertion. A matcher is a functional interface with a single abstract method
        `match` that takes an object (`actual`) and returns True if the matching is successful.

        Args:
            matcher: A matcher object
            actual: The object to be matched
            msg: message

        Returns:
            None
        """
        if not matcher.match(actual):
            self.fail(msg)


class IsolatedAsyncIOTestCase(unittest.IsolatedAsyncioTestCase, TestCase):
    ...

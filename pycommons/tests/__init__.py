"""PyCommons tests namespace."""
from __future__ import annotations

from importlib_metadata import PackageNotFoundError, version

__author__ = "Shashank Sharma"
__email__ = "shashankrnr32@gmail.com"

from .case import IsolatedAsyncIOTestCase, TestCase
from .condition import skip, skip_if, skip_unless, flaky, fails
from .exception import raises
from .parametrized import cases, TestData
from .utils import TestUtils

__all__ = [
    "IsolatedAsyncIOTestCase",
    "TestCase",
    "TestData",
    "TestUtils",
    "__author__",
    "__email__",
    "__version__",
    "cases",
    "fails",
    "flaky",
    "raises",
    "skip",
    "skip_if",
    "skip_unless",
]

# Used to automatically set version number from GitHub actions
# as well as not break when being tested locally
try:
    __version__ = version(__package__)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "0.0.0"

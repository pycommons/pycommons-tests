from abc import ABC, abstractmethod
from typing import TypeVar, Generic

_T = TypeVar("_T")


class Matcher(ABC, Generic[_T]):
    @abstractmethod
    def match(self, value: _T) -> bool:
        ...


class AnyOfMatcher(Matcher[_T]):
    def __init__(self, *args: Matcher[_T]):
        self._matchers = args

    def match(self, value: _T) -> bool:
        for matcher in self._matchers:
            if matcher.match(value):
                return True
        return False


class AllOfMatcher(Matcher[_T]):
    def __init__(self, *args: Matcher[_T]):
        self._matchers = args

    def match(self, value: _T) -> bool:
        for matcher in self._matchers:
            if not matcher.match(value):
                return False
        return True

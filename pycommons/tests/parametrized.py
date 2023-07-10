import dataclasses
import functools
from typing import Any, Optional, Callable
from unittest import TestCase


@dataclasses.dataclass
class TestData:
    data: Any
    expected: Any
    enabled: bool = True

    message: Optional[str] = None

    def get_message(self):
        return (
            f"{self.message if self.message else 'TestCase'} "
            f"(data={self.data}, expected={self.expected})"
        )


def cases(*testcases: TestData):
    def decorator(f: Callable):
        @functools.wraps(f)
        def wrapped(self: TestCase):
            for case in testcases:
                if case.enabled:
                    with self.subTest(case.get_message()):
                        f(self, case)

        return wrapped

    return decorator

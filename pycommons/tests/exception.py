import functools
from typing import Type, Callable
from unittest import TestCase


def raises(exception_type: Type[BaseException]):
    def decorator(f: Callable):
        @functools.wraps(f)
        def wrapped(self: TestCase, *args, **kwargs):
            with self.assertRaises(exception_type):
                f(self, *args, **kwargs)

        return wrapped

    return decorator

import time

from pycommons.tests.case import TestCase
from pycommons.tests.utils import TestUtils


class TestTestUtils(TestCase):
    def test_delay(self):
        _start = time.time()
        TestUtils.delay(100, "Testing purpose")
        _end = time.time()
        self.assertSame(_start, _start)
        self.assertNotSame(_start, _end)

        self.assertTrue(110 >= (_end - _start) * 1000 >= 100)

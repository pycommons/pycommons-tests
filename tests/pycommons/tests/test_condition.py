import logging
import random
import sys

from pycommons.tests.case import TestCase
from pycommons.tests.condition import flaky


class TestFlakyTest(TestCase):
    def setUp(self) -> None:
        logging.root.setLevel(logging.DEBUG)
        logging.root.addHandler(logging.StreamHandler(sys.stdout))

    @flaky(run_times=6)
    def test_flaky_test(self):
        self.assertEqual(2, random.randint(0, 10))

    @flaky(run_times=6)
    def test_flaky_test_passes(self):
        self.assertEqual(2, 1 + 1)

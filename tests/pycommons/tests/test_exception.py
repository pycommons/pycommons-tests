from pycommons.tests.case import TestCase
from pycommons.tests.condition import fails
from pycommons.tests.exception import raises


class TestRaisesAnnotation(TestCase):
    @raises(RuntimeError)
    def test_raises_exception(self):
        raise RuntimeError("")

    @fails
    @raises(Exception)
    def test_does_not_raise_exception(self):
        self.assertEqual(2, 1 + 1)

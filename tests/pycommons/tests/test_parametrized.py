from pycommons.tests.case import TestCase
from pycommons.tests.parametrized import cases, TestData


class TestParametrized(TestCase):
    @cases(
        TestData(expected=2, data=(1, 1)),
        TestData(expected=0, data=(1, -1)),
        TestData(expected=100, data=(6, 9, 3, 7, 100, -25)),
        TestData(expected=0, data=(1, 1, 1, 2), enabled=False),
    )
    def test_parametrized(self, test_data: TestData):
        self.assertEqual(test_data.expected, sum(test_data.data))

    @cases()
    def test_parametrized_with_no_parameters(self, test_data: TestData):
        self.assertEqual(test_data.expected, sum(test_data.data))

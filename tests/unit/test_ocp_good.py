from unittest import TestCase
from parameterized import parameterized

from unit.ocp_common import products
from design_patterns.solid.ocp.common import Color, Size
from design_patterns.solid.ocp.product_filter_good import ColorSpecification, SizeSpecification, BetterFilter, Specification


SPEC_RED = ColorSpecification(Color.RED)
SPEC_GREEN = ColorSpecification(Color.GREEN)
SPEC_BLUE = ColorSpecification(Color.BLUE)
SPEC_SMALL = SizeSpecification(Size.SMALL)
SPEC_MEDIUM = SizeSpecification(Size.MEDIUM)
SPEC_LARGE = SizeSpecification(Size.LARGE)
SPEC_BLUE_MEDIUM = SPEC_BLUE & SizeSpecification(Size.MEDIUM)
SPEC_BLUE_LARGE = SPEC_BLUE & SizeSpecification(Size.LARGE)


class TestBetterFilter(TestCase):
    def setUp(self) -> None:
        self.products = products
        self.bfilter = BetterFilter()

    @parameterized.expand(
        [
            (SPEC_RED, ["Car"]),
            (SPEC_BLUE, ["Notebook", "Ship"]),
            (SPEC_GREEN, ["Apple"]),
            (SPEC_SMALL, ["Apple"]),
            (SPEC_MEDIUM, ["Notebook"]),
            (SPEC_LARGE, ["Car", "Ship"]),
            (SPEC_BLUE_MEDIUM, ["Notebook"]),
            (SPEC_BLUE_LARGE, ["Ship"]),
        ]
    )
    def test_filter_called_with_valid_return_filtered_result(self, spec, expected):
        product_filtered = []
        for product in self.bfilter.filter(self.products, spec):
            product_filtered.append(product.name)
        self.assertListEqual(product_filtered, expected)


class TestSpecification(TestCase):
    def test_is_satisfied(self):
        spec = Specification()
        with self.assertRaises(NotImplementedError):
            spec.is_satisfied("any")

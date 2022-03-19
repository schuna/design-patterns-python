from unittest import TestCase

from parameterized import parameterized

from design_patterns.solid.ocp.common import Color, Size
from design_patterns.solid.ocp.product_filter_bad import ProductFilter
from unit.ocp_common import products


class TestProductFilter(TestCase):
    def setUp(self) -> None:
        self.products = products
        self.pfilter = ProductFilter()

    @parameterized.expand(
        [
            (Color.RED, ["Car"]),
            (Color.BLUE, ["Notebook", "Ship"]),
            (Color.GREEN, ["Apple"]),
        ]
    )
    def test_filter_by_color(self, color, expected):
        product_filtered = []
        for product in self.pfilter.filter_by_color(self.products, color):
            product_filtered.append(product.name)
        self.assertListEqual(product_filtered, expected)

    @parameterized.expand(
        [
            (Size.SMALL, ["Apple"]),
            (Size.MEDIUM, ["Notebook"]),
            (Size.LARGE, ["Car", "Ship"]),
        ]
    )
    def test_filter_by_size(self, size, expected):
        product_filtered = []
        for product in self.pfilter.filter_by_size(self.products, size):
            product_filtered.append(product.name)
        self.assertListEqual(product_filtered, expected)

    @parameterized.expand(
        [(Color.BLUE, Size.MEDIUM, ["Notebook"]), (Color.BLUE, Size.LARGE, ["Ship"])]
    )
    def test_filter_by_size_and_color(self, color, size, expected):
        product_filtered = []
        for product in self.pfilter.filter_by_size_and_color(
                self.products, size, color
        ):
            product_filtered.append(product.name)
        self.assertListEqual(product_filtered, expected)

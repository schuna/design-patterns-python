from unittest import TestCase
from parameterized import parameterized

from design_patterns.solid.ocp import (
    Product,
    Color,
    Size,
    ColorSpecification,
    SizeSpecification,
    BetterFilter,
    ProductFilter,
    Specification,
    Filter,
)

SPEC_RED = ColorSpecification(Color.RED)
SPEC_GREEN = ColorSpecification(Color.GREEN)
SPEC_BLUE = ColorSpecification(Color.BLUE)
SPEC_SMALL = SizeSpecification(Size.SMALL)
SPEC_MEDIUM = SizeSpecification(Size.MEDIUM)
SPEC_LARGE = SizeSpecification(Size.LARGE)
SPEC_BLUE_MEDIUM = SPEC_BLUE & SizeSpecification(Size.MEDIUM)
SPEC_BLUE_LARGE = SPEC_BLUE & SizeSpecification(Size.LARGE)

products = [
    Product("Apple", Color.GREEN, Size.SMALL),
    Product("Car", Color.RED, Size.LARGE),
    Product("Notebook", Color.BLUE, Size.MEDIUM),
    Product("Ship", Color.BLUE, Size.LARGE),
]


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


class TestSpecification(TestCase):
    def test_is_satisfied(self):
        spec = Specification()
        with self.assertRaises(NotImplementedError):
            spec.is_satisfied("any")


class TestFilter(TestCase):
    def test_filter(self):
        m_filter = Filter()
        with self.assertRaises(NotImplementedError):
            m_filter.filter("items", "spec")

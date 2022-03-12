from unittest import TestCase

from src.design_patterns.builder.html_builder import HtmlBuilder
from src.design_patterns.builder.html_element import HtmlElement


class TestHtmlBuilder(TestCase):
    def setUp(self) -> None:
        self.html_builder = HtmlBuilder(HtmlElement("ul"))
        self.html_builder_created = HtmlElement.create("ul")

    def test_add_child(self):
        expected = "<ul>\n  <li>\n    hello\n  </li>\n  <li>\n    world\n  </li>\n</ul>"
        self.html_builder.add_child(HtmlElement('li', 'hello'))
        self.html_builder.add_child(HtmlElement('li', 'world'))
        self.assertEqual(expected, str(self.html_builder))

    def test_add_child_fluent(self):
        expected = "<ul>\n  <li>\n    hello\n  </li>\n  <li>\n    world\n  </li>\n</ul>"
        self.html_builder_created.add_child_fluent(HtmlElement('li', 'hello'))\
            .add_child_fluent(HtmlElement('li', 'world'))
        self.assertEqual(expected, str(self.html_builder_created))



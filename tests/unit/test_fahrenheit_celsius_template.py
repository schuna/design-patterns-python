import contextlib
import io
from unittest import TestCase
from unittest.mock import patch

from design_patterns.template_method.fahrenheit_celsius_template import ConverterTemplate


class TestConverterTemplate(TestCase):
    @patch("design_patterns.template_method.fahrenheit_celsius.sys")
    def test_run(self, mock_sys):
        expected = "Input Fahrenheit:\n" \
                   + "32.00℉ = 0.00℃\n" \
                   + "Input Fahrenheit:\n" \
                   + "99.00℉ = 37.22℃\n" \
                   + "Input Fahrenheit:\n" \
                   + "Fahrenheit to Celsius Finished!\n"
        mock_sys.stdin.readline.side_effect = ["32", "99", "a"]
        converter = ConverterTemplate()

        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            converter.run()

        self.assertEqual(expected, buf.getvalue())

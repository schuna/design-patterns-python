import contextlib
import io
from unittest import TestCase
from unittest.mock import patch

from design_patterns.template_method.fahrenheit_celsius import convert_fahrenheit_celsius


class TestMain(TestCase):
    @patch("design_patterns.template_method.fahrenheit_celsius.sys")
    def test_main(self, mock_sys):
        expected = "Input Fahrenheit:\n" \
                   + "32.00℉ = 0.00℃\n" \
                   + "Input Fahrenheit:\n" \
                   + "105.00℉ = 40.56℃\n" \
                   + "Input Fahrenheit:\n" \
                   + "Fahrenheit to Celsius Finished!\n"
        mock_sys.stdin.readline.side_effect = ["32", "105", "x"]
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            convert_fahrenheit_celsius()
        self.assertEqual(expected, buf.getvalue())

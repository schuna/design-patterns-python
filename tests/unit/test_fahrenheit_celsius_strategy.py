import contextlib
import io
from unittest import TestCase
from unittest.mock import patch

from design_patterns.strategy.application_runner import ApplicationRunner
from design_patterns.strategy.fahrenheit_celsius_strategy import ConverterStrategy


class TestConverterStrategy(TestCase):
    @patch("design_patterns.template_method.fahrenheit_celsius.sys")
    def test_run(self, mock_sys):
        expected = "Input Fahrenheit:\n" \
                   + "32.00℉ = 0.00℃\n" \
                   + "Input Fahrenheit:\n" \
                   + "99.00℉ = 37.22℃\n" \
                   + "Input Fahrenheit:\n" \
                   + "Fahrenheit to Celsius Finished!\n"
        mock_sys.stdin.readline.side_effect = ["32", "99", "a"]
        runner = ApplicationRunner(ConverterStrategy())

        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            runner.run()

        self.assertEqual(expected, buf.getvalue())

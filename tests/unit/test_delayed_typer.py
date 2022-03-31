import contextlib
import io
from unittest import TestCase

from design_patterns.command.delayed_typer import DelayedTyper


class TestDelayedTyper(TestCase):
    def setUp(self) -> None:
        self.command = DelayedTyper(0, "0")

    def test_execute(self):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            self.command.main()
        self.assertTrue(DelayedTyper.stop)
        self.assertEqual('13571', buf.getvalue()[:5])


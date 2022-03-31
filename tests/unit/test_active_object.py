import contextlib
import io
from unittest import TestCase

from design_patterns.command.active_object import ActiveObject, WakeupCommand, SleepCommand, current_time_milliseconds


class TestSleepCommand(TestCase):
    def setUp(self) -> None:
        self.active_object = ActiveObject()
        self.sleep_command = SleepCommand(1000, self.active_object, WakeupCommand())
        self.active_object.add_command(self.sleep_command)

    def test_execute(self):
        expected = "Command Executed!\n"
        buf = io.StringIO()

        start_time = current_time_milliseconds()
        with contextlib.redirect_stdout(buf):
            self.active_object.run()
        sleep_time = current_time_milliseconds() - start_time

        self.assertTrue(sleep_time >= 1000)
        self.assertTrue(sleep_time < 1100)
        self.assertEqual(expected, buf.getvalue())

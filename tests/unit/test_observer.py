import contextlib
import io
from unittest import TestCase

from design_patterns.observer.event import Person, call_doctor
from design_patterns.observer.observer import Subject, Observer


class TestPerson(TestCase):
    def setUp(self) -> None:
        self.person = Person("John", "123 Camino St.")

    def test_catch_a_cold(self):
        expected = "John is ill\nA doctor has been called to 123 Camino St.\n"
        self.person.falls_ill.append(lambda name, address: print(f'{name} is ill'))
        self.person.falls_ill.append(call_doctor)

        string_buffer = io.StringIO()
        with contextlib.redirect_stdout(string_buffer):
            self.person.catch_a_cold()

        self.assertEqual(expected, string_buffer.getvalue())


class TestSubject(TestCase):
    def setUp(self) -> None:
        self.subject = Subject()
        Observer(1, self.subject)
        Observer(2, self.subject)

    def test_notify(self):
        expected = "Observer ID: 1 Got ('Notification...',) From Subject ID: 0\n" \
                   + "Observer ID: 2 Got ('Notification...',) From Subject ID: 0\n"

        string_buffer = io.StringIO()
        with contextlib.redirect_stdout(string_buffer):
            self.subject.notify("Notification...")

        self.assertEqual(expected, string_buffer.getvalue())

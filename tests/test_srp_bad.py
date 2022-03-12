import os
from unittest import TestCase
from parameterized import parameterized
from src.design_patterns.solid.srp_bad.journal import Journal
from tempfile import TemporaryDirectory, TemporaryFile


class TestJournal(TestCase):
    def setUp(self) -> None:
        self.journal = Journal()
        self.journal.add_entry("Journal #1")
        self.journal.add_entry("Journal #2")

    @parameterized.expand([(0, "1: Journal #2"), (1, "0: Journal #1")])
    def test_remove_entry_called_valid_then_remove_selected(self, pos, expected):
        self.journal.remove_entry(pos)
        self.assertEqual(expected, str(self.journal))

    @parameterized.expand(
        [
            (2, ValueError),
        ]
    )
    def test_remove_entry_called_invalid_then_raise_exception(self, pos, exception):
        with self.assertRaises(exception):
            self.journal.remove_entry(pos)

    def test_save_when_called_save_journal(self):
        temp_dir = TemporaryDirectory()
        temp_file = os.path.join(temp_dir.name, "output.txt")
        self.journal.save(temp_file)
        actual = self.read_file(temp_file)

        self.assertEqual("0: Journal #1\n1: Journal #2", actual)

    @staticmethod
    def read_file(filename):
        with open(filename, "r") as rf:
            return rf.read()

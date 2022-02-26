from unittest import TestCase
from unittest.mock import patch, mock_open
from parameterized import parameterized

from src.design_patterns.solid.srp import Journal, PersistenceManager


class TestPersistenceManager(TestCase):

    def setUp(self) -> None:
        self.journal = Journal()
        self.journal.add_entry("Journal")

    def test_save_to_file_called_valid_store_journal(self):
        open_mock = mock_open()
        with patch("src.design_patterns.solid.srp.open", open_mock, create=True):
            PersistenceManager.save_to_file(self.journal, "filename")

        open_mock.assert_called_with("filename", "w")
        open_mock.return_value.write.assert_called_once_with(str(self.journal))


class TestJournal(TestCase):
    def setUp(self) -> None:
        self.journal = Journal()
        self.journal.add_entry("Journal #1")
        self.journal.add_entry("Journal #2")

    @parameterized.expand([
        (0, "1: Journal #2"),
        (1, "0: Journal #1")
    ])
    def test_remove_entry_called_valid_then_remove_selected(self, pos, expected):
        self.journal.remove_entry(pos)
        self.assertEqual(expected, str(self.journal))

    @parameterized.expand([
        (2, ValueError),
    ])
    def test_remove_entry_called_invalid_then_raise_exception(self, pos, exception):
        with self.assertRaises(exception):
            self.journal.remove_entry(pos)
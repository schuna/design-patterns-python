from unittest import TestCase

from parameterized import parameterized

from src.design_patterns.proxy.person import ResponsiblePerson, Person


class TestResponsiblePerson(TestCase):
    @parameterized.expand([(18, "drinking"), (17, "too young")])
    def test_drink_regulated_by_age(self, age, expected):
        self.person = ResponsiblePerson(Person(age))
        actual = self.person.drink()
        self.assertEqual(expected, actual)

    @parameterized.expand([(16, "driving"), (15, "too young")])
    def test_drive_regulated_by_age(self, age, expected):
        self.person = ResponsiblePerson(Person(age))
        actual = self.person.drive()
        self.assertEqual(expected, actual)

    @parameterized.expand(
        [(Person(16), "driving while drunk"), (ResponsiblePerson(Person(16)), "dead")]
    )
    def test_drink_and_driving(self, person, expected):
        actual = person.drink_and_drive()
        self.assertEqual(expected, actual)

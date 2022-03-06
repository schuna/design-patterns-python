from unittest import TestCase

from parameterized import parameterized

from src.design_patterns.proxy.protection import Driver, Car, CarProxy


class TestProtectionProxy(TestCase):
    @parameterized.expand(
        [
            (Driver("James", 20), "Car is being driven by James"),
            (Driver("Alex", 26), "Car is being driven by Alex"),
        ]
    )
    def test_drive_when_called_return_driver_name(self, driver, expected):
        car = Car(driver)
        actual = car.drive()
        self.assertEqual(expected, actual)

    @parameterized.expand(
        [
            (Driver("James", 20), "Car is being driven by James"),
            (Driver("Sam", 15), "Age under 16 can not drive, Sam is 15 years old"),
        ]
    )
    def test_drive_regulate_with_age(self, driver, expected):
        car = CarProxy(driver)
        actual = car.drive()
        self.assertEqual(expected, actual)

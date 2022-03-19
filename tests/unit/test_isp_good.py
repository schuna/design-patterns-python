from unittest import TestCase

from design_patterns.solid.isp.printer_good import MyPrinter, Photocopier, MultiFunctionMachine


class TestMyPrinter(TestCase):
    def test_print(self):
        self.printer = MyPrinter()
        self.assertEqual("print document", self.printer.print("document"))


class TestPhotocopier(TestCase):
    def setUp(self) -> None:
        self.printer = Photocopier()

    def test_print(self):
        self.assertEqual("print document", self.printer.print("document"))

    def test_scan(self):
        self.assertEqual("scan document", self.printer.scan("document"))


class TestMultiFunctionMachine(TestCase):
    def setUp(self) -> None:
        self.printer = MultiFunctionMachine(MyPrinter(), Photocopier())

    def test_print(self):
        self.assertEqual("print document", self.printer.print("document"))

    def test_scan(self):
        self.assertEqual("scan document", self.printer.scan("document"))

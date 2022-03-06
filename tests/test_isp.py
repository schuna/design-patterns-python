from unittest import TestCase

from src.design_patterns.solid.isp import MultiFunctionPrinter, OldFashionedPrinter, MyPrinter, Photocopier, \
    MultiFunctionMachine


class TestMultiFunctionPrinter(TestCase):
    def setUp(self) -> None:
        self.printer = MultiFunctionPrinter()

    def test_print(self):
        self.assertEqual("print document", self.printer.print("document"))

    def test_fax(self):
        self.assertEqual("fax document", self.printer.fax("document"))

    def test_scan(self):
        self.assertEqual("scan document", self.printer.scan("document"))


class TestOldFashionedPrinter(TestCase):
    def setUp(self) -> None:
        self.printer = OldFashionedPrinter()

    def test_print(self):
        self.assertEqual("print document", self.printer.print("document"))

    def test_fax(self):
        self.assertEqual("fax document", self.printer.fax("document"))

    def test_scan(self):
        with self.assertRaises(NotImplementedError):
            self.printer.scan("document")


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

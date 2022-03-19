from abc import abstractmethod


class Printer:
    @abstractmethod
    def print(self, document):
        raise NotImplementedError  # pragma: no cover


class Scanner:
    @abstractmethod
    def scan(self, document):
        raise NotImplementedError  # pragma: no cover


class MyPrinter(Printer):
    def print(self, document):
        return f"print {document}"


class Photocopier(Printer, Scanner):
    def print(self, document):
        return f"print {document}"

    def scan(self, document):
        return f"scan {document}"


class MultiFunctionDevice(Printer, Scanner):
    @abstractmethod
    def print(self, document):
        raise NotImplementedError  # pragma: no cover

    @abstractmethod
    def scan(self, document):
        raise NotImplementedError  # pragma: no cover


class MultiFunctionMachine(MultiFunctionDevice):
    def __init__(self, printer, scanner):
        self.scanner = scanner
        self.printer = printer

    def print(self, document):
        return self.printer.print(document)

    def scan(self, document):
        return self.scanner.scan(document)
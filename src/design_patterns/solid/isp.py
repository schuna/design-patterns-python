from abc import abstractmethod

"""
ISP Violated
"""


class Machine:
    def print(self, document):
        raise NotImplementedError

    def fax(self, document):
        raise NotImplementedError

    def scan(self, document):
        raise NotImplementedError


class MultiFunctionPrinter(Machine):
    def print(self, document):
        return f"print {document}"

    def fax(self, document):
        return f"fax {document}"

    def scan(self, document):
        return f"scan {document}"


class OldFashionedPrinter(Machine):
    def print(self, document):
        return f"print {document}"

    def fax(self, document):
        return f"fax {document}"

    def scan(self, document):
        raise NotImplementedError("Printer cannot scan!")


"""
follow ISP 
"""


class Printer:
    @abstractmethod
    def print(self, document):
        raise NotImplementedError


class Scanner:
    @abstractmethod
    def scan(self, document):
        raise NotImplementedError


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
        raise NotImplementedError

    @abstractmethod
    def scan(self, document):
        raise NotImplementedError


class MultiFunctionMachine(MultiFunctionDevice):
    def __init__(self, printer, scanner):
        self.scanner = scanner
        self.printer = printer

    def print(self, document):
        return self.printer.print(document)

    def scan(self, document):
        return self.scanner.scan(document)

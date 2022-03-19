class Machine:
    def print(self, document):
        raise NotImplementedError  # pragma: no cover

    def fax(self, document):
        raise NotImplementedError  # pragma: no cover

    def scan(self, document):
        raise NotImplementedError  # pragma: no cover


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

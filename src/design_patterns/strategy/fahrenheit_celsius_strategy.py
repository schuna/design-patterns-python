from abc import ABCMeta, abstractmethod

from design_patterns.template_method.fahrenheit_celsius import number_from_input_stream


class Application(metaclass=ABCMeta):
    @abstractmethod
    def init(self):
        raise NotImplementedError  # pragma: no cover

    @abstractmethod
    def idle(self):
        raise NotImplementedError  # pragma: no cover

    @abstractmethod
    def cleanup(self):
        raise NotImplementedError  # pragma: no cover

    @abstractmethod
    def set_done(self):
        raise NotImplementedError  # pragma: no cover


class ConverterStrategy(Application):
    def __init__(self):
        self.done = False

    def init(self):
        self.done = False

    def idle(self):
        print("Input Fahrenheit:")
        fahrenheit = number_from_input_stream()
        if fahrenheit is None:
            self.set_done()
        else:
            celsius = 5.0 / 9.0 * (fahrenheit - 32)
            print(f"{fahrenheit:.2f}℉ = {celsius:.2f}℃")

    def cleanup(self):
        print("Fahrenheit to Celsius Finished!")

    def set_done(self):
        self.done = True

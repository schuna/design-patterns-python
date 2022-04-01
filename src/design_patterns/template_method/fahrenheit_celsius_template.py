from design_patterns.template_method.application_template import Application
from design_patterns.template_method.fahrenheit_celsius import number_from_input_stream


class TemperatureConverter(Application):
    def __init__(self):
        super().__init__()

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


if __name__ == '__main__':
    converter = TemperatureConverter()
    converter.run()

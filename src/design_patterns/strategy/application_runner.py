from design_patterns.strategy.fahrenheit_celsius_strategy import ConverterStrategy


class ApplicationRunner:
    def __init__(self, application):
        self.application = application

    def run(self):
        self.application.init()
        while not self.application.done:
            self.application.idle()
        self.application.cleanup()


if __name__ == '__main__':  # pragma: no cover
    runner = ApplicationRunner(ConverterStrategy())
    runner.run()

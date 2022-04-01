from abc import ABCMeta, abstractmethod


class Application(metaclass=ABCMeta):
    def __init__(self):
        self.done = False

    @abstractmethod
    def init(self):
        raise NotImplementedError  # pragma: no cover

    @abstractmethod
    def idle(self):
        raise NotImplementedError

    @abstractmethod
    def cleanup(self):
        raise NotImplementedError

    def set_done(self):
        self.done = True

    def run(self):
        self.init()
        while not self.done:
            self.idle()
        self.cleanup()

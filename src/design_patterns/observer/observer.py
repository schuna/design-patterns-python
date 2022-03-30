class Subject:
    def __init__(self, id=0):
        self.id = id
        self.__observers = []

    def register(self, observer):
        self.__observers.append(observer)

    def notify(self, *args, **kwargs):
        for observer in self.__observers:
            observer.notify(self, *args, **kwargs)

    def __str__(self):
        return f"Subject ID: {self.id}"


class Observer:
    def __init__(self, id, subject):
        self.id = id
        subject.register(self)

    def notify(self, subject, *args):
        print(f"Observer ID: {self.id} Got {args} From {subject}")


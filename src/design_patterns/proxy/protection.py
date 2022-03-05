class Car:
    def __init__(self, driver):
        self.driver = driver

    def drive(self):
        return f"Car is being driven by {self.driver.name}"


class CarProxy:
    def __init__(self, driver):
        self.driver = driver
        self.car = Car(self.driver)

    def drive(self):
        if self.driver.age >= 16:
            return f"Car is being driven by {self.driver.name}"
        else:
            return f"Age under 16 can not drive, {self.driver.name} is {self.driver.age} years old"


class Driver:
    def __init__(self, name, age):
        self.name = name
        self.age = age

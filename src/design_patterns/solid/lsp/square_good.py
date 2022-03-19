class Square:
    def __init__(self, side):
        self._side = side

    @property
    def area(self):
        return self._side * self._side

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        self._side = value

    def __str__(self):
        return f"Side: {self._side}, area: {self.area}"

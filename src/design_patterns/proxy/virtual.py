class Bitmap:
    def __init__(self, filename):
        self.filename = filename
        self.image = None
        self.load()

    def load(self):
        self.image = self.filename.split(".")[0]

    def draw(self):
        return f"Drawing image {self.image}"


class LazyBitmap:
    def __init__(self, filename):
        self.filename = filename
        self.image = None
        self._bitmap = None

    def draw(self):
        if not self._bitmap:
            self._bitmap = Bitmap(self.filename)
        return self._bitmap.draw()

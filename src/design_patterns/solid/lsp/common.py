class User:
    def __init__(self, name):
        self.name = name


class SubscribedUser(User):
    def __init__(self, name):
        super(SubscribedUser, self).__init__(name)
        self.subscribed = True


class Account:
    def __init__(self, user, email_broadcaster):
        self.user = user
        self.email_broadcaster = email_broadcaster

    def on_account_created(self, event):
        return self.email_broadcaster.broadcast(event, self.user)


class Rectangle:
    def __init__(self, width, height):
        self._height = height
        self._width = width

    @property
    def area(self):
        return self._width * self._height

    def __str__(self):
        return f"Width: {self.width}, height: {self.height}"

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

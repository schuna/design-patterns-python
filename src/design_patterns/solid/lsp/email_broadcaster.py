class User:
    def __init__(self, name):
        self.name = name


class SubscribedUser(User):
    def __init__(self, name):
        super(SubscribedUser, self).__init__(name)
        self.subscribed = True


class EmailBroadcasterViolateLSP:
    def __init__(self):
        print("Email Broadcaster")

    def broadcast(self, event, user: User):
        return f"Event: {event} to User: {user.name}"


class SubscriptionEmailBroadcasterViolateLSP(EmailBroadcasterViolateLSP):
    def __init__(self):
        super(SubscriptionEmailBroadcasterViolateLSP, self).__init__()

    def broadcast(self, event, user: SubscribedUser):
        return f"Event: {event} to User: {user.name}, subscribed: {user.subscribed}"


class EmailBroadcaster:
    def __init__(self):
        print("Email Broadcaster")

    def broadcast(self, event, user: SubscribedUser):
        return f"Event: {event} to User: {user.name}, subscribed: {user.subscribed}"


class AnonymousEmailBroadcaster(EmailBroadcaster):
    def __init__(self):
        super(AnonymousEmailBroadcaster, self).__init__()

    def broadcast(self, event, user: User):
        return f"Event: {event} to User: {user.name}"


class Account:
    def __init__(self, user, email_broadcaster):
        self.user = user
        self.email_broadcaster = email_broadcaster

    def on_account_created(self, event):
        return self.email_broadcaster.broadcast(event, self.user)

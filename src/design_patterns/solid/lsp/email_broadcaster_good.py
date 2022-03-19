from design_patterns.solid.lsp.common import SubscribedUser, User


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

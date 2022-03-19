from unittest import TestCase

from parameterized import parameterized

from design_patterns.solid.lsp.common import Account, User, SubscribedUser
from design_patterns.solid.lsp.email_broadcaster_good import EmailBroadcaster, AnonymousEmailBroadcaster
from design_patterns.solid.lsp.square_good import Square


class TestSquare(TestCase):
    def setUp(self) -> None:
        self.square = Square(1)

    @parameterized.expand([(3, "Side: 3, area: 9"), (5, "Side: 5, area: 25")])
    def test_side_change_then_return_changed_square(self, side, expected):
        self.square.side = side
        self.assertEqual(expected, str(self.square))

    @parameterized.expand([(3, "Side: 3, area: 9"), (5, "Side: 5, area: 25")])
    def test_area_when_called_result(self, side, expected):
        self.square.side = side
        self.assertEqual(
            expected, f"Side: {self.square.side}, area: {self.square.area}"
        )


class TestEmailBroadcaster(TestCase):

    @parameterized.expand(
        [
            (
                    "event1",
                    SubscribedUser("user1"),
                    EmailBroadcaster(),
                    "Event: event1 to User: user1, subscribed: True",
            ),
            (
                    "event2",
                    SubscribedUser("user2"),
                    AnonymousEmailBroadcaster(),
                    "Event: event2 to User: user2",
            ),
            (
                    "event3",
                    User("user3"),
                    AnonymousEmailBroadcaster(),
                    "Event: event3 to User: user3",
            ),
        ]
    )
    def test_on_account_created_uphold_lsp_return_message(
            self, event, user, email_broadcaster, expected
    ):
        account = Account(user, email_broadcaster)
        result = account.on_account_created(event)
        self.assertEqual(expected, result)

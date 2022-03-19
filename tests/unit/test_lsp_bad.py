from unittest import TestCase

from parameterized import parameterized

from design_patterns.solid.lsp.common import User, SubscribedUser, Account, Rectangle
from design_patterns.solid.lsp.email_broadcaster_bad import EmailBroadcaster, SubscriptionEmailBroadcaster
from design_patterns.solid.lsp.square_bad import Square


class TestSquare(TestCase):
    def setUp(self) -> None:
        self.rectangle = Square(5)

    @parameterized.expand(
        [
            (Rectangle(2, 3), "Width: 4, height: 5"),
            (Square(5), "Width: 4, height: 4"),
        ]
    )
    def test_height_changed_then_width_also_changed(self, rectangle, expected):
        rectangle.height = 5
        rectangle.width = 4
        self.assertEqual(expected, str(rectangle))

    @parameterized.expand([(Rectangle(2, 3), 20), (Square(5), 16)])
    def test_area_when_called_return_result(self, rectangle, expected):
        rectangle.height = 5
        rectangle.width = 4
        self.assertEqual(expected, rectangle.area)


class TestEmailBroadcaster(TestCase):

    @parameterized.expand(
        [
            (
                    "event1",
                    User("user1"),
                    EmailBroadcaster(),
                    "Event: event1 to User: user1",
            ),
            (
                    "event2",
                    SubscribedUser("user2"),
                    EmailBroadcaster(),
                    "Event: event2 to User: user2",
            ),
            (
                    "event3",
                    SubscribedUser("user3"),
                    SubscriptionEmailBroadcaster(),
                    "Event: event3 to User: user3, subscribed: True",
            ),
        ]
    )
    def test_on_account_created_violate_lsp_return_message(
            self, event, user, email_broadcaster, expected
    ):
        account = Account(user, email_broadcaster)
        result = account.on_account_created(event)
        self.assertEqual(expected, result)

    def test_on_account_created_violate_lsp_raise_exception(self):
        account = Account(User("user1"), SubscriptionEmailBroadcaster())
        with self.assertRaises(AttributeError):
            account.on_account_created("event1")

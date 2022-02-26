from unittest import TestCase

from parameterized import parameterized

from src.design_patterns.solid.lsp.rectangle import SquareViolateLSP, Rectangle, Square
from src.design_patterns.solid.lsp.email_broadcaster import (
    Account,
    User,
    SubscribedUser,
    EmailBroadcasterViolateLSP,
    SubscriptionEmailBroadcasterViolateLSP,
    EmailBroadcaster,
    AnonymousEmailBroadcaster,
)


class TestSquareViolateLSP(TestCase):
    def setUp(self) -> None:
        self.rectangle = SquareViolateLSP(5)

    @parameterized.expand(
        [
            (Rectangle(2, 3), "Width: 4, height: 5"),
            (SquareViolateLSP(5), "Width: 4, height: 4"),
        ]
    )
    def test_height_changed_then_width_also_changed(self, rectangle, expected):
        rectangle.height = 5
        rectangle.width = 4
        self.assertEqual(expected, str(rectangle))

    @parameterized.expand([(Rectangle(2, 3), 20), (SquareViolateLSP(5), 16)])
    def test_area_when_called_return_result(self, rectangle, expected):
        rectangle.height = 5
        rectangle.width = 4
        self.assertEqual(expected, rectangle.area)


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
    def setUp(self) -> None:
        pass

    @parameterized.expand(
        [
            (
                "event1",
                User("user1"),
                EmailBroadcasterViolateLSP(),
                "Event: event1 to User: user1",
            ),
            (
                "event2",
                SubscribedUser("user2"),
                EmailBroadcasterViolateLSP(),
                "Event: event2 to User: user2",
            ),
            (
                "event3",
                SubscribedUser("user3"),
                SubscriptionEmailBroadcasterViolateLSP(),
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
        account = Account(User("user1"), SubscriptionEmailBroadcasterViolateLSP())
        with self.assertRaises(AttributeError):
            account.on_account_created("event1")

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

from unittest import TestCase

from src.design_patterns.solid.dip import (
    ResearchViolateDIP,
    Person,
    Relationships,
    RelationshipsViolateDIP,
    Research,
)


class TestResearchViolateDIP(TestCase):
    def setUp(self) -> None:
        self.relationship = RelationshipsViolateDIP()
        self.research = ResearchViolateDIP(self.relationship)
        self.relationship.add_parent_and_child(Person("John"), Person("Chris"))
        self.relationship.add_parent_and_child(Person("John"), Person("Matt"))

    def test_query(self):
        self.assertEqual("Chris,Matt", self.research.query("John"))


class TestResearchFollowDIP(TestCase):
    def setUp(self) -> None:
        self.relationship = Relationships()
        self.research = Research(self.relationship)
        self.relationship.add_parent_and_child(Person("John"), Person("Chris"))
        self.relationship.add_parent_and_child(Person("John"), Person("Matt"))

    def test_query(self):
        self.assertEqual("Chris,Matt", self.research.query("John"))

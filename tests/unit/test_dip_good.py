from unittest import TestCase

from design_patterns.solid.dip.common import Person
from design_patterns.solid.dip.relationship_research_good import Relationships, Research


class TestResearchFollowDIP(TestCase):
    def setUp(self) -> None:
        self.relationship = Relationships()
        self.research = Research(self.relationship)
        self.relationship.add_parent_and_child(Person("John"), Person("Chris"))
        self.relationship.add_parent_and_child(Person("John"), Person("Matt"))

    def test_query(self):
        self.assertEqual("Chris,Matt", self.research.query("John"))

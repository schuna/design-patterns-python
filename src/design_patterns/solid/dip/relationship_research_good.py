from abc import abstractmethod

from design_patterns.solid.dip.common import Relationship


class RelationshipBrowser:
    @abstractmethod
    def find_all_children_of(self, name):
        raise NotImplementedError  # pragma: no cover


class Relationships(RelationshipBrowser):
    relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.PARENT, parent))

    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name


class Research:
    def __init__(self, browser):
        self.browser = browser

    def query(self, name):
        result = []
        for p in self.browser.find_all_children_of(name):
            result.append(p)
        return ",".join(result)

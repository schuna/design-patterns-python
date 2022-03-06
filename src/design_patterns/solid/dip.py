from abc import abstractmethod
from enum import Enum


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name):
        self.name = name


class RelationshipsViolateDIP:
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.CHILD, parent))


class RelationshipBrowser:
    @abstractmethod
    def find_all_children_of(self, name):
        raise NotImplementedError


class Relationships(RelationshipBrowser):
    relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.PARENT, parent))

    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name


class ResearchViolateDIP:
    def __init__(self, relationships):
        self.relations = relationships.relations

    def query(self, name):
        result = []
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                result.append(r[2].name)
        return ",".join(result)


class Research:
    def __init__(self, browser):
        self.browser = browser

    def query(self, name):
        result = []
        for p in self.browser.find_all_children_of(name):
            result.append(p)
        return ",".join(result)

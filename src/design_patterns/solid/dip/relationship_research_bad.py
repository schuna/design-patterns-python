from design_patterns.solid.dip.common import Relationship


class Relationships:
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.CHILD, parent))


class Research:
    def __init__(self, relationships):
        self.relations = relationships.relations

    def query(self, name):
        result = []
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                result.append(r[2].name)
        return ",".join(result)

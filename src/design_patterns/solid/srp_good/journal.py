class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.entries.append(f"{self.count}: {text}")
        self.count += 1

    def remove_entry(self, pos):
        if 0 > pos or pos >= self.count:
            raise ValueError
        del self.entries[pos]
        self.count -= 1

    def __str__(self):
        return "\n".join(self.entries)
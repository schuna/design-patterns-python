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

    # break SRP
    # def save(self, filename):
    #     file = open(filename, "w")
    #     file.write(str(self))
    #     file.close()
    #
    # def load(self, filename):
    #     pass
    #
    # def load_from_web(self, url):
    #     pass


class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        with open(filename, "w") as wf:
            wf.write(str(journal))

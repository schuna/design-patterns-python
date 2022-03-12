class Repository:
    @staticmethod
    def save_to_file(journal, filename):
        with open(filename, "w") as wf:
            wf.write(str(journal))

from design_patterns.command.active_object import Command, ActiveObject, SleepCommand


class DelayedTyper(Command):
    active_object = ActiveObject()
    stop = False

    def __init__(self, delay, ch):
        self.delay = delay
        self.its_char = ch

    def main(self):
        self.active_object.add_command(DelayedTyper(100, "1"))
        self.active_object.add_command(DelayedTyper(300, "3"))
        self.active_object.add_command(DelayedTyper(500, "5"))
        self.active_object.add_command(DelayedTyper(700, "7"))

        class StopCommand(Command):
            def execute(self):
                DelayedTyper.stop = True

        self.active_object.add_command(SleepCommand(1000, self.active_object, StopCommand()))
        self.active_object.run()

    def execute(self):
        print(f"{self.its_char}", end="")
        if not DelayedTyper.stop:
            self.delay_and_repeat()

    def delay_and_repeat(self):
        self.active_object.add_command(SleepCommand(self.delay, self.active_object, self))

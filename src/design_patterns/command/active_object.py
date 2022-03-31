import time

from abc import ABCMeta, abstractmethod


def current_time_milliseconds():
    return round(time.time() * 1000)


class Command(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        raise NotImplementedError  # pragma: no cover


class ActiveObject:
    def __init__(self):
        self.command_queue = []

    def add_command(self, command):
        self.command_queue.append(command)

    def run(self):
        while len(self.command_queue):
            command = self.command_queue.pop()
            command.execute()


class SleepCommand(Command):
    def __init__(self, milliseconds, active_object, wakeup_command):
        self.start_time = 0
        self.sleep_time = milliseconds
        self.active_object = active_object
        self.wakeup_command = wakeup_command
        self.started = False

    def execute(self):
        current_time = current_time_milliseconds()
        if not self.started:
            self.started = True
            self.start_time = current_time
            self.active_object.add_command(self)
        elif (current_time - self.start_time) < self.sleep_time:
            self.active_object.add_command(self)
        else:
            self.active_object.add_command(self.wakeup_command)


class WakeupCommand(Command):
    def execute(self):
        print("Command Executed!")

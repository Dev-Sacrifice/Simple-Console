from enum import Enum
from datetime import datetime


class Levels(Enum):
    FAILED = "\x1b[48;5;197m\x1b[38;5;255m ✗ \x1b[0m\x1b[38;5;197m"
    SUCCESS = "\x1b[48;5;171m\x1b[38;5;255m ✓ \x1b[0m\x1b[38;5;171m"
    INFO = "\x1b[48;5;111m\x1b[38;5;255m INF \x1b[0m\x1b[38;5;111m"
    DEBUG = "\x1b[48;5;129m\x1b[38;5;255m DBG \x1b[0m\x1b[38;5;129m"

    @property
    def priority(self):
        priorities = {
            Levels.FAILED: 0,
            Levels.SUCCESS: 1,
            Levels.INFO: 2,
            Levels.DEBUG: 3,
        }
        return priorities[self]


class Logger:
    RESET = "\x1b[0m"
    BLACK = "\x1b[38;5;8m"

    def __init__(
        self,
        log_level: Levels = Levels.DEBUG,
        log_file: str = None,
        show_timestamp: bool = True,
        show_brackets: bool = True,
        military_time: bool = False,
    ):
        self.show_timestamp = show_timestamp
        self.show_brackets = show_brackets
        self.military_time = military_time
        self.log_level = log_level
        self.log_file = log_file

    def timestamp(self) -> str:
        now = datetime.now()
        timestamp = (
            now.strftime("%H:%M:%S")
            if self.military_time
            else now.strftime("%I:%M:%S %p")
        )

        if self.show_brackets:
            return f"[{timestamp}]"

        return timestamp

    def log(self, level: Levels, message: str):
        timestamp = self.timestamp()

        if level.priority <= self.log_level.priority:
            if self.log_file:
                with open(self.log_file, "a") as fp:
                    fp.write(f"{timestamp} [{level.name}] - {message}\n")

            _timestamp_ = (
                f"{self.BLACK}{timestamp}{self.RESET}" if self.show_timestamp else ""
            )
            timestamp_for_console = f"{_timestamp_} " if _timestamp_ else ""

            print(f"{timestamp_for_console}{level.value} {message} {self.RESET}")

    def success(self, message: str):
        self.log(Levels.SUCCESS, message)

    def failed(self, message: str):
        self.log(Levels.FAILED, message)

    def debug(self, message: str):
        self.log(Levels.DEBUG, message)

    def info(self, message: str):
        self.log(Levels.INFO, message)

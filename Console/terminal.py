import os
import time
import ctypes
from threading import Thread, Event


class Terminal:
    @staticmethod
    def clear() -> None:
        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def set_title(title: str) -> None:
        ctypes.windll.kernel32.SetConsoleTitleW(title)

    @staticmethod
    def loader(
        done_event: Event,
        characters: list[str] = ["|", "/", "-", "\\"],
        message: str = "Loading...",
    ) -> None:
        while not done_event.is_set():
            for c in characters:
                print(f"{c} {message}", end="\r", flush=True)
                time.sleep(0.15)

            if done_event.is_set():
                break

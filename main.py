import sys

# Disable bytecode file generation
sys.dont_write_bytecode = True

from Console import Terminal, Logger, Levels
from threading import Event
import time


def simple_logger_example():
    # Initialize the Logger
    logger = Logger(log_level=Levels.SUCCESS, log_file="./app.log", show_brackets=True)

    # Log messages of different levels
    logger.success("Success")
    logger.failed("Failed")
    logger.info("Info")
    logger.debug("Debug")


def simple_terminal_example():
    # Clear the terminal and set title
    Terminal.clear()
    Terminal.set_title("Simple Console by @Dev-Sacrifice")

    # Show a loading spinner
    done_event = Event()
    loader_thread = Thread(target=Terminal.loader, args=(done_event, "Loading..."))
    loader_thread.start()

    # Simulate a task and stop the loader after 3 seconds
    time.sleep(3)
    done_event.set()
    loader_thread.join()

    print("Loading finished!")


if __name__ == "__main__":
    simple_logger_example()
    simple_terminal_example()

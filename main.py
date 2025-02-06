import sys

sys.dont_write_bytecode = True
from Console import Terminal, Logger, Levels

if __name__ == "__main__":
    Terminal.clear()
    Terminal.set_title("Simple Console by @Sacrifice")
    logger = Logger(Levels.SUCCESS, "./app.log", show_brackets=True)
    logger.success("Success")
    logger.failed("Failed")
    logger.info("Info")
    logger.debug("Debug")
    logger.log_level = Levels.FAILED

    logger.success("Success")
    logger.failed("Failed")
    logger.info("Info")
    logger.debug("Debug")

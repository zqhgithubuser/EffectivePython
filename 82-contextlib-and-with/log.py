import logging
from contextlib import contextmanager


@contextmanager
def log_level(level, name):
    logger = logging.getLogger(name)
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)

    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(levelname)s:%(name)s:%(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    try:
        yield logger
    finally:
        logger.setLevel(old_level)


with log_level(logging.DEBUG, "my-log") as my_logger:
    my_logger.debug(f"This is a message for {my_logger.name}!")
    logging.debug("This will not print")

logging.error("Error will print")

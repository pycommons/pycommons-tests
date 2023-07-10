import logging
import time


class TestUtils:
    @classmethod
    def delay(cls, millis: int, reason: str):
        logging.info("Delaying the thread by %s milliseconds; Reason: %s", millis, reason)
        time.sleep(millis / 1000)

import time

import Constants


class Timer:
    def __init__(self):
        self._start_time = 0

    def start(self):
        self._start_time = time.time()

    def has_elapsed(self, sec) -> bool:
        return time.time() - self._start_time >= sec

    def is_ready_to_shot(self):
        return self.has_elapsed(Constants.RELOAD_TIME)





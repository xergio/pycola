
import time
import random

class Item(object):

    def __init__(self, value):
        self._value = value


    def __call__(self):
        # pass
        time.sleep(random.random())


import time
import random

class Item(object):

    def __init__(self, value):
        self._value = value


    def __call__(self):
        # pass, do nothing with 'value'
        time.sleep(random.random())

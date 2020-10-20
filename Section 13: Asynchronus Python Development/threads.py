# atomic operation? an operation that can't be stopped during execution, it must finish it's execution

import time
import random

from threading import Thread

counter = 0

def increment_counter():
    global countercounter += 1
    time.sleep(random.random()) # let's do some FUZZING to see how it behaves now
    print(f"New Counter value: {counter}")
    time.sleep(random.random())
    print("-----------")


for x in range(10):
    t = Thread(target=increment_counter)
    time.sleep(random.random())
    t.start()


"""
be very careful with multi-threading
"""
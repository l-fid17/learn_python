import time

def ask_user():
    start = time.time()
    user_input = input("Input: ")
    greet = f"Hello, {user_input}"
    print(greet)
    print(f"ask_user() took {time.time() - start}")


def complex_calculation():
    start = time.time()
    print("Started calculating...")
    [x**2 for x in range(20000000)]
    print(f"complex_calculation() took {time.time() - start}")


# start = time.time()
# ask_user()
# complex_calculation()
# print(f"single thread took {time.time() - start}")


from threading import Thread

thread1 = Thread(target=complex_calculation)
thread2 = Thread(target=ask_user)

start = time.time()

thread1.start()
thread2.start()

thread1.join() # tells the thread to wait until it's finished
thread2.join()

print(f"double threads took {time.time() - start}")


"""
concurrent.futures
"""
import time
from concurrent.futures import ThreadPoolExecutor

start = time.time()

with ThreadPoolExecutor(max_workers=2) as pool:
    pool.submit(complex_calculation)
    pool.submit(ask_user)

print(f"double threads took {time.time() - start}")

import time
from multiprocessing import Process

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


process = Process(target=complex_calculation)
process2 = Process(target=ask_user)

process.start()
process2.start()

start = time.time()

process.join()
process2.join()

print(f"Two processes total time: {time.time() - start}")


"""
with concurrent.futures
"""

from concurrent.futures import ProcessPoolExecutor

with ProcessPoolExecutor(max_workers=2) as pool:
    pool.submit(complex_calculation)
    pool.submit(complex_calculation)


print(f"Two processes total time: {time.time() - start}")

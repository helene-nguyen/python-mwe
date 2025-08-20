"""
Multithreading example (for I/O-bound tasks)
Python allows you to run multiple threads within a single process.
Threads are lightweight units of execution that can run concurrently,
especially useful for I/O-bound tasks like reading files, network requests, or waiting for user input.
However, due to Python’s Global Interpreter Lock (GIL), only one thread can execute Python bytecode at a time,
so multithreading doesn’t provide true parallelism for CPU-intensive tasks
"""
import threading
import time

def print_numbers():
    for i in range(5):
        print(f"Number {i}")
        time.sleep(1)  # simulate I/O wait

thread = threading.Thread(target=print_numbers)
thread.start()

print("Main thread continues...")
thread.join()
print("Thread finished.")
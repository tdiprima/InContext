import time
from contextlib import contextmanager


@contextmanager
def timer(label: str):
    start_time = time.time()
    try:
        yield
    finally:
        end_time = time.time()  # Record end time
        elapsed_time = end_time - start_time
        print(f"{label} took {elapsed_time:.4f} seconds")


with timer("Sleeping for 2 seconds"):
    time.sleep(2)

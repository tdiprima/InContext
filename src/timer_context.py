import time
from contextlib import contextmanager


@contextmanager
def timer(label="Operation"):
    start = time.time()
    yield
    end = time.time()
    print(f"[{label}] took {end - start:.4f} seconds")


# Dummy function to demonstrate
def process_data():
    time.sleep(1)  # Simulate work


if __name__ == "__main__":
    with timer("Data Processing"):
        process_data()

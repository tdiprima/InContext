import time


class Timer:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        print(f"Took {time.time() - self.start:.2f}s")


with Timer():
    sum(i**2 for i in range(10**6))

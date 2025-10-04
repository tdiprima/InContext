# Stacking context managers like they're Pringles - you can't stop at just one fr fr
import os
import sys
import time
from contextlib import contextmanager

from rich import print


# Class-based Timer
class Timer:
    def __init__(self, label="Block"):
        self.label = label

    def __enter__(self):
        self.start = time.time()
        return self  # Optional: allows 'as' usage if needed

    def __exit__(self, *args):
        end = time.time()
        print(
            f"[bold magenta][{self.label}] took {end - self.start:.4f} seconds[/bold magenta]"
        )
        return False  # Propagate exceptions if any


# Generator-based suppress_stdout
@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:
            yield
        finally:
            sys.stdout = old_stdout


# Generator-based throttle
@contextmanager
def throttle(seconds):
    yield
    time.sleep(seconds)


# Dummy function to simulate a job (prints output and takes time)
def run_job():
    print("[bold magenta]Starting job... (this would be suppressed)[/bold magenta]")
    # Simulate some work
    total = sum(i for i in range(1000000))
    print(f"[bold magenta]Job completed with result: {total}[/bold magenta]")
    time.sleep(0.2)  # Add a bit of delay to see timer in action


# Stacking example
if __name__ == "__main__":
    print("[bold magenta]Starting stacked context managers...[/bold magenta]")
    with Timer("Job"), suppress_stdout(), throttle(0.5):
        run_job()
    print("[bold magenta]Stacked contexts completed.[/bold magenta]")

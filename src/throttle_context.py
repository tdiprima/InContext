# Slow your roll with this rate limiter - no spam allowed, we're classy like that ✨
import time
from contextlib import contextmanager

from rich import print


@contextmanager
def throttle(seconds):
    yield
    time.sleep(seconds)


# Dummy function to demonstrate
def ping_api():
    print("[bold white]Pinging API...[/bold white]")


if __name__ == "__main__":
    for _ in range(5):
        with throttle(1):  # Pause 1 second between calls
            ping_api()

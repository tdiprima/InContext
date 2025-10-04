# Thread safety is giving main character energy - no race conditions allowed 🚫
import threading
from contextlib import contextmanager

from rich import print

lock = threading.Lock()


@contextmanager
def thread_safe():
    lock.acquire()
    try:
        yield
    finally:
        lock.release()


# Shared resource (dummy)
shared_counter = 0


# Dummy function to demonstrate
def update_shared_resource():
    global shared_counter
    shared_counter += 1
    print(f"[bold blue]Updated shared counter to: {shared_counter}[/bold blue]")


if __name__ == "__main__":
    # Simulate concurrent updates (in a simple way; in real code, use threads)
    with thread_safe():
        update_shared_resource()
    with thread_safe():
        update_shared_resource()

    # To demonstrate threading, let's create threads
    def threaded_update():
        with thread_safe():
            update_shared_resource()

    threads = [threading.Thread(target=threaded_update) for _ in range(3)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

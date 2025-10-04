# Shutting up noisy functions because we don't need that energy rn ✋
import os
import sys
from contextlib import contextmanager

from rich import print


@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:
            yield
        finally:
            sys.stdout = old_stdout


# Dummy function to demonstrate
def noisy_func():
    print("Loud output you don't care about.")
    print("More noise!")


if __name__ == "__main__":
    # Without suppression (for comparison)
    print("[bold green]Without suppression:[/bold green]")
    noisy_func()

    # With suppression
    print("[bold green]\nWith suppression (you won't see the noise):[/bold green]")
    with suppress_stdout():
        noisy_func()
    print("[bold green]Suppression ended.[/bold green]")

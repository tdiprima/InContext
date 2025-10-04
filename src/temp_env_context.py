# Environment variables on a temporary flex - here today, gone tomorrow bestie
import os
from contextlib import contextmanager

from rich import print


@contextmanager
def temp_env(key, value):
    original = os.environ.get(key)
    os.environ[key] = value
    try:
        yield
    finally:
        if original is None:
            del os.environ[key]
        else:
            os.environ[key] = original


# Dummy function to demonstrate
def run_tests():
    print(f"[bold red]ENV_MODE is: {os.environ.get('ENV_MODE', 'Not set')}[/bold red]")


if __name__ == "__main__":
    # Before
    print("[bold red]Before context:[/bold red]")
    run_tests()

    # Inside context
    with temp_env("ENV_MODE", "test"):
        print("[bold red]\nInside context:[/bold red]")
        run_tests()

    # After
    print("[bold red]\nAfter context:[/bold red]")
    run_tests()

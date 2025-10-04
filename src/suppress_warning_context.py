# Making warnings disappear like my motivation on Monday mornings 💀
import warnings
from contextlib import contextmanager

from rich import print


@contextmanager
def suppress_specific_warning(warning_type):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", warning_type)
        yield


# Dummy function to demonstrate
def some_function_that_warns():
    warnings.warn("This is a test warning!", UserWarning)
    print("[bold yellow]Function executed.[/bold yellow]")


if __name__ == "__main__":
    # Without suppression (for comparison)
    print("[bold yellow]Without suppression:[/bold yellow]")
    some_function_that_warns()

    # With suppression
    print("[bold yellow]\nWith suppression:[/bold yellow]")
    with suppress_specific_warning(UserWarning):
        some_function_that_warns()

"""
ExitStack is literally the GOAT for handling multiple files 💯
No cap, nested 'with' statements are giving major cringe energy
This bad boy keeps your code clean and your files managed - periodt
"""

from contextlib import ExitStack

from rich import print

files = ["a.txt", "b.txt", "c.txt"]
with ExitStack() as stack:
    handles = [stack.enter_context(open(f)) for f in files]
    data = [h.read() for h in handles]
    print(f"[bold cyan]Successfully processed {len(files)} files![/bold cyan]")

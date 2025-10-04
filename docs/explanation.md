# Python Context Management

## Decorator

Normally, a **context manager** in Python is something you can use in a `with` statement:

```python
with open("file.txt") as f:
    data = f.read()
```

That works because `open()` returns an object that implements the context manager protocol (`__enter__` and `__exit__`).

Now, writing your own context manager from scratch means you'd have to implement a whole class with `__enter__` and `__exit__`:

```python
class MyCtx:
    def __enter__(self):
        print("entering")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print("exiting")
```

That's boilerplate-y as hecc.

---

### What `@contextmanager` Does

The `@contextmanager` decorator (from `contextlib`) lets you write a context manager **as a generator function** instead of a whole class.

Example:

```python
from contextlib import contextmanager

@contextmanager
def my_ctx():
    print("entering")
    yield  # execution jumps back to caller inside `with`
    print("exiting")
```

And then:

```python
with my_ctx():
    print("doing stuff")
```

Output:

```
entering
doing stuff
exiting
```

---

### How it Works

* The code **before `yield`** acts like `__enter__`.
* The code **after `yield`** acts like `__exit__`.
* Whatever you `yield` becomes the value assigned to the variable in `with ... as ...`.

Example:

```python
@contextmanager
def open_file(path, mode):
    f = open(path, mode)
    try:
        yield f  # this is what `as f` gets
    finally:
        f.close()
```

Now you can use:

```python
with open_file("data.txt", "w") as f:
    f.write("hello")
```

---

### TL;DR

Adding `@contextmanager`:

* Saves you from writing a class with `__enter__`/`__exit__`.
* Lets you describe setup/teardown logic with a generator function and `yield`.
* Makes your code cleaner and more Pythonic when you just need lightweight resource management.

## What happens when an exception is raised

Let's see what happens when stuff blows up inside a `with` block. 👌

Using our custom context manager:

```python
from contextlib import contextmanager

@contextmanager
def demo():
    print("entering")
    try:
        yield
    finally:
        print("exiting")
```

Now let's use it:

```python
with demo():
    print("inside")
    raise ValueError("boom")
```

**Output:**

```
entering
inside
exiting
Traceback (most recent call last):
  ...
ValueError: boom
```

👉 Notice:

* The code **before `yield`** ran (`entering`).
* The code inside the `with` block ran (`inside`).
* Even though we raised an exception, the code **after `yield`** in the context manager (`finally: exiting`) still ran.
* Then the exception bubbled up like normal.

---

### Why this matters

This is gold for **resource cleanup**. Imagine handling files, DB connections, locks, etc. — even if an exception happens, you still guarantee cleanup:

```python
@contextmanager
def open_file(path, mode):
    f = open(path, mode)
    try:
        yield f
    finally:
        print("closing file")
        f.close()

with open_file("test.txt", "w") as f:
    f.write("hello")
    raise RuntimeError("oh no")
```

Output:

```
closing file
Traceback (most recent call last):
  ...
RuntimeError: oh no
```

The file **always** gets closed — no leaks.

---

⚡️ So the TL;DR:
When an exception happens inside the `with` block, the `@contextmanager` decorator makes sure the cleanup code after the `yield` **still runs no matter what**. That's the real superpower.

&mdash; *gpt-5*

<br>

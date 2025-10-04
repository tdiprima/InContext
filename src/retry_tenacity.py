"""
Retry mechanism demonstration that attempts a flaky task up to 3 times before giving up.
The key is to specify which exceptions trigger a retry.
"""

import random

from tenacity import retry, retry_if_exception_type, stop_after_attempt


@retry(stop=stop_after_attempt(3), retry=retry_if_exception_type(Exception))
def flaky_task():
    if random.random() < 0.7:
        raise Exception("Failed!")
    return "Success!"


print(flaky_task())

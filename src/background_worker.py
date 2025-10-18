"""
Well now, listen here - this here's a simple way to wrangle them background tasks.
See, when you fire off a worker task, you gotta make sure it don't just run wild after you're done with it.
This little helper makes sure when you're finished, them tasks get cleaned up proper-like.
Ain't nobody got time for tasks runnin' loose like chickens with their heads cut off!
"""

import asyncio
import contextlib
from contextlib import asynccontextmanager


@asynccontextmanager
async def background_worker(coro):
    task = asyncio.create_task(coro)
    try:
        yield task
    finally:
        task.cancel()
        with contextlib.suppress(asyncio.CancelledError):
            await task


async def ticker():
    while True:
        print("tick")
        await asyncio.sleep(1)


async def handler():
    async with background_worker(ticker()):
        await asyncio.sleep(3)


asyncio.run(handler())

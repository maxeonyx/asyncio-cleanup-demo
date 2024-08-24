import asyncio

from .utils import name_task, log, trace


@name_task
async def task_1_SIMPLE():
    try:
        await asyncio.sleep(99)
    finally:
        log("cleanup! 😃")


@name_task
async def task_2_ERROR():
    try:
        trace("Wait 3s for Exception...\n")
        await asyncio.sleep(3)
        raise Exception("task_ERROR: error!")
    finally:
        log("cleanup! 😃")


async def main():
    await asyncio.gather(
        task_1_SIMPLE(),
        task_2_ERROR(),
    )


asyncio.run(main())

# Exception:         ✅
# KeyboardInterrupt: ✅
# SIGTERM:           Total failure.

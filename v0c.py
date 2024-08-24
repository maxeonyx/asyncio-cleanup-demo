import asyncio
import signal

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


def on_signal(sig, loop):
    trace(f"signal: {sig.name}")
    loop.stop()


async def main():
    loop = asyncio.get_running_loop()
    loop.add_signal_handler(signal.SIGTERM, on_signal, signal.SIGTERM, loop)

    await asyncio.gather(
        task_1_SIMPLE(),
        task_2_ERROR(),
    )


asyncio.run(main())

# Exception:         ✅
# KeyboardInterrupt: ✅
# SIGTERM:           Total failure.

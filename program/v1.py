import asyncio
import signal

from .tasks import task_1_SIMPLE, task_2_ERROR
from .utils import trace, log, name_task


@name_task
async def task_3_ASYNC():
    try:
        await asyncio.sleep(99)
    except asyncio.CancelledError:
        trace("cancelled!")
        raise
    finally:
        await asyncio.sleep(0.1)
        log("cleanup! 😃")


@name_task
async def task_4_HANG():
    try:
        await asyncio.sleep(99)
    except asyncio.CancelledError:
        trace("cancelled!")
        raise
    finally:
        trace("hanging...")
        await asyncio.sleep(99)
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
        task_3_ASYNC(),
        task_4_HANG(),
    )


asyncio.run(main())

# Exception:         Hangs.
# KeyboardInterrupt: task_3 cleanup skipped & hangs.
# SIGTERM:           Hangs.

import asyncio
import signal

from .tasks import task_1_SIMPLE, task_3_ASYNC, task_2_ERROR, task_4_HANG
from .utils import trace


def on_signal(sig, loop):
    trace(f"signal: {sig.name}")
    loop.stop()


async def main():
    loop = asyncio.get_running_loop()
    loop.add_signal_handler(signal.SIGTERM, on_signal, signal.SIGTERM, loop)

    async with asyncio.TaskGroup() as tg:
        tg.create_task(task_1_SIMPLE())
        tg.create_task(task_2_ERROR())
        tg.create_task(task_3_ASYNC())
        tg.create_task(task_4_HANG())


asyncio.run(main())

# Exception:         Hangs.
# KeyboardInterrupt: Hangs.
# SIGTERM:           Hangs.

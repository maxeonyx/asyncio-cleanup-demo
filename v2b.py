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
    loop.add_signal_handler(signal.SIGINT, on_signal, signal.SIGINT, loop)

    await asyncio.gather(
        task_1_SIMPLE(),
        task_2_ERROR(),
        task_3_ASYNC(),
        task_4_HANG(),
    )


asyncio.run(main())

# Exception:         Hangs.
# KeyboardInterrupt: Hangs.
# SIGTERM:           Hangs.

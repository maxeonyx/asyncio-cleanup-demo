import asyncio

from .utils import trace


def asyncio_run_with_timeout(main_coro, timeout):
    loop = asyncio.new_event_loop()
    main_task = loop.create_task(main_coro, name=main_coro.__name__)
    try:
        return loop.run_until_complete(main_task)
    finally:
        _cancel_all_tasks_with_timeout(loop, timeout)
        loop.run_until_complete(loop.shutdown_asyncgens())
        loop.run_until_complete(loop.shutdown_default_executor(timeout))


# Pretty much copied from asyncio.run() source code
def _cancel_all_tasks_with_timeout(loop, timeout):
    to_cancel = asyncio.all_tasks(loop)
    if not to_cancel:
        return

    for task in to_cancel:
        trace(f"cancelling {task.get_name()}")
        task.cancel()

    trace(f"waiting {timeout}s tasks to cancel...")
    done, pending = loop.run_until_complete(
        asyncio.wait(to_cancel, timeout=timeout, return_when=asyncio.ALL_COMPLETED)
    )

    if pending:
        trace("shutdown timeout!")
        for task in pending:
            trace(f"{task.get_name()} didn't finish in time")

    for task in done:
        if task.cancelled():
            continue
        if task.exception() is not None:
            trace(
                f"{task.get_name()} raised an exception during shutdown: {task.exception()}"
            )

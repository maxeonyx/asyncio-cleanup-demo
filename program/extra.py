import asyncio


async def better_shield(coro):
    task = asyncio.create_task(coro)
    try:
        await asyncio.shield(task)
    except asyncio.CancelledError:
        await task
        raise

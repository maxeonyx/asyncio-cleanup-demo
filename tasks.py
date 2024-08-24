import asyncio

from .utils import ainput, trace, log, name_task


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

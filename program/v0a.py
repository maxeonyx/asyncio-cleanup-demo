import asyncio


async def task_1_SIMPLE():
    await asyncio.sleep(99)


async def task_2_ERROR():
    print("Wait 3s for Exception...\n")
    await asyncio.sleep(3)
    raise Exception("task_ERROR: error!")


async def main():
    await asyncio.gather(
        task_1_SIMPLE(),
        task_2_ERROR(),
    )


asyncio.run(main())

# Exception:         ✅
# KeyboardInterrupt: ✅
# SIGTERM:           ✅

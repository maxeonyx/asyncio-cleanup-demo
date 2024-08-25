import asyncio


async def connect():
    await asyncio.open_connection("host", "port")


async def fail_after_3s():
    print("Wait 3s for Exception...\n")
    await asyncio.sleep(3)
    raise Exception("ERROR!")


async def main():
    await asyncio.gather(
        connect(),
        fail_after_3s(),
    )


asyncio.run(main())

# Exception:         ✅
# KeyboardInterrupt: ✅
# SIGTERM:           ✅

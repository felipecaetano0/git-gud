import asyncio


async def method(i):
    print(f"Entering {i}")
    await asyncio.sleep(i)
    print(f"Exiting {i}")


async def coordinator():
    print("Starting Coordinator")
    task1 = asyncio.create_task(method(1))
    task2 = asyncio.create_task(method(2))
    print("Tasks Created...")
    await task1
    await task2
    print("Coordinator Finished")


if __name__ == "__main__":
    asyncio.run(coordinator())

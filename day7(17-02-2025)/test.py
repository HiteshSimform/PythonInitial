import asyncio

async def compute():
    await asyncio.sleep(2)
    return "Result ready"

async def main():
    future = asyncio.ensure_future(compute())
    print("Task started")
    result = await future
    print(result)

asyncio.run(main())
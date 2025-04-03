import asyncio

async def my_coroutine():
    print("Start coroutine")
    await asyncio.sleep(1)  # Simulate an asynchronous operation
    print("End coroutine")
    return 42

# Running the coroutine
async def main():
    result = await my_coroutine()
    print(f"Result: {result}")

# Run the main coroutine
asyncio.run(main())
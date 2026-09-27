"""Question: Write an async function square_after_delay(n) that sleeps for 1 second then returns n ** 2. 
Use asyncio.gather to run it for n in [1, 2, 3, 4, 5] concurrently, and print the list of results. It should
take ~1 second total, not 5."""

#Answer:
import asyncio
async def square_after_delay(n):
    await asyncio.sleep(1)
    return n ** 2 
async def main():
    results = await asyncio.gather(*(square_after_delay(n) for n in [1, 2, 3, 4, 5]))
    print(results)
asyncio.run(main())

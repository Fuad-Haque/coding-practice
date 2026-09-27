"""Question: Write an async function countdown(n) that prints numbers from n down to 1, waiting 1 second
between each (use asyncio.sleep), then prints "Liftoff!". Run it with asyncio.run."""


#Answer:

import asyncio

async def countdown(n):
    for i in range(n, 0, -1):
        print(i)
        await asyncio.sleep(1)
    print("Liftoff!")

asyncio.run(countdown(3))
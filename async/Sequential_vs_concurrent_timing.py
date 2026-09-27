"""Question: Write three coroutines brew_coffee(), toast_bread(), fry_egg() that each sleep for 3,2,
and 4 seconds respectively (simulating cooking time) and then print they're done. First run them sequentially
and time it. Then run them concurrently with gather and time it. Confirm the concurrent version takes about as
long as the slowest single task (~4s), not the sum(~9s)."""

#Answer:
import asyncio
import time
async def brew_coffee():
    print("Brewing coffee in just a second...")
    await asyncio.sleep(3)
    print("Coffee brewed!")
async def toast_bread():
    print("Starting to toast bread, just put it in the oven...")
    await asyncio.sleep(2)
    print("Bread successfully toasted in 2 seconds")
async def fry_egg():
    print("Frying egg, your protein will be ready in a jiffy!...")
    await asyncio.sleep(4)
    print("Egg fried!")  
async def main():
    start = time.time()
    await brew_coffee()
    await toast_bread()
    await fry_egg()
    print(f"Sequential: {time.time() - start:.1f}s")
    start = time.time()
    await asyncio.gather(brew_coffee(), toast_bread(), fry_egg())
    print(f"Concurrent: {time.time() - start:.1f}s")

asyncio.run(main())
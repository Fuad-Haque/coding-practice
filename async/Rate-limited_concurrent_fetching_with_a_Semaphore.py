"""Question: You have 20 URLs to fetch, but you don't want to blast the server with 20 simultaneous requests
-- you want to limit yourself to at most 5 concurrent requests at a time. Use asyncio.Semaphore(5) to cap concurrency.
(A semaphore is a bouncer with 5 tickets -- a coroutine must acquire a ticket before proceeding, and give it back
when done, so only 5 can be "inside" at once.)"""

#Answer:
import asyncio
import httpx
urls = [f"https://api.github.com/users/octocat" for _ in range(20)]
async def fetch_with_limit(client, url, semaphore):
    async with semaphore:
        response = await client.get(url, timeout=10.0)
        return response.status_code
async def main():
    semaphore = asyncio.Semaphore(5)
    async with httpx.AsyncClient() as client:
        tasks = [fetch_with_limit(client, url, semaphore) for url in urls]
        results = await asyncio.gather(*tasks)
        print(results)
        print(f"Fetched {len(results)} URLs with max 5 concurrent")
asyncio.run(main())
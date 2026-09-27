"""Use httpx.AsyncClient to GET https://api.github.com/zen (returns a random piece of GitHub "zen" wisdom
as plain text) and print the response text and status code."""

#Answer:
import asyncio
import httpx
async def main():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.github.com/zen")
        print(response.status_code)
        print(response.text)
asyncio.run(main())
"""Question: You have this list of URLs:
urls = [
    "https://api.github.com/users/torvalds",
    "https://api.github.com/users/gvanrossum",
    "https://api.github.com/users/octocat",
]
Write a function that fetches all three concurrently, and for each, prints the GitHub username (login field
from JSON) and their number of public repos (public_repos field). Handle the case where a request might fail
(use return_execptions=True in gather, or try/except inside the fetch function)."""

#Answer:
import asyncio
import httpx
urls = [
    "https://api.github.com/users/torvalds",
    "https://api.github.com/users/gvanrossum",
    "https://api.github.com/users/octocat",
]
async def fetch_user(client, url):
    try:
        response = await client.get(url, timeout=10.0)
        response.raise_for_status()
        data = response.json()
        return data["login"], data["public_repos"]
    except httpx.HTTPError as e:
        return f"Error fetching {url}", str(e)
async def main():
    async with httpx.AsyncClient() as client:
        results = await asyncio.gather(*(fetch_user(client, url) for url in urls))
        for login, repos in results:
            print(f"{login}: {repos}")
asyncio.run(main())
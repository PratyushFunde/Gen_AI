import asyncio
import aiohttp
import time

url="https://httpbin.org/delay/3"

async def fetch_url(session,url):
    async with session.get(url) as response:
        print(f"Fetched {url} with status {response.status}")

async def main():
    start=time.time()
    urls=["https://postman-echo.com/get"]*30
    async with aiohttp.ClientSession() as session:
       tasks= [fetch_url(session,url) for url in urls]
       await asyncio.gather(*tasks)
    end=time.time()
    print(f"Total time taken is {end-start:.2f}")

asyncio.run(main())
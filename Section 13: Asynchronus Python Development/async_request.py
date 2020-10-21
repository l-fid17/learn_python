import asyncio
import time

try:
    import aiohttp
    import async_timeout
except:
    import pip
    pip.main(["install", "aiohttp"])
    import aiohttp
    import async_timeout

async def fetch_page(session, url):
    page_start = time.time()
    async with async_timeout.timeout(10):
        async with session.get(url) as response:
            print(f"Page took {time.time() - page_start}s to load")
            return response.status


async def get_multiple_pages(loop, urls):
    tasks = []
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            tasks.append(fetch_page(session, url))
        grouped_tasks = asyncio.gather(*tasks)
        return await grouped_tasks
        
# loop = asyncio.get_event_loop()
# loop.run_until_complete(fetch_page("http://books.toscrape.com"))

# print("--------------")

# tasks = [fetch_page("http://books.toscrape.com") for i in range(50)]
# start = time.time()
# loop.run_until_complete(asyncio.gather(*tasks))
# print(f"Loading all took {time.time() - start}s to load")

loop = asyncio.get_event_loop()

urls = ["http://books.toscrape.com" for i in range(50)]
start = time.time()
loop.run_until_complete(get_multiple_pages(loop, urls))
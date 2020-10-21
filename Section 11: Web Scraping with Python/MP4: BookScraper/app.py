import asyncio, aiohttp,async_timeout, time
import requests
import logging

from pages.all_books_page import AllBooksPage

logging.basicConfig(
    format='%(ascitime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%d-%m-%Y %H:%M:%S',
    level=logging.CRITICAL,
    filename='logs.txt'
)
logger = logging.getLogger('scraping')

logger.info("Loading books list...")


response = requests.get("http://books.toscrape.com/")
content = response.content

page = AllBooksPage(content)

loop = asyncio.get_event_loop()

books = page.books

async def fetch_page(session, url):
    page_start = time.time()
    async with async_timeout.timeout(10):
        async with session.get(url) as response:
            print(f"Page took {time.time() - page_start}s to load")
            return await response.text()


async def get_multiple_pages(loop, urls):
    tasks = []
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            tasks.append(fetch_page(session, url))
        grouped_tasks = asyncio.gather(*tasks)
        return await grouped_tasks


urls = [f"http://books.toscrape.com/catalogue/page-{page_num+1}.html" for page_num in range(1, page.page_count)]
start = time.time()
pages = loop.run_until_complete(get_multiple_pages(loop, urls))
print(f"Total pages requests took {time.time() - start}s")

for page_content in pages:
    logger.debug("Creating AllBooksPage from page content.")
    page = AllBooksPage(page_content)
    books.extend(page.books)



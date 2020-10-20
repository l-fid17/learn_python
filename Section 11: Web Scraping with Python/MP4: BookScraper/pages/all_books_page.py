import re
import logging

try:
    from bs4 import BeautifulSoup
except:
    import pip
    pip.main(["install", "beautifulsoup4"])
    from bs4 import BeautifulSoup

from locators.all_books_page import AllBooksPageLocators
from parsers.book_parser import BookParser

logger = logging.getLogger("scraping.all_books_page")

class AllBooksPage:
    def __init__(self, page_content):
        logger.debug("Parsing page content with BeautifulSoup HTML parser.")
        self.soup = BeautifulSoup(page_content, "html.parser")

    @property
    def books(self):
        logger.debug(f"Finding all books in the page using `{AllBooksPageLocators.BOOKS}`.")
        return [BookParser(e) for e in self.soup.select(AllBooksPageLocators.BOOKS)]

    @property
    def page_count(self):
        logger.debug("Finding the number of all pages available...")
        content = self.soup.select_one(AllBooksPageLocators.PAGER).string
        pattern = "Page [0-9]+ of ([0-9]+)"
        matcher = re.search(pattern, content)
        page_count = int(matcher.group(1))
        logger.info(f"Found `{page_count}` page(s) available.")
        logger.debug(f"Extracted number of pages as int: `{page_count}`.")
        return page_count
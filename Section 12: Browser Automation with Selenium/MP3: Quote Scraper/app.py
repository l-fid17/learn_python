"""
Milestone Project 3: A Quote Scraper
"""
try:
    from selenium import webdriver
except:
    import pip
    pip.main(["install", "selenium"])
    from selenium import webdriver


from pages.quotes_page import QuotesPage

chrome = webdriver.Chrome(executable_path="/home/luca/chromedriver")
chrome.get("http://quotes.toscrape.com")
page = QuotesPage(chrome)

for quote in page.quotes:
    print(quote)
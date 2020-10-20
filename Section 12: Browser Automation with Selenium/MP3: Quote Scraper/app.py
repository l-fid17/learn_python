"""
MP3: Rewrite A Quote Scraper using Selenium instead of bs4
"""
try:
    from selenium import webdriver
except:
    import pip
    pip.main(["install", "selenium"])
    from selenium import webdriver


from pages.quotes_page import QuotesPage, InvalidTagForAuthorError

try:
    author = input("Enter the name of the author: ")
    tag = input("Enter tag: ")

    chrome = webdriver.Chrome(executable_path="/home/luca/chromedriver")
    chrome.get("http://quotes.toscrape.com/search.aspx")
    page = QuotesPage(chrome)

    print(page.search_for_quotes(author, tag))
except InvalidTagForAuthorError as e:
    print(e)
except Exception as e:
    print(e)
    print("An unknown error occurred. Please try again.")
    
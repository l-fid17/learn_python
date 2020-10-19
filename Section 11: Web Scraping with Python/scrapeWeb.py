import requests

try:
    from bs4 import BeautifulSoup
except:
    import pip
    pip.main(["install", "beautifulsoup4"])


page = requests.get("http://example.com/")
soup = BeautifulSoup(page.content, "html.parser")
print(soup)
print(soup.find("h1").string)
print([x.string for x in soup.find_all("p")])
try:
    from bs4 import BeautifulSoup
except:
    import pip
    pip.main(["install", "beautifulsoup4"])
    from bs4 import BeautifulSoup


SIMPLE_HTML = """
<html>
    <body>
        <h1>Hello</h1>
        <p class="subtitle">and welcome</p>
        <div>
            <p>Just some text</p>
        </div>
        <div>
            <li><a href="www.link.here">Link</a></li>
            <li>item2</li>
            <li>item3</li>
        </div>
    </body>
</html>
"""

simple_soup = BeautifulSoup(SIMPLE_HTML, 'html.parser')

print(simple_soup.find("h1").string)

def find_list_items(el):
    list_items = simple_soup.find_all(el)
    list_contents = [c.string for c in list_items]
    return list_contents

li_items = find_list_items("li")
print(li_items)

def find_subtitle():
    p = simple_soup.find('p', {'class': 'subtitle'})
    return p.string

subt = find_subtitle()
print(subt)

def find_nested_element():
    locator = 'div p' # also called css locator
    item_name = simple_soup.select_one(locator)
    return item_name


item = find_nested_element()
print(item.string)

def use_attrs(): # to read attributes e.g. href
    link = simple_soup.select_one('a').attrs['href']
    return link


link = use_attrs()
print(link)
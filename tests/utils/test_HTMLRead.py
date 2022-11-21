from novelscraper.utils.HTMLRead import get_html
from bs4 import BeautifulSoup



def test_get_html():
    html_doc = """<html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title"><b>The Dormouse's story</b></p>

    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>

    <p class="story">...</p>
    """

    soup: BeautifulSoup = get_html(html_string=html_doc)
    print(soup.title)
    assert(soup.title.name == "title")
    assert(soup.title.string == "The Dormouse's story")








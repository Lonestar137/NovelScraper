from bs4 import BeautifulSoup

# example constant variable
NAME = "novelscraper"


def get_html(html_string)->BeautifulSoup:
    soup: BeautifulSoup = BeautifulSoup(html_string, 'html.parser')
    return soup



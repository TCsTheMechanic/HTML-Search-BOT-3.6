from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

def names_searcher():
    html_code = urlopen("https://overwatch.gamepedia.com/Category:Quotations").read()
    soup = BeautifulSoup(html_code, features="html.parser")
    data = soup.find_all(href=re.compile("./Quotes"))

    names_list = []
    for item in data:
        if '%' not in str(item):
            #remove tags before the name
            item = str(item).replace('<a href="/', '')
            #add item on names_list until find /Q
            names_list.append(item[:item.find('/Q')])

    return names_list

#links_searcher()
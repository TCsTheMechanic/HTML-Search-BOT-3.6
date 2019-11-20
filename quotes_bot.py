from names_bot import names_searcher
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

def quotes_searcher():
    quotes_file = open("quotes_file.txt", "w")

    #single test enviroment
    #test_names = ["Mercy"]
    #for name in test_names:

    for name in names_searcher():
        print("Searching "+ name +" quotes...")
        html_code = urlopen("https://overwatch.gamepedia.com/" + name + "/Quotes").read()
        soup = BeautifulSoup(html_code, features="html.parser")
        data = soup.find_all(href=re.compile("https://overwatch.gamepedia.com/File:."))

        quotes_list = ["something"]
        for item in data:
            #remove tags before the quotes
            item = str(item).replace('<a href="https://overwatch.gamepedia.com/File:', '')
            item = item.replace('_', ' ')
            #verify if is it a real quote
            if name + ' - ' in item:
                #remove test quotes
                if '%' not in item:
                    if '.wav"' in item:
                        #remove duplicated quotes
                        if quotes_list[-1] != item[:item.find('.wav"')]:
                            #add item on quotes_list until find .wav"
                            quotes_list.append(item[:item.find('.wav"')])
                    elif '.ogg"' in item:
                        if quotes_list[-1] != item[:item.find('.ogg"')]:
                            quotes_list.append(item[:item.find('.ogg"')])
                    else:
                        if quotes_list[-1] != item[:item.find('.mp3"')]:
                            quotes_list.append(item[:item.find('.mp3"')])
        quotes_list.pop(0)
        quotes_file.write("#--------------------------" + name + "'s quotes--------------------------\n")
        for quote in quotes_list:
            quote = quote.replace(name + ' - ', '')
            #remove links after some quotes
            if '>' in quote:
                quotes_file.write('"' + quote[:quote.find('>')] + '\n')
            else:
                quotes_file.write('"' + quote + '"\n')
    quotes_file.close()

quotes_searcher()
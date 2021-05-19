import requests
from bs4 import BeautifulSoup

page = 1
next_btn = True

while next_btn:
    website = requests.get('https://quotes.toscrape.com/page/' + str(page))
    soup = BeautifulSoup(website, 'html.parser')

    next_btn = soup.select_one('.next > a')
    quotes = soup.select('.quote')

    for quote in quotes:
        text = quote.select_one('.text')
        author = quote.select_one('.author')
        tags = quote.select('.tag')
        print(text.text)
        print(author.text)
        for tag in tags:
            print(tag.text, sep=', ')
        print('======================================\n')
    print('Scraped page', page, '\n\n')
    page += 1

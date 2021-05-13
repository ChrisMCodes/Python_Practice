import requests
from bs4 import BeautifulSoup

website = requests.get('https://quotes.toscrape.com/')

# print(website.text) # .text gets full html of site


soup = BeautifulSoup(website.text, 'html.parser')

'''
title = soup.find('title')
print(title.text) # .text gets content without tag
'''

'''
quote = soup.find(class_='text') # find returns first of its kind
print(quote.text)
'''
'''
quotes = soup.find_all(class_='text')
print(quotes) # in iterable list
'''
'''
login_link = soup.find(href='/login')
print(login_link)
'''
'''
# Selecting text and author
quote = soup.find(class_='quote')
quote_text = quote.find(class_='text')
quote_author = quote.find(class_='author')
print(quote.text, quote_author.text)
'''

# You can also select by css tag
# using .select (for all) or
# .select_one (for the first)

quotes = soup.select(".text")
# returns an array
print(quotes)

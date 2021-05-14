from bs4 import BeautifulSoup
import requests

file = open("quotes.txt", "w")

website = requests.get('https://quotes.toscrape.com')
soup = BeautifulSoup(website.text, 'html.parser')

quotes = soup.find_all(class_='text')
authors = soup.find_all(class_='author')

count = 0
for quote in quotes:
    file.write(quote.text + "\n")
    file.write("-" + authors[count].text)
    file.write("\n\n")
    count += 1

file.close()

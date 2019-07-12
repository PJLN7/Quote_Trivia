import requests
from bs4 import BeautifulSoup
from random import randint

url = "http://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
quotes = soup.select('.quote')

data = []

for quote in quotes:
    text = quote.find(class_="text").get_text()
    name = quote.find('small').get_text()
    link = quote.find('a')['href']
    data.append({
        "text": text,
        "name": name,
        "link": link
    })

def start_game():
    guesses = 4
    quote_idx = randint(0, len(data))
    selected_quote = data[quote_idx]
    start = input(f"{selected_quote['text']}. Who said this quote?\n")
    while guesses > 0:
        if start != selected_quote['name']:
            guesses -= 1
            start = input('Nope. Try again!\n')
        print("That's it, you won!")
        return "That's it, you won!"
    print("Sorry, you ran out of guesses...")
    return "Sorry, you ran out of guesses..."

start_game()
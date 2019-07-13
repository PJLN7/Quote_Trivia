import requests
from bs4 import BeautifulSoup
from random import choice
from time import sleep
# can delay function call with sleep(# of seconds)

data = []

def scrape_data(url):
    print('Loading data...')
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.select('.quote')

    for quote in quotes:
        text = quote.find(class_="text").get_text()
        name = quote.find('small').get_text()
        link = quote.find('a')['href']
        data.append({
            "text": text,
            "name": name,
            "link": link
        })
    print('Data loaded!')

def start_game():
    print('Starting game...')
    guesses = 4
    selected_quote = choice(data)
    start = input(f"{selected_quote['text']}. Who said this quote? {guesses} guesses remaining\n")
    while start != selected_quote['name']:
        if guesses == 1:
            print("Sorry ran out of guesses...")
            replay = input("Would you like to play again?\n")
            if replay.lower() in ['yes', 'y']:
                return start_game()
            print('Thanks for playing!')
            return 'Thanks for playing!'
        guesses -= 1
        start = input(f'Nope. Try again! {guesses} guess(es) remaining\n')
    print('That\"s it! You won!')
    

scrape_data("http://quotes.toscrape.com/")
start_game()
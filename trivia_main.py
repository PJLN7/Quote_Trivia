import requests
from bs4 import BeautifulSoup
import re
from random import choice
from csv import reader, writer

def scrape_data(url):
    # Using BeautifulSoup to scrape data from a commonly used website for scraping
    print('Fetching data...')
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.select('.quote')
    data = []

    for quote in quotes:
        unknown_chars_regex = re.compile(r"[“”]")
        text = unknown_chars_regex.sub('', quote.find(class_="text").get_text())
        name = quote.find('small').get_text()
        link = quote.find('a')['href']
        data.append({
            "text": text,
            "name": name,
            "link": link
        })
    print('Data fetched!')
    return data

def save_data_to_file(data):
    # Saving data scraped from website to a newly generated csv file
    print('Saving data...')
    with open("quotes_list.csv", "w", newline='') as file:
        csv_writer = writer(file)
        csv_writer.writerow(['text', 'name', 'link'])
        for quote in data:
            csv_writer.writerow([quote['text'], quote['name'], quote['link']])
    print('Data saved!')

def start_game():
    # Reading from CSV file and starting game
    quotes_list = []
    with open('quotes_list.csv') as file:
        csv_reader = reader(file)
        quotes_list = list(csv_reader)[1::]
    print('Starting game...')
    guesses = 4
    selected_quote = choice(quotes_list)
    start = input(
        f"{selected_quote[0]}. Who said this quote?\n{guesses} guesses remaining\n")
    while start != selected_quote[1]:
        if guesses == 1:
            print("Sorry ran out of guesses...")
            replay = input("Would you like to play again?\n")
            if replay.lower() in ['yes', 'y']:
                return start_game()
            print('Thanks for playing!')
            return 'Thanks for playing!'
        guesses -= 1
        start = input(f'Nope. Try again!\n{guesses} guess(es) remaining\n')
    print('That\"s it! You won!')

save_data_to_file(scrape_data("http://quotes.toscrape.com/"))
start_game()
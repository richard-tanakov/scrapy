import requests
from bs4 import BeautifulSoup
from time import sleep


def get_url()
    for count in range(1, 8):
        sleep(1)
        url = f"https://scrapingclub.com/exercise/list_basic/?page={count}"

        response = requests.get(url)
        soup = BeautifulSoup(response.text, "lxml")

        data = soup.find_all("div", class_="w-full rounded border")
        for i in data:

            url_card = "https://scrapingclub.com" + i.find("a").get("href")

            yield (url_card)

""" достаем из карточек товара описание """
for card_info in list_card_url:
    response = requests.get(card_info)
    soup = BeautifulSoup(response.text, "lxml")

    card = soup.find("div", class_="p-6")
    name = card.find("h3", class_="card-title").text
    price = card.find("h4", class_="my-4 card-price").text
    card_inf = card.find("p", class_="card-description").text
    #print(name + "\n" + price + "\n\n" + card_inf + "\n\n")

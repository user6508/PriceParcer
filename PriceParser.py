import requests
from bs4 import BeautifulSoup
import argparse


def itbox(url):
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(response.text, 'lxml')
    item_price = soup.find('strong', class_="stuff-price__digits").text
    item_name = soup.find('h1', class_="h1 scada").text
    item_currency = soup.find('span', class_="stuff-price__currency").text.strip()

    print(f' {item_name} -{item_price}{item_currency}')


def rozetka(url):
    pass


func_dict = {'itbox': itbox}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('shop_name')
    args = parser.parse_args()
    if args.shop_name not in func_dict:
        print('Will implemented soon :)')
        exit(1)
    print('Enter %s item link:' % args.shop_name)
    url = input()
    func_dict[args.shop_name](url)

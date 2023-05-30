import requests
import json
from urllib.parse import urlparse
import argparse
from dotenv import load_dotenv,find_dotenv
import os


def shorten_link(token, url):
    url = "https://api-ssl.bitly.com/v4/bitlinks"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    body = {
        "long_url": client_link
    }
    response = requests.post(url, headers=headers, json=body)
    response.raise_for_status()
    bitlink = response.json()["link"]
    return bitlink


def count_clicks(token,url):
    bitlink_parse = urlparse(bitlink)
    correct_bitlink = f"{bitlink_parse.netloc}{bitlink_parse.path}"
    url = f"https://api-ssl.bitly.com/v4/bitlinks/{correct_bitlink}/clicks/summary"
    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    clicks = response.json()["total_clicks"]
    return clicks


def is_bitlink(url):
    bitlink_parse = urlparse(bitlink)
    correct_bitlink = f"{bitlink_parse.netloc}{bitlink_parse.path}"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    bitlink_parse = urlparse(bitlink)
    response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{correct_bitlink}', headers=headers)
    return response.ok


def main():
    load_dotenv(find_dotenv())
    parser = argparse.ArgumentParser(
        description="Выводит битлинк или показывает сколько было переходов по битлинку"
    )
    parser.add_argument("client_link", help="Ссылка на страницу")
    args = parser.parse_args()
    token = os.environ["BITLY_TOKEN"]

    try:
        if is_bitlink(token, url):
            clicks = count_clicks(token, url)
            print("Всего кликов:", clicks)
        else:
            bitlink = shorten_link(token, url)
            print("Битлинк:", bitlink)
    except requests.exceptions.HTTPError:
        print("Invalid input")
        

if __name__ == '__main__':
    main()

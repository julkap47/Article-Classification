import requests
import trafilatura
import pandas as pd


def download_text(url):
    headers = { 'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    downloaded = response.text

    text = trafilatura.extract(downloaded)
    return text
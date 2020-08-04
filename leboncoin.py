from bs4 import BeautifulSoup
import requests

URL = 'https://www.leboncoin.fr/ventes_immobilieres/offres/'
HEADERS = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0"}

def browse(url, headers):
    """
    Scrap url
    """
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    nav = soup.find_all(name='ul')
    __import__("pdb").set_trace()

    results = nav[0].find_all(name="li")
    for r in results:
        print(r.text)

browse(URL, HEADERS)


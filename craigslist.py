from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup

URL = 'https://tokyo.craigslist.org/d/appliances/search/ppa?lang=en&cc=us'

HEADERS = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0"}


def scrap_craigslist(url, headers):
  page = requests.get(url, headers=headers)
  soup = BeautifulSoup(page.content, 'lxml')

  products = soup.find_all(class_="result-info")

  for p in products:
    date = p.find(class_="result-date").get('datetime')
    date = datetime.strptime(date, '%Y-%m-%d %H:%M')
    product_name = p.find(class_="result-title").get_text()
    product_price = float(p.find(class_="result-price").get_text()[1:])
    product_location = p.find(class_="result-hood")
    product_location = product_location.get_text() if product_location else ""

    if product_price < 2000 and 'lamp' in product_name.lower() and (datetime.today() - timedelta(weeks=8) < date):
      print(date, product_name, product_price, product_location)

if __name__ == "__main__":
  scrap_craigslist(URL, HEADERS)


import requests
from bs4 import BeautifulSoup

URL = 'https://tokyo.craigslist.org/d/appliances/search/ppa?lang=en&cc=us'

HEADERS = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0"}


def scrap(url, headers):
  page = requests.get(url, headers=headers)
  soup = BeautifulSoup(page.content, 'html.parser')

  products = soup.find_all(class_="result-info")

  for p in products:
      product_name = p.find(class_="result-title").get_text()
      product_price = p.find(class_="result-price").get_text()
      print("#" * 30)
      print(product_name, product_price)
# products[0].find(class_="result-name").get_text()
  # price = soup.find(class_="Fx4vi").get_text()

  # return(first_prod_name)
#   def convert_price(s):
#     return s[0:5]

#   converted_price = convert_price(price)

#   if converted_price < 1:
#     send_mail()
#   print(converted_price)
#   print(title.strip())
#   send_mail() # For testing, i guess...

print(scrap(URL, HEADERS))



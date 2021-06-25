from bs4 import BeautifulSoup
import requests
import re

url = 'https://stomcenter.ru/uslugi/stomatologiya-pricelist/'
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

name = soup.find_all('span')
price = soup.find_all('strong')

# for i in range(0, len(name)):
	# print(name[i].get_text())
for i in range(0, len(price)):
	 print(price[i].get_text())

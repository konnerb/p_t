import requests
from bs4 import BeautifulSoup

print('**** Running p_t... ****')

URL = input('Enter target URL : ')
print(URL)

headers_input = str(input("Enter your User-Agent : "))
headers = {"User-Agent": headers_input}
print(headers)

target_price = input("Enter target Price : ")
print(target_price)

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id="productTitle")
price = soup.find(id="productPrice")

convert_price = float(price[0:5])

if(convert_price < target_price):
    print("Price matched!")

print('**** Finished Running p_t ****')
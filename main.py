from bs4 import BeautifulSoup
import requests
url =  "https://www.film.ru/compilation/100-luchshih-filmov-xxi-veka-po-versii-zhurnala-empire"
req = requests.get(url)
src = req.text
soap = BeautifulSoup(src,'lxml')

s = soap.find_all('a',class_="film_list_link")

for k in s:
    name = k.text.strip().split()
    hrf =  'https://www.film.ru' + k.get('href')
    print(name,hrf)


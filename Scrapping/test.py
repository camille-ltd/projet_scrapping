import requests 
from bs4 import BeautifulSoup
import pandas 

url='https://www.mistergoodbeer.com/bars-pas-chers/bordeaux'
res=requests.get(url)
# if res.ok:
#     soup=BeautifulSoup(res.text,'lxml')
#     bar=soup.findAll('div',{'class': 'a'})
#     adresse=soup.findAll('div',{'class': 'subtitle'})
#     print('bar: '+ str(bar) + 'n\n' + 'adresse: ' + str(adresse))

# soup=BeautifulSoup(res.text,'lxml')
# names=soup.find_all('a', style="flex-grow:1")
# for name in names:
#     print(name.text)

# test1 = [name.string for name in names]
# print(test1)

# soup=BeautifulSoup(res.text,'lxml')
# adresses=soup.find_all('h3', class_='subtitle is-6')
# #print(adresses)

# test = [adress.string for adress in adresses]
# #print(test)


soup=BeautifulSoup(res.text,'html.parser')
prices=soup.find("div", class_="card-content").find_all("p")
#print(prices)



# test3 = [price.string.strip() for price in prices]
# print(test3)

# soup1=BeautifulSoup(prices, 'html.parser')
# print(soup1)

# for price in prices:
#     print(price.text)


# dict={"bar" : test1, 'Adresses' : test}
# print(dict)
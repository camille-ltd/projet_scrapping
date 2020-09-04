import requests 
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

url='https://www.mistergoodbeer.com/bars-pas-chers/bordeaux'
res=requests.get(url)
soup=BeautifulSoup(res.text,'lxml')


#Récupération des noms des bars
titles=soup.find_all('h2', class_="card-header-title")
for title in titles:
    name=title.find("a").text
    #print(name)

#Récupération des adresses des bars
subtitles=soup.find_all('div', class_='card-content')
for subtitle in subtitles:
    adress=subtitle.find("h3").text
    #print(adress)


#Récupération des prix en happy hour
card_contents=soup.find_all("div", class_="card-content")
for card_content in card_contents:
    price_hp=card_content.find("p").text.split()[0:7]
    #print(price_hp)

#Récupération des prix hors happy hour
card_contents=soup.find_all("div", class_="card-content")
for card_content in card_contents:
    real_price=card_content.find("p").text.split()[7:]
    #print(real_price)

#Récupération des notes sur google
url2='https://www.google.com/search?client=firefox-b-d&q=camelot+bordeaux#lrd=0xd5527c8508c16ad:0xec1b9b67da064e4e,1,,,'
res2=requests.get(url)
soup2=BeautifulSoup(res.text,'lxml')
#print(soup)

note=soup.find("div", class_="review-score-container")
print(note)

#Création d'un dataframe 
# dic={
# "Enseigne" : name,
# "Adresse" : adress, 
# "Prix en happy hour" : price_hp, 
# "Prix hors happy hour" : real_price}
# print(dic)

# df = pd.DataFrame(data=dic)
# print(df)


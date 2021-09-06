from bs4 import BeautifulSoup
import requests
import re
import numpy as np

def snapdeal(entry,entry_url="https://www.snapdeal.com/search?keyword="):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}

    entry_words=entry.split()

    entry_links=[]
    products_data=[]

    for word in entry_words:
        entry_url=entry_url+word
        entry_url=entry_url+"%20"

    # print(entry_url)
    source=requests.get(entry_url).text

    information = BeautifulSoup(source, 'lxml')
    info2=information.find_all("div",class_="product-desc-rating")

    for info in info2:

        try:
            entry_links.append(info.find("a").get('href'))
        except Exception as e:
            pass

    for link in entry_links:

        source = requests.get(link).text
        info = BeautifulSoup(source, 'lxml')

        try:
            name=info.find("h1").get('title')
        except Exception as e:
            name="Not available"

        try:
            price_inr=info.find("span",class_="payBlkBig").text
        except Exception as e:
            price_inr=""

        try:
            r=info.find("span",class_="avrg-rating").text
            temp=""
            for i in r:
                if i!="(" and i!=")":
                    temp+=i
            avg_rating=temp

        except Exception as e:
            avg_rating=""

        try:
            num_ratings=info.find("span",itemprop="ratingCount").text
        except Exception as e:
            num_ratings=""

        try:
            img_url=info.find("img",class_="cloudzoom").get("src")
            # img.append(np.array(Image.open(BytesIO(requests.get(img_url,stream=True).content))))
        except Exception as e:
            img_url=""

        products_data.append({'name':name, 'url':link, 'avg_rating':avg_rating, 'num_ratings':num_ratings, 'price_inr':price_inr, 'img_url':img_url})

    return products_data

print(snapdeal("shoes"))

import numpy as np
import requests
from bs4 import BeautifulSoup
import re

def get_imgurl(link, headers):
    response2 = requests.get(link, headers=headers)
    soup2 = BeautifulSoup(response2.content, 'html.parser')
    response2.close()
    return soup2.find('img',class_='_396cs4 _2amPTt _3qGmMb _3exPp9')['src']

def getItems(query):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}
    url_list = ['https://www.flipkart.com/search?q=']
    word_list = query.strip().split()
    for word in word_list:
        url_list.append(word)
        url_list.append('%20')
    url = "".join(url_list[:-1])
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    response.close()
    containers = soup.find_all('div', {'class': '_2kHMtA'})
    if(containers == []):
        containers = soup.find_all('div', {'class': '_4ddWXP'})

    products_data = []
    for container in containers:
        try:
            name = container.a.img['alt']
            link = 'https://www.flipkart.com' + container.a['href']
            avg_rating = float(container.find('div',class_="_3LWZlK").text) if container.find('div',class_="_3LWZlK") else 0.0
            num_ratings = 0 if (avg_rating==0) else (int(container.find('span',class_="_2_R_DZ").span.span.text.strip().replace(',','')[:-8]) if container.find('span',class_="_2_R_DZ").span else int(container.find('span',class_="_2_R_DZ").text[1:-1].replace(',','')))
            price_inr = float(container.find('div',class_="_30jeq3").text.strip().replace(',','')[1:])
            img_url = container.find('img',class_='_396cs4 _3exPp9')['src'] if container.find('img',class_='_396cs4 _3exPp9') else get_imgurl('https://www.flipkart.com'+container.find('a',class_='_1fQZEK')['href'], headers)

            products_data.append({'name':name, 'url':link, 'avg_rating':str(avg_rating), 'num_ratings':str(num_ratings), 'price_inr':str(price_inr), 'img_url':img_url})
        except:
            pass
    return products_data

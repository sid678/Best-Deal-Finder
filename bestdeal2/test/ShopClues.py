#!/usr/bin/env python
# coding: utf-8


import time
from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementClickInterceptedException



def scrape(product_name):
    if product_name != "":
        item = product_name
    else:
        item = input("Enter product name : ")
    search_query = item.replace(" ", "%20")
    url = "https://www.shopclues.com/search?q=" + search_query
    #print(url)
    
    ##### Web scrapper for infinite scrolling page #####
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=option)
    # driver = webdriver.Chrome(executable_path=r"D:\projects\Web_scrape\chromedriver.exe", options = option)
    driver.get(url)
    time.sleep(0.5)  # Allow 2 seconds for the web page to open
    scroll_pause_time = 0.8
    screen_height = driver.execute_script("return window.screen.height;")   # get the screen height of the web
    i = 1

    while True:
        # scroll one screen height each time
        driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
        i += 1
        time.sleep(scroll_pause_time)
        # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
        scroll_height = driver.execute_script("return document.body.scrollHeight;")  
        # Break the loop when the height we need to scroll to is larger than the total scroll height
        if (screen_height) * i > scroll_height:
            break 
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    found_items = []
    tags = soup.find_all(class_ = "column col3 search_blocks")
    for tag in tags:
        link = tag.a['href']
        img_link = tag.find_all(class_ = "img_section")[0].img['src']
        title = tag.find_all(class_ = "img_section")[0].img['title']
        new_price = tag.find_all(class_ = "p_price")[0].text.replace(" ", "")
        old_price = tag.find_all(class_ = "p_price")[1].text.replace(" ", "")

        # all details written compiled into a dictionary with the following tags and appended to found_items list
        found_items.append({
            "url" : link,
            "img_url" : img_link,
            "name" : title,
            "price_inr" : new_price[1:],
            "avg_rating" : "0.0",
            "num_ratings" : "0"
            # "item_old_price" : old_price
        })
    return found_items


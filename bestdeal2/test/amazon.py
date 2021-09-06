# 1
import os
import selenium
from selenium import webdriver
import time
from PIL import Image
import io
import requests
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementClickInterceptedException

def scrape(query):
    # 2
    opts = webdriver.ChromeOptions()
    opts.headless =True
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=opts)

    # 3
    query.replace(' ','+')
    search_url="https://www.amazon.in/s?k={q}"
    driver.get(search_url.format(q=query))

    #4
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)#sleep_between_interactions

    #5
    allitems = driver.find_elements_by_class_name("sg-col-inner")
    items_list=[]
    for item in allitems:
        try:
            imglink = item.find_element_by_class_name("s-image").get_attribute('src')
            name_utils = item.find_elements_by_class_name("a-size-base-plus")
            name = name_utils[0].text + name_utils[1].text
            # print(name)
            rating_utils = item.find_element_by_class_name("a-icon-alt").get_attribute('innerHTML')
            # print(rating_utils)
            num_ratings = item.find_element_by_class_name("a-icon-alt").find_element_by_xpath("../../../../../span[2]").get_attribute('aria-label')
            # print(num_ratings)
            price = item.find_element_by_class_name("a-price-whole").text
            # print(price)
            url = name_utils[1].find_element_by_xpath("..").get_attribute("href")
            # print(url)
            items_list.append({
                "name" : name,
                "url" : url,
                "avg_rating" : rating_utils[:3],
                "num_ratings" : num_ratings,
                "price_inr": price,
                "img_url" : imglink,
            })
        except:
            print("Not suitable product")

    print(query)
    print(len(items_list))
    # print(items_list[0])
    return items_list
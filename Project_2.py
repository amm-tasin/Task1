from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time


url = "https://books.toscrape.com"

driver = webdriver.Chrome()
driver.get(url)

title_data = []
price_data = []
stock_data = []
rate_data = []

while True :
    title = driver.find_elements(By.CSS_SELECTOR, "img.thumbnail") 
    for i in title:
        title_data.append(i.get_attribute("alt"))


    price = driver.find_elements(By.CSS_SELECTOR, "p.price_color")
    for i in price:
        price_data.append(i.text)

    stock = driver.find_elements(By.CSS_SELECTOR,"p.instock")
    for i in stock:
        stock_data.append(i.text)

    rate = driver.find_elements(By.CSS_SELECTOR,"p.star-rating")
    for i in rate :
        m = i.get_attribute("class")
        sp = m.split(" ")[1]
        rate_data.append(sp)
    


    try:
        nxt = driver.find_element(By.CSS_SELECTOR,"li.next a")
        print(nxt.get_attribute("href"))
        nxt.click()
    except:
        break


data = {
    "Book" : title_data,
    "Price" : price_data,
    "rating": rate_data,
    "Stock": stock_data
}

df = pd.DataFrame(data)
df.to_csv("AllBooks.csv", index=False)

time.sleep(1)
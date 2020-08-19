from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://french.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText=3d+printer&viewtype=&tab=")
time.sleep(2)
driver.execute_script("window.scrollTo(0,document.body.scrollHeigh)")
time.sleep(2)
elem = driver.find_elements_by_css_selector("p")
for elems in elem:
    driver.find_elements_by_class_name("elements-title-normal__content large")
    print(elems.text)


driver.close()
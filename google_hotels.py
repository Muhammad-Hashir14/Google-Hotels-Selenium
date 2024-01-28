import time
from typing import Dict, Any

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.binary_location = r"C:\Program Files (x86)\chrome-win64\chrome.exe"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=chrome_options)

url = "https://www.google.com/travel/search?q=google%20hotels&g2lb=2502548%2C2503771%2C2503781%2C2504510%2C4258168%2C4284970%2C4291517%2C4814050%2C4874190%2C4893075%2C4965990%2C10208620%2C10209059%2C72248047%2C72248048%2C72277293%2C72302247%2C72317059%2C72406588%2C72421566%2C72427842%2C72430562%2C72440517%2C72448541%2C72458060%2C72458707%2C72462234%2C72469155%2C72470440%2C72470899%2C72472051%2C72473738%2C72473841%2C72479990%2C72480010%2C72484736%2C72485656%2C72486593&hl=en-PK&gl=pk&ssta=1&ts=CAESCAoCCAMKAggDGhwSGhIUCgcI6A8QARgdEgcI6A8QARgeGAEyAhAAKgcKBToDUEtS&qs=CAE4BkIJCXZfiL9NtowfQgkJDGxpNeON27lCCQlJm7afbrM9Ew&ap=aAE&ictx=1&ved=0CAAQ5JsGahcKEwjI9-C3mv6DAxUAAAAAHQAAAAAQCQ"
driver.get(url)
driver.maximize_window()

data = {
}
wait_time = 20
for i in range(1,195):
    anchors = driver.find_elements(By.XPATH, "//*[@class='PVOOXe']")
    for anchor in anchors:
        anchor = WebDriverWait(driver, wait_time).until(
            EC.element_to_be_clickable(anchor)
        )
        anchor.click()
        time.sleep(2)
        about = WebDriverWait(driver, wait_time).until(
            EC.element_to_be_clickable((By.XPATH, "(//*[@class='mrslJ ZjAUM  nkLxl rZGTQc']//span)[5]"))
        )
        about.click()
        time.sleep(2)
        try:
            name_element = WebDriverWait(driver, wait_time).until(
                EC.visibility_of_element_located((By.XPATH, "//*[@class='FNkAEc o4k8l']"))
            )
            name = name_element.text
        except Exception as e:
            print("Error extracting name:", e)
            name = "Default Name"

        try:
            info_element = WebDriverWait(driver, wait_time).until(
                EC.visibility_of_element_located((By.XPATH, "//*[@class='G8T82']"))
            )
            info = info_element.text
        except Exception as e:
            print("Error extracting info:", e)
            info = "Default Info"

        data[name] = info
        print(data)
        time.sleep(2)
        driver.back()
        time.sleep(1)
        driver.back()
    time.sleep(4)

    next_button = WebDriverWait(driver, wait_time).until(
        EC.element_to_be_clickable((By.XPATH,"//*[@class='eGUU7b']//span")))
    next_button.click()
    time.sleep(5)
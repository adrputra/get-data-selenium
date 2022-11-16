from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import json
import requests
import pickle

PATH = "../chromedriver.exe"
options = webdriver.ChromeOptions()
options.headless = False
driver = webdriver.Chrome(executable_path=PATH, options=options)


def loginIg():
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "input[name='username']"))).send_keys("getData123_")
    driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys(
        "Akunbersama123;")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit'] div").click()
    # pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
    driver.find_element_by_xpath(
        f"//button[@class='_acan _acap _acas']").click()


def searchIG(tag, n):
    driver.get("https://www.instagram.com/explore/tags/%s/" % tag)
    driver.implicitly_wait(5)
    links = []
    try:
        driver.find_element_by_xpath(
            f"//button[@class='_acan _acap _acas']").click()
        loginIg()
        driver.implicitly_wait(10)

        for i in range(n):
            for j in range(3):
                id = driver.find_element_by_xpath(
                    f"//article//div[@class='_ac7v _aang'][{i+1}]//div[@class='_aabd _aa8k _aanf'][{j+1}]//a").get_attribute('href')
                # print(id.split('/')[4])
                links.append(id.split('/')[4])
                driver.execute_script("window.scrollBy(0, 500)")
                time.sleep(2)
    except NoSuchElementException:
        print("no data")

    print(links)
    # getDataPostIg(breakList(links))
    getDataPostIg(links)


def breakList(my_list):
    n = 50
    final = [my_list[i * n:(i + 1) * n]
             for i in range((len(my_list) + n - 1) // n)]
    return final


def getDataPostIg(links):
    data = []
    for id in links:
        url = "https://instagram203.p.rapidapi.com/postinfo/%s" % id
        headers = {
            "X-RapidAPI-Key": "a55e034d55mshbc70cc52c774ecfp169a4ejsn4ccf9fef4b1c",
            "X-RapidAPI-Host": "instagram203.p.rapidapi.com"
        }
        response = requests.request("GET", url, headers=headers)
        result = response.json()
        # result = response.text
        # print(result["data"]["like_count"])
        caption = result["data"]["caption"]["text"]
        likes = result["data"]["like_count"]
        views = "" #sebenarnya untuk viewnya ada view_count tapi gua mau kondisiin error ndra coba nanti kalo bisa gua tes lagi
        data.append([caption, likes, views])
    print(data)


# getDataPostIg("Ck7xOZsO5xi")
searchIG("anggur", 2)

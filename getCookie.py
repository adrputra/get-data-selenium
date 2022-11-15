from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import os
import urllib.request
import time
import pickle
import pyautogui as p

PATH = "chromedriver.exe"
options = webdriver.ChromeOptions()
options.headless = False
driver = webdriver.Chrome(executable_path=PATH, options=options)
dirPath = ""
tiktokCookiePath = "tiktokCookie.txt"

def getCookie():
    driver.get("https://www.tiktok.com/")
    # login = driver.find_element_by_xpath("//button[@data-e2e='top-login-button']")
    # login.click()
    # time.sleep(2)
    # qr = driver.find_element_by_xpath("//a[@href='/login/qrcode']")
    # qr.click()
    time.sleep(60)
    save_cookie(driver,tiktokCookiePath)
    print("COokie saved")
    driver.implicitly_wait(2)

def save_cookie(driver, path):
    with open(path, 'wb') as filehandler:
        pickle.dump(driver.get_cookies(), filehandler)

getCookie()
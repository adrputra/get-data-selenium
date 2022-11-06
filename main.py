from selenium import webdriver
import os
import urllib.request
from datetime import datetime
import youtubeAPI
# import json

PATH = "chromedriver.exe"
options = webdriver.ChromeOptions()
options.headless = False
driver = webdriver.Chrome(executable_path=PATH, options=options)    

def Youtube(tag,n):
    driver.get("https://www.youtube.com/hashtag/%s"%tag)
    links = []

    for i in range(n):
        for j in range(2):
            # links.append(driver.find_element_by_xpath(f"//div[@id='primary']//ytd-rich-grid-row[{i+1}]//ytd-rich-item-renderer[{j+1}]//a[@id='video-title-link']").get_attribute('href'))
            link = driver.find_element_by_xpath(f"//div[@id='primary']//ytd-rich-grid-row[{i+1}]//ytd-rich-item-renderer[{j+1}]//a[@id='video-title-link']").get_attribute('href')
            links.append(link.split('=')[1])
    print(links)
    # getLikesYoutube(links)
    getLikesYoutubeAPI(links)

def getLikesYoutube(links):
    data = []
    for link in links:
        print('Opening', link)
        driver.get(link)
        driver.implicitly_wait(10)
        try:
            title = driver.find_element_by_xpath("//ytd-watch-metadata//h1").text
            likes = driver.find_element_by_xpath("//ytd-segmented-like-dislike-button-renderer//span[@role='text']").text
            views = driver.find_element_by_xpath("//div[@id='info-container']//span[1]").text
            data.append([link,title,likes,views])
        except NoSuchElementException:
            getLikesYoutube(links)
    print(data)
    writeToFile(data)

def getLikesYoutubeAPI(videoID):
    # resp = json.load(youtubeAPI.main(videoID))
    resp = youtubeAPI.main(videoID)
    data = []
    items = resp['items']
    for item in items:
        data.append([item['id'], item['snippet']['title'], item['statistics']['viewCount'], item['statistics']['likeCount'], item['statistics']['commentCount']])
    writeToFile(data)

def writeToFile(data):
    dt = datetime.now()
    ts = datetime.timestamp(dt)
    result = open("Youtube_Get_Data_Result_"+str(ts)+".txt","a+", encoding='utf-8')
    for val in data:
        result.writelines(f"{val[0]};{val[1]};{val[2]};{val[3]};{val[4]};\n")

Youtube("realmadrid",2)
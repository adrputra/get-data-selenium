from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import os
import urllib.request
from datetime import datetime
import youtubeAPI
import time
# import json

PATH = "chromedriver.exe"
options = webdriver.ChromeOptions()
options.headless = False
driver = webdriver.Chrome(executable_path=PATH, options=options)

def Youtube(tag,n):
    driver.get("https://www.youtube.com/hashtag/%s"%tag)
    links = []
    try:
        for i in range(n):
            for j in range(2):
                # links.append(driver.find_element_by_xpath(f"//div[@id='primary']//ytd-rich-grid-row[{i+1}]//ytd-rich-item-renderer[{j+1}]//a[@id='video-title-link']").get_attribute('href'))
                link = driver.find_element_by_xpath(f"//div[@id='primary']//ytd-rich-grid-row[{i+1}]//ytd-rich-item-renderer[{j+1}]//a[@id='video-title-link']").get_attribute('href')
                print(link)
                if "shorts" in link:
                    continue
                else:
                    links.append(link.split('=')[1])
                    driver.execute_script("window.scrollBy(0, 500)")
                    time.sleep(2)
    except NoSuchElementException:
            getLikesYoutubeAPI(links)
        
    print(links)
    # getLikesYoutube(links)
    getLikesYoutubeAPI(breakList(links))

def breakList(my_list):
    n=50
    final = [my_list[i * n:(i + 1) * n] for i in range((len(my_list) + n - 1) // n )]
    return final

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
    for i in range(len(videoID)):
        resp = youtubeAPI.main(videoID[i])
        data = []
        items = resp['items']
        dt = datetime.now().strftime("%Y%m%d")
        rawData = open("Raw_Data_"+dt+"_"+str(i)+".txt","a+", encoding='utf-8')
        rawData.writelines(str(items))
        for item in items:
            try:
                vid = item['id']
                channel = item['snippet']['channelTitle']
                title = item['snippet']['title']
                viewCount = item['statistics']['viewCount']
                if "likeCount" in item['statistics']:
                    likeCount = item['statistics']['likeCount']
                else:
                    likeCount = 0
                commentCount = item['statistics']['commentCount']
                data.append([vid,title,viewCount,likeCount,commentCount,hastag,channel])
                # data.append([item['id'], item['snippet']['title'], item['statistsics']['viewCount'], item['statistics']['likeCount'], item['statistics']['commentCount']])
            except KeyError:
                continue
        # print(data)
        writeToFile(data,videoID[i])

def writeToFile(data,videoID):
    dt = datetime.now()
    ts = datetime.timestamp(dt)
    result = open("Youtube_Get_Data_Result_"+".txt","a+", encoding='utf-8')
    for val in data:
        result.writelines(f"{val[0]};{val[1]};{val[2]};{val[3]};{val[4]};{val[5]};\n")
    saveVideoID = open("RawVideoID.txt","a+",encoding='utf-8')
    for val in videoID:
        saveVideoID.writelines(f"{val};")

# Youtube("indonesia",100)
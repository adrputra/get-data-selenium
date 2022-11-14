from selenium import webdriver
PATH = "chromedriver.exe"
options = webdriver.ChromeOptions()
options.headless = False
driver = webdriver.Chrome(executable_path=PATH, options=options).maximize_window()
driver.get(f"https://www.tiktok.com/search/video?q=%23indonesia")

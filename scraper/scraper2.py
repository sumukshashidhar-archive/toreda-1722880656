from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time
# from fake_useragent import UserAgent

# ua = UserAgent()
UserAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument(f'user-agent={UserAgent}')
options.add_argument('--headless')



## this path may depend on what you're using and where
driver = webdriver.Chrome('/usr/local/bin/chromedriver', options = options)
#driver = webdriver.Chrome(ChromeDriverManager().install(), options=options) #part of a possible fix


## modifying the query here
url = 'https://www.moneyworks4me.com/best-index/nse-stocks/top-nse500-companies-list/'


#//*[@id="table-data"]

driver.get(url)
# print(driver.page_source)

# time.sleep(5)
print('Page loaded')

# elementname = driver.find_element(By.XPATH, '/html/body/div[7]/div[1]/section[1]/div/div/div/div/div[1]/div[2]/div/div/nav/div/div/a[1]/div/p[2]')

time.sleep(5)
# element = driver.find_elements_by_xpath('/html/body/div[7]/div[1]/section[1]/div/div/div/div/div[1]/div[2]/div/div/nav/div/div/a[1]/div/p[2]')
element2 = driver.find_element_by_xpath('//*[@id="table-data"]')
# print(element2.text)

f1 = open('test.txt', 'w')
f1.write(element2.text)
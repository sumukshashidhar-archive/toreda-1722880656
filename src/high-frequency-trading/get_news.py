from bs4 import BeautifulSoup
from selenium import webdriver
import urllib.request
from sentiment import sentiment_analysis
import re


xpath = '//*[@id="Col1-0-Sustainability-Proxy"]/section/div[2]/div[2]/div/div/div/div[1]/div'
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome('/usr/lib/chromium/chromedriver', options = options)

driver.get('https://in.finance.yahoo.com/quote/WIPRO.BO/sustainability?p=WIPRO.BO')

item = driver.find_element_by_xpath(xpath)
print(item)







def sustainability():
    slink = 'https://in.finance.yahoo.com/quote/WIPRO.BO/sustainability?p=WIPRO.BO'
    h = urllib.request.urlopen(slink)
    soup = BeautifulSoup(h, 'lxml')
    print(soup.findAll('<div class="D(ib) Fz(36px) Fw(500)" data-reactid'))


sustainability()
from selenium import webdriver
from time import sleep
import  requests
from selenium.webdriver.support.select import Select
#推荐结果
driver = webdriver.Chrome()
driver.get('https://test.xliane.com/html2/webapp/fastIssue/index.html#/fastProgress/index')
driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[2]/input').send_keys('110224199201305248')
sleep(1)
driver.find_element_by_xpath('//p[@class="com"]').click()
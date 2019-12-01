from selenium import webdriver
from time import sleep
import  requests
from selenium.webdriver.support.select import Select
#推荐结果
driver = webdriver.Chrome()
driver.get('https://test.xliane.com/html3/webapp/fastIssue/index.html#/customerProgress/index')
driver.find_element_by_xpath('//*[@id="app"]/div/ul/li[1]/div/div[2]/input').send_keys('110224199201305248')
sleep(1)
driver.find_element_by_xpath('//*[@id="app"]/div/ul/li[2]/div/div[2]/input').send_keys('13262576101')
driver.find_element_by_xpath('//*[@id="app"]/div/ul/li[3]/div/div[3]/button').click()
sleep(2)
txt=driver.find_element_by_xpath('//*[@id="app"]/div/ul/div')
driver.find_element_by_xpath('//*[@id="app"]/div/ul/li[3]/div/div[2]/input').send_keys(txt.text)
sleep(1)
driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/p').click()
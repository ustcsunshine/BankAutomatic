from selenium import webdriver
from time import sleep
import  requests
#推荐结果
driver = webdriver.Chrome()
driver.get('https://test.xliane.com/application/cardapp/twobar/UserIndex/view')#打开网址https://test.xliane.com/application/cardapp/twobar/UserIndex/view
driver.find_element_by_xpath('//input[@placeholder="请输入您的11位手机号码"]').send_keys('12000000000')
sleep(2)
driver.find_element_by_xpath('//div[@class="btn blue"]').click()#获取验证码
sleep(3)
text=driver.find_element_by_xpath('//div[@class="container"]/div[2]').text
print(text)
sleep(2)
driver.find_element_by_xpath('//input[@type="text"]').send_keys(text)
sleep(2)
driver.find_element_by_xpath('//button[@class="confirm"]').click()
sleep(2)
driver.find_element_by_xpath('//a[@class="confirm"]').click()
sleep(1)
driver.find_element_by_xpath('//div[@class="confirm"]').click()
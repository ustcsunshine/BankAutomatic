from selenium import webdriver
from time import sleep
import  requests
from selenium.webdriver.support.select import Select
#推荐结果
driver = webdriver.Chrome()
driver.get('https://test.xliane.com/html2/webapp/fastIssue/index.html#/recommendResult/index')#打开网址https://test.xliane.com/application/cardapp/twobar/UserIndex/view
driver.find_element_by_xpath('//input[@placeholder="请输入您的11位手机号码"]').send_keys('12000000000')#手机号码
sleep(1)
driver.find_element_by_xpath('//*[@id="app"]/div/ul/li[2]/div/div[3]/div').click()#点击获取验证码
sleep(2)
code=driver.find_element_by_xpath('//*[@id="app"]/div/ul/li[2]/div/div[3]/div')
driver.find_element_by_xpath('//*[@id="app"]/div/ul/li[2]/div/div[2]/input').send_keys(code.text)
driver.find_element_by_xpath('//button[@class="confirm"]').click()#点击下一步
sleep(2)
'''
def is_exist_element(elem):
    s=driver.find_element_by_xpath('//a[@class="confirm"]')
    if len(s)==0:
        print('不存在元素%' % elem)
        return False
    if len(s) == 1:
        return True
    else:
        print("存在%s个元素分别是%s" %, (len(s), elem))
        return False
'''

driver.find_element_by_xpath('//div[@class="confirm"]').click()
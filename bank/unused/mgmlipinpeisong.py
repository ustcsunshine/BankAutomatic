from selenium import webdriver
from time import sleep
import  requests
from selenium.webdriver.support.select import Select
#推荐结果
driver = webdriver.Chrome()
driver.get('https://test.xliane.com/html2/webapp/fastIssue/index.html?bz1=0#/giftDistribute/index')#打开网址https://test.xliane.com/application/cardapp/twobar/UserIndex/view
driver.find_element_by_xpath('//input[@placeholder="请输入您的11位手机号码"]').send_keys('13262576101')#手机号码
sleep(1)
driver.find_element_by_xpath('//div[@id="smscode"]').click()#点击获取验证码
sleep(2)

driver.find_element_by_xpath('//p[@class="com"]').click()#点击下一步
sleep(2)
'''
driver.find_element_by_xpath('//input[@placeholder="请输入获奖人姓名"]').send_keys('二二二')
driver.find_element_by_xpath('//input[@placeholder="请输入身份证号码"]').send_keys('')
driver.find_element_by_xpath('//input[@placeholder="请输入邮编"]').send_keys('1001')
driver.find_element_by_xpath('//p[@class="des"]').send_keys('上海市浦东新区来安路500号')
'''

driver.find_element_by_xpath('//p[@class="com"]').click()
sleep(2)
txt=driver.find_element_by_xpath('/html/body/div[6]/span')
if txt.text =='提交成功':
    print(txt.text)

else:
    print('没有提示')







driver.find_element_by_xpath('//a[@class="confirm"]').click()
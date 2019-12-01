from selenium import webdriver
from time import sleep
import  requests
from selenium.webdriver.support.select import Select
#推荐结果
driver = webdriver.Chrome()
driver.get('https://test.xliane.com/html2/webapp/fastIssue/index.html#/tplus0/index')#打开网址https://test.xliane.com/application/cardapp/twobar/UserIndex/view
driver.find_element_by_xpath('//input[@placeholder="请输入合作方代码"]').send_keys('1002')#输入合作方代码
sleep(1)
driver.find_element_by_xpath('//input[@placeholder="请输入您的11位手机号码"]').send_keys('13262576101')#手机号码

sleep(1)
driver.find_element_by_xpath('//div[@id="smscode"]').click()#点击获取验证码
sleep(2)
driver.find_element_by_xpath('//p[@class="com"]').click()#点击下一步
sleep(2)
table = driver.find_element_by_xpath('//table[@id="tb"]')#id定位获取整个表格对象
trlist= driver.find_elements_by_tag_name('tr')#通过标签获取表格中的所有行
print(len(trlist))
for row in trlist:
    #遍历行对象，获取每一行中所有列对象
    tdlist = row.find_elements_by_tag_name('td')
    for col in trlist:
        print(col.text + '\t', end='')
    print('\n')


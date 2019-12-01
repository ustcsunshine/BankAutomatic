from selenium import webdriver
from time import sleep
import  requests
from selenium.webdriver.support.select import Select
#推荐结果
driver = webdriver.Chrome()
driver.get('https://test.xliane.com/html2/webapp/fastIssue/index.html#/mgm/index')#打开网址https://test.xliane.com/application/cardapp/twobar/UserIndex/view
driver.find_element_by_xpath('//input[@placeholder="请输入手机号码"]').send_keys('13262576101')#推广人手机号码
sleep(1)
driver.find_element_by_xpath('//input[@placeholder="请输入姓名"]').send_keys('窦路路')#姓名
sleep(1)
driver.find_element_by_xpath('//input[@placeholder="请输入合作方代码"]').send_keys('1001')#合作方代码
sleep(1)
driver.find_element_by_xpath('//div[@id="smscode"]').click()#点击获取验证码
sleep(2)
driver.find_element_by_xpath('//p[@class="com"]').click()#点击下一步
sleep(2)
selector = driver.find_element_by_id("cardType")#选中下拉框
selector.find_element_by_xpath("//option[@value='110']").click()#选中淘宝金卡
sleep(1)
driver.find_element_by_xpath('//*[@id="app"]/div/ul/li[1]/div/div[3]/div/label').click()#切换到选择卡种
sleep(2)
driver.find_element_by_xpath('//*[@id="app"]/div/ul/li[1]/div/div[4]/div/label').click()#切换到排除卡种
#selector.find_element_by_xpath("//option[@value='72']").click()
driver.find_element_by_xpath("//p[@class='com']").click()#点击确定
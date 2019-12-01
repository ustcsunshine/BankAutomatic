from selenium import webdriver
from time import sleep
import  requests
#推荐结果
driver = webdriver.Chrome()
driver.get('https://test.xliane.com/application/api/myhtml/html_webapp_fastIssue_index-customerRecommend_index')#打开网址https://test.xliane.com/application/cardapp/twobar/UserIndex/view
driver.find_element_by_xpath('//input[@placeholder="请输入您的姓名"]').send_keys('李孝雪')
sleep(2)
driver.find_element_by_xpath('//input[@placeholder="推荐人获奖短信接收号码"]').send_keys('17621523734')#手机号
sleep(1)

driver.find_element_by_xpath('//div[@id="smscode"]').click()
sleep(2)
driver.find_element_by_xpath('//div[@class="reviseBtn"]/p').click()
sleep(1)
message=driver.find_element_by_xpath('//p[@id="copyright"]').text
print(message)

try:
    assert message==u'©本服务由兴业银行信用卡中心提供 v3.6.5'
    print('test pass')
except Exception as e:
    print('test fail',format(e))


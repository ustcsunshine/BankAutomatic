from selenium import webdriver
from time import sleep
import  requests
from selenium.webdriver.support.select import Select
#推荐结果
driver = webdriver.Chrome()
driver.get('https://test.xliane.com/html2/webapp/entrance-con/home.html?id=1cdced2a92f841c38792060bbf516c60')#打开四宫格
sleep(1)

'''
driver.find_element_by_xpath('/html/body/div[1]/ul/li[2]/span').click()#切换到健康活力
ul=driver.find_element_by_xpath('//ul[@class="kind-list"]')
lis=ul.find_element_by_xpath('li')
f=len(lis)
print(f)
sleep(2)
num=driver.find_elements_by_xpath('//div[@class="header"]//span')
if len(num)==6:
    print("6个按钮")
    for i in num:
        print(i.text())
else:
    print('获取不正常')
sleep(1)
driver.find_element_by_xpath('/html/body/div[1]/ul/li[3]/span').click()#低碳环保
driver.find_element_by_xpath('/html/body/div[1]/ul/li[4]/span').click()#尊贵身份
driver.find_element_by_xpath('/html/body/div[1]/ul/li[5]/span').click()#星座时尚
driver.find_element_by_xpath('/html/body/div[1]/ul/li[6]/span').click()#推荐有礼
'''

driver.find_element_by_xpath('/html/body/div[3]/ul/li[1]/div[3]/div[1]/span').click()  # 点击权益详情

sleep(2)
dig_alert = driver.switch_to.alert
sleep(1)
print(dig_alert)
dig_alert.accept()
sleep(1)

driver.find_element_by_xpath('/html/body/div[3]/ul/li[1]/div[3]/div[2]/span').click()#点击立即申请





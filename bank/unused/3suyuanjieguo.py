from time import sleep

from selenium import webdriver

# 推荐结果
driver = webdriver.Chrome()
driver.get(
    'https://test.xliane.com/html2/webapp/fastIssue/index.html#/recommendResult/index')  # 打开网址https://test.xliane.com/application/cardapp/twobar/UserIndex/view
driver.find_element_by_xpath('//input[@placeholder="请输入您的11位手机号码"]').send_keys('12000000000')  # 手机号码
sleep(1)
driver.find_element_by_xpath('//*[@id="app"]/div/ul/li[2]/div/div[3]/div').click()  # 点击获取验证码
sleep(2)
code = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]')
print(code.text)
driver.find_element_by_xpath('//*[@id="app"]/div/ul/li[2]/div/div[2]/input').send_keys(code.text)
driver.find_element_by_xpath('//button[@class="confirm"]').click()  # 点击下一步
sleep(2)
driver.find_element_by_xpath('//a[@class="confirm"]').click()

from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import  requests
#推荐结果
url='https://test.xliane.com/application/api/myhtml/html_webapp_fastIssue_index-clerkRecommend_index'
def get_track(distance):

	track = []
	current = 0
	mid = distance * 3 / 4
	t = 0.2
	v = 0
	while current < distance:
		if current < mid:
			a = 2
		else:
			a = -3
		v0 = v
		v = v0 + a * t
		move = v0 * t + 1 / 2 * a * t * t
		current += move
		track.append(round(move))
	return track

def main():
    driver = webdriver.Chrome()
    driver.set_window_position(900,10)
    driver.get(url)

    sleep(1)
    #输入用户名和密码
    driver.find_element_by_xpath('//input[@placeholder="请输入手机号码,推广代码,或人力资源ID"]').send_keys('17621523736')
    sleep(2)
    driver.find_element_by_xpath('//input[@placeholder="请输入姓名"]').send_keys('李孝雪')  # 手机号
    sleep(2)

    driver.find_element_by_xpath("//p[@class='']").click()
    sleep(2)
    element = WebDriverWait(driver, 5, 0.5).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='img_arrow']")))
    element.click()
    sleep(5)
    flag = 0
    distance =195
    offset = 5
    times = 0
    while 1:
        action=ActionChains(driver)
        action.click_and_hold(button).perform()
        action.reset_actions()
        print(distance)
        track = get_track(distance)
        for i in track:
            action.move_by_offset(xoffset=0,yoffset=0).perform()
            action.reset_actions()
        sleep(1)
        action.release().perform()
        sleep(5)
        try:
            alert = driver.find_element_by_xpath('//*[@id="imgCode"]/div/div[1]/span[1]').text
        except Exception as e:
            print
            'get alert error: %s' % e
            alert = ''
        if alert:
            print
            u'滑块位移需要调整: %s' % alert
            distance -= offset
            times += 1
            sleep(5)
        else:
            print('滑块验证通过')

            flag = 1
            # 验证成功后跳回最外层页面
            break

        sleep(2)
        driver.quit()
        print
        "finish~~"
        return flag


    #










mobileEmulation = {'deviceName': 'Apple iPhone X'}
options = webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation', mobileEmulation)
driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)

#driver = webdriver.Chrome()
driver.get('https://test.xliane.com/application/api/myhtml/html_webapp_fastIssue_index-clerkRecommend_index')#打开网址https://test.xliane.com/application/cardapp/twobar/UserIndex/view
driver.find_element_by_xpath('//input[@placeholder="请输入手机号码,推广代码,或人力资源ID"]').send_keys('17621523736')
sleep(2)
driver.find_element_by_xpath('//input[@placeholder="请输入姓名"]').send_keys('李孝雪')#手机号
sleep(2)

driver.find_element_by_xpath("//p[@class='']").click()
sleep(2)
button=driver.find_element_by_xpath('//div[@class="img_arrow"]')
action =ActionChains(driver)
action.click_and_hold(button).perform()
action.reset_actions()
action.move_by_offset(180,0).perform()



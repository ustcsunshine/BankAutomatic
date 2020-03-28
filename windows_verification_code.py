import unittest
import cv2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime
from datetime import timedelta
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base64 import b64decode
from PIL import Image
from time import sleep
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# 针对chrome浏览器
options = webdriver.ChromeOptions()

# options.add_argument('--user-agent=Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3')
options.add_experimental_option('w3c', False)
options.add_argument('--user-agent=iphone')
options.add_argument("--auto-open-devtools-for-tabs")
# 自己随便定义一个chrome默认会话缓存路径
options.add_argument(r"--user-data-dir=/Users/jingjing.li/Downloads")

driver = webdriver.Chrome(executable_path='chromedriver.exe', options=options)


class Login(unittest.TestCase):
    def setUp(self):
        driver.maximize_window()
        driver.get("https://test.xliane.com/html2/webapp/fastIssue/index.html#/clerkRecommend/index")

    def test_search_in_python_org(self):
        login_form1 = driver.find_element_by_xpath('//*[@id="app"]/div/ul/li[1]/div/div[2]/input')
        login_form1.send_keys(17621523736)
        login_form2 = driver.find_element_by_xpath('//*[@id="app"]/div/ul/li[2]/div/div[2]/input')
        login_form2.send_keys("李孝雪")
        # nextStep=driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/p')
        nextStep = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/\div[1]/p')))

        # 通过js执行点击事件
        js = "oElements  = document.getElementsByTagName('p');for(var i=0;i<oElements.length;i++){if(oElements[i].className == 'com'){oElements[i].click();}}"
        driver.execute_script(js)

        try:
            slider = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="imgCode"]/div/div[3]/div[2]')))
        finally:
            pass

        bgImage = getImage(driver, '//*[@id="imgCode"]/div/div[2]/img[1]', "yanzheng.jpg")
        sliderImage = getImage(driver, '//*[@id="imgCode"]/div/div[2]/img[2]', "huakuai.jpg")

        '''
        实例化一个action对象
        计算滑块滑动距离
        '''
        px = get_x_y("jingjing.li/Downloads/huakuai.jpg", "jingjing.li/Downloads/yanzheng.jpg", "jingjing.li/Downloads/\result.jpg")
        action = TouchActions(driver)
        action.flick_element(slider, px, 0, 50).perform()
        pass

    def tearDown(self):
        pass


# 获取base64编码图片对象
def getImage(driver, xPath, name):
    imageElement = driver.find_element_by_xpath(xPath)
    imgStr = imageElement.get_attribute('src')
    # imgStr = imgStr.replace("%0A", '\n')
    imgStr = imgStr.split(",")[-1]
    img_data = b64decode(imgStr)  # b64decode 解码
    with open('./' + name, 'wb') as fout:
        fout.write(img_data)
        fout.close()
    image = Image.open('./' + name)
    return image


def get_x_y(gaps_picture, big_picture, result_path="", is_show=False):
    """
    输入缺口图片和匹配的大图、图片的类型，返回缺口图片在大图的起点位置（x,y)
    :param gaps_picture: 缺口图片路径
    :param big_picture: 大图路径
    :param i
    s_show: 默认不展示图片
    :return:
    """
    # 1, 数据输入：对图片进行预处理，灰度化分析
    gaps_temp = 'gaps_img_gray_temp.jpg'  # 用于可视化
    big_temp = 'big_img_rgb_temp.jpg'
    gaps_img_gray = cv2.imread(gaps_picture, 0)  # 0表示返回灰度图
    cv2.imwrite(gaps_temp, gaps_img_gray)  # 保存缺口图的灰度图
    w, h = gaps_img_gray.shape[::-1]
    big_img_rgb = cv2.imread(big_picture)
    cv2.imwrite(big_temp, big_img_rgb)  # 相当于big_img的拷贝
    big_img_gray = cv2.imread(big_picture, 0)

    # 2, 数据处理：图片识别匹配
    match_result = cv2.matchTemplate(gaps_img_gray, big_img_gray, cv2.TM_CCOEFF_NORMED)  # 归一化相关系数匹配
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(match_result)  # 获取最佳匹配结果的坐标
    y_goal, x_goal = max_loc

    # 3, 数据输出：返回识别的结果，缺口图在大图的位置
    if is_show is True:
        show_result_img = cv2.imread(big_temp)
        cv2.rectangle(show_result_img, (y_goal, x_goal), (y_goal + w, x_goal + h), (0, 0, 255), 2)
        print(y_goal, x_goal, y_goal + w, x_goal + h)
        cv2.destroyAllWindows()
        cv2.imshow('Show_result', show_result_img)
        if result_path:
            # 保存结果

            cv2.imwrite(result_path, show_result_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return y_goal


if __name__ == "__main__":
    unittest.main()



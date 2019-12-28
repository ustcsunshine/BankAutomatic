from selenium import webdriver
import os,sys
from time import sleep

def insert_img(driver,file_name):

    base_dir = os.path.dirname(os.path.dirname(__file__))
    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\', '/')
    base = base_dir.split('test_case')[0]
    file_path = base + "report/image/"+file_name
    driver.get_screenshot_as_file(file_path)


if __name__ == '__main__':

    driver = webdriver.Chrome()
    driver.get("https://test.xliane.com/html2/webapp/fastIssue/index.html#/customerRecommend/index")
    sleep(2)
    insert_img(driver, 'login.png')
    driver.quit()

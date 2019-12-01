from selenium.webdriver import Remote
from selenium import webdriver
from time import sleep
def browser():
    driver = webdriver.Chrome()
    return driver

if __name__ =='__main__':
    dr=browser()
    dr.get("https://test.xliane.com/html2/webapp/fastIssue/index.html#/customerRecommend/index")
    sleep(3)
    dr.quit()
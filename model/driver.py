from time import sleep

from selenium import webdriver


def browser():
    driver = webdriver.Chrome()
    return driver


if __name__ == '__main__':
    dr = browser()
    dr.get("https://test.xliane.com/html2/webapp/fastIssue/index.html#/customerRecommend/index")
    sleep(3)
    dr.quit()

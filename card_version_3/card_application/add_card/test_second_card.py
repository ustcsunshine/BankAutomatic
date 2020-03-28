import time
from card_version_3.card_application.add_card.mac_upload import UploadClick, UploadClick
from card_version_3.card_application.basic_info.basic_info import CardApplicationBasicInfo
from utils import file_util
from model import unit_init


class SecondCardTest(unit_init.Base):

    def test_upload(self):
        file_util.upload_file(UploadClick(self.driver).upload_click,
                              'https://test.xliane.com/html3/webapp/fastIssue/index.html#/recruit/entry1',
                              '//*[@id="app"]/div/div[2]/div[2]/img', "/Users/jingjing.li/Downloads/kong.jpeg")
        time.sleep(1)

    def test_add_card(self):
        url = 'https://test.xliane.com/html3/webapp/fast-issue-con/parnter.html?id=1cdced2a92f841c38792060bbf516c60'
        CardApplicationBasicInfo(self.driver).open_login("孔夫子", 110224199201305248, 15111161603, url)
        time.sleep(3)
        # file_util.load_file(UploadClick(self.driver).upload_click_no_open,
        #                     '//*[@id="img1"]', "/Users/jingjing.li/Downloads/kong.jpeg")
        time.sleep(2)
        file_util.load_file(UploadClick(self.driver).upload_click_no_open,
                            '//*[@id="img1"]', "/Users/jingjing.li/Downloads/kong.jpeg")
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[12]/div[3]/a').click()
        time.sleep(2)
        file_util.load_file(UploadClick(self.driver).upload_click_no_open,
                            '//*[@id="img2"]', "/Users/jingjing.li/Downloads/kongfan.jpeg")
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[16]/div[3]/a').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="next"]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="startDate"]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[1]/div/div[66]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[1]/div/div[63]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/a').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="confirmtrue"]').click()
        time.sleep(300)

    def test_add_card_name(self):
        url = 'https://test.xliane.com/html3/webapp/fast-issue-con/parnter.html?id=1cdced2a92f841c38792060bbf516c60'
        CardApplicationBasicInfo(self.driver).open_login("李济含", 132801197706054629, 17701687725, url)
        time.sleep(3)
        # file_util.load_file(UploadClick(self.driver).upload_click_no_open,
        #                     '//*[@id="img1"]', "/Users/jingjing.li/Downloads/kong.jpeg")
        time.sleep(2)
        file_util.load_file(UploadClick(self.driver).upload_click_no_open,
                            '//*[@id="img1"]', "/Users/jingjing.li/Downloads/hantou.jpeg")
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[12]/div[3]/a').click()
        time.sleep(2)
        file_util.load_file(UploadClick(self.driver).upload_click_no_open,
                            '//*[@id="img2"]', "/Users/jingjing.li/Downloads/hangr.jpeg")
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[16]/div[3]/a').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="next"]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="startDate"]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[1]/div/div[66]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[1]/div/div[63]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/a').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="confirmtrue"]').click()
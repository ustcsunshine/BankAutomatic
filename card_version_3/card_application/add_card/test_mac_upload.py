import time

from card_version_3.card_application.add_card.mac_upload import UploadClick, UploadClick
from card_version_3.card_application.basic_info.basic_info import CardApplicationBasicInfo
from utils import file_util
from model import unit_init


class UploadClickTest(unit_init.Base):


    def test_upload(self):
        file_util.upload_file(UploadClick(self.driver).upload_click,
                              'https://test.xliane.com/html3/webapp/fastIssue/index.html#/recruit/entry1',
                              '//*[@id="app"]/div/div[2]/div[2]/img', "/Users/jingjing.li/Downloads/kong.jpeg")
        time.sleep(3600)

    def test_no_url(self):
        UploadClick(self.driver).open('https://test.xliane.com/html3/webapp/fastIssue/index.html#/recruit/entry1')
        file_util.load_file(UploadClick(self.driver).upload_click_no_open,
                              '//*[@id="app"]/div/div[2]/div[2]/img', "/Users/jingjing.li/Downloads/kong.jpeg")
        time.sleep(3600)




from card_version_3.card_application.basic_info.basic_info import CardApplicationBasicInfo
from card_version_3.card_application.detail_info.detail_info import CardApplicationDetailInfo
from card_version_3.card_application.other_info.other_info import CardApplicationOtherInfo
from model import unit_init
from utils.identity_util import CreateIDCardTest
from utils.phone_util import Phone
from time import sleep
from selenium.webdriver.common.keys import Keys

from pykeyboard import PyKeyboard
from pymouse import PyMouse
import pyperclip
import time
from selenium.webdriver.common.by import By

from web.login_operator import LoginOperator


class UploadClick(LoginOperator):

    def upload_click(self, url, location):
        self.open(url)
        sleep(1)
        self.click((By.XPATH, location))

    def upload_click_no_open(self, location):
        self.click((By.XPATH, location))





from card_version_3.car_payment.basic_info.basic_info import CarPaymentBasicInfo
from card_version_3.car_payment.personal_info.personal_info import CarPaymentPersonalInfo
from card_version_3.car_payment.pretrial_application.pretrial_application import CarPaymentApplyInfo
from model import unit_init
from utils.identity_util import CreateIDCardTest
from utils.phone_util import Phone
from utils.url import CardUrl
from web.login_operator import LoginOperator


class CarPaymentTest(unit_init.Base):

    def test_car_payment(self):
        CarPaymentBasicInfo(self.driver).open_login("李大亿", CreateIDCardTest.CreateIDCard(), "110", "10", CardUrl.CAR_PAYMENT_URL)

        CarPaymentPersonalInfo(self.driver).login("上海科技馆有限公司", 110)

        CarPaymentApplyInfo(self.driver).login(Phone.create_phone())

    def click(self):
        LoginOperator(self.driver).click(self.salon_banner_loc)


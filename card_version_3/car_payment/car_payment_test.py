from card_version_3.car_payment.basic_info.basic_info import CarPaymentBasicInfo
from card_version_3.car_payment.personal_info.personal_info import CarPaymentPersonalInfo
from card_version_3.car_payment.pretrial_application.pretrial_application import CarPaymentApplyInfo
from model import unit_init


class CarPaymentTest(unit_init.Base):

    def test_car_payment(self):
        url = 'https://test.xliane.com/html2/car-instalment3/index.html'
        CarPaymentBasicInfo(self.driver).open_login("李个一", "110101198701048327", "110", "10", url)

        CarPaymentPersonalInfo(self.driver).login("上海科技馆有限公司", 110)

        CarPaymentApplyInfo(self.driver).login('17621523735')

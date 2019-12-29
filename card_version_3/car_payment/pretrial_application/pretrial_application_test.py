from card_version_3.car_payment.pretrial_application.pretrial_application import CarPaymentApplyInfo
from model import unit_init
from utils.url import CardUrl


class CarPaymentPretrialApplicationTest(unit_init.Base):

    def car_payment_pretrial_application_page(self, phone, url):
        CarPaymentApplyInfo(self.driver).open_login(phone, url)

    def test_car_payment_apply_info(self):
        self.car_payment_pretrial_application_page("17621523736", CardUrl.CAR_PAYMENT_PRETRIAL_APPLICATION_URL)

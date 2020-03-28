from card_version_3.car_payment.pretrial_application.pretrial_application import CarPaymentApplyInfo
from model import unit_init
from utils.phone_util import Phone
from utils.url import CardUrl


class CarPaymentPretrialApplicationTest(unit_init.Base):

    def car_payment_pretrial_application_page(self, phone, url):
        CarPaymentApplyInfo(self.driver).open_login(phone, url)

    def test_car_payment_apply_info(self):
        self.car_payment_pretrial_application_page(Phone.create_phone(), CardUrl.CAR_PAYMENT_PRETRIAL_APPLICATION_URL)
        car_apply_label = self.driver.find_element_by_xpath('/html/body/div[3]')
        self.assertIn(car_apply_label.text, ' Redis过期')



    def test_car_payment_apply_phone_miss(self):
        self.car_payment_pretrial_application_page('123000000', CardUrl.CAR_PAYMENT_PRETRIAL_APPLICATION_URL)
        car_apply_label = self.driver.find_element_by_xpath('/html/body/div[3]')
        self.assertEqual(car_apply_label.text, '请输入11位手机号')

    def test_car_payment_apply_phone_space(self):
        self.car_payment_pretrial_application_page('12345678 01', CardUrl.CAR_PAYMENT_PRETRIAL_APPLICATION_URL)
        car_apply_label = self.driver.find_element_by_xpath('/html/body/div[3]')
        self.assertEqual(car_apply_label.text, '请输入11位手机号')

    def test_car_payment_apply_phone_english(self):
        self.car_payment_pretrial_application_page('12345678m01', CardUrl.CAR_PAYMENT_PRETRIAL_APPLICATION_URL)
        car_apply_label = self.driver.find_element_by_xpath('/html/body/div[3]')
        self.assertEqual(car_apply_label.text, '请输入11位手机号')

from bank.test.car_payment.car_payment_first import CarPaymentBasicInfo
from bank.test.car_payment.car_payment_second import CarPaymentPersonalInfo
from bank.test.car_payment.car_payment_three import CarPaymentApplyInfo
from bank.test.models import myunit


class CarPaymentTest(myunit.MyTest):

    def test_car_payment(self):
        url = 'https://test.xliane.com/html2/car-instalment3/index.html'
        CarPaymentBasicInfo(self.driver).car_payment_basic_info("李个一", "110101198701048327", "110", "10", url)

        CarPaymentPersonalInfo(self.driver).personal_info("上海科技馆有限公司", 110)

        CarPaymentApplyInfo(self.driver).apply_info('17621523735')



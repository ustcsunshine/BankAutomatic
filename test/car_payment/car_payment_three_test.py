from test.models import myunit
from test.car_payment.car_payment_three import CarPaymentApplyInfo


class CarPaymentApplyTest(myunit.MyTest):

    def car_payment_apply_page(self, phone, url):
        # url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/mgm/index'
        CarPaymentApplyInfo(self.driver).car_payment_apply_info(phone, url)



    def test_car_payment_apply_info(self):
        url = 'https://test.xliane.com/html/car-instalment3/apply.html'
        self.car_payment_apply_page("17621523736", url)





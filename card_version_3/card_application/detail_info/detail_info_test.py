from card_version_3.card_application.detail_info.detail_info import DetailInfo
from models import myunit


class DetailInfoTest(myunit.MyTest):

    # def process_first_page(self, username, identity, phone, url):
    #     # url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/mgm/index'
    #     DetailInfo(self.driver).fast_detail_info(username, identity, phone, url)

    def info_login_verify(self, company, area, line, departaddr, departname, salary, homeaddr, url):
        # url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/mgm/index'
        DetailInfo(self.driver).fast_detail_info(company, area, line, departaddr, departname, salary, homeaddr, url)

    # 正常填写详情页
    def test_login_detail_info(self):
        url = 'https://test.xliane.com/html3/webapp/fast-issue-con/process_two.html'
        self.info_login_verify("上海蓝天科技有限公司", "021", "6951691", "浦东新区来安路500号", "业务部", "120", "广兰路200号", url)

    # 详情页的公司名称为空时
    def test_login_detail_name_null(self):
        url = 'https://test.xliane.com/html3/webapp/fast-issue-con/process_two.html'
        self.info_login_verify("", "021", "6951691", "浦东新区来安路500号", "业务部", "120", "广兰路200号", url)
        base_info_label = self.driver.find_element_by_xpath('/html/body/div[7]')
        self.assertEqual(base_info_label.text, '单位名称不能为空')

    # 详情页的公司名称超过15位时
    def test_login_detail_name_more(self):
        url = 'https://test.xliane.com/html3/webapp/fast-issue-con/process_two.html'
        self.info_login_verify("上海科技馆有限公司是是是是是是是", "021", "6951691", "浦东新区来安路500号", "业务部", "120", "广兰路200号", url)
        base_info_label = self.driver.find_element_by_xpath('/html/body/div[7]')
        self.assertEqual(base_info_label.text, '单位名称不能超过15个汉字')

    # 详情页的区号不正确时
    def test_login_detail_area_miss(self):
        url = 'https://test.xliane.com/html3/webapp/fast-issue-con/process_two.html'
        self.info_login_verify("上海科技馆有限公", "0214", "6951691", "浦东新区来安路500号", "业务部", "120", "广兰路200号", url)
        base_info_label = self.driver.find_element_by_xpath('/html/body/div[7]')
        self.assertEqual(base_info_label.text, '您输入的区号不存在，请重新输入')

    # 详情页的区号为空时
    def test_login_detail_area_null(self):
        url = 'https://test.xliane.com/html3/webapp/fast-issue-con/process_two.html'
        self.info_login_verify("上海科技馆有限公", "", "6951691", "浦东新区来安路500号", "业务部", "120", "广兰路200号", url)
        base_info_label = self.driver.find_element_by_xpath('/html/body/div[7]')
        self.assertEqual(base_info_label.text, '区号不能为空')

    # 详情页的区号为英文
    def test_login_detail_area_null(self):
        url = 'https://test.xliane.com/html3/webapp/fast-issue-con/process_two.html'
        self.info_login_verify("上海科技馆有限公", "12m", "6951691", "浦东新区来安路500号", "业务部", "120", "广兰路200号", url)
        base_info_label = self.driver.find_element_by_xpath('/html/body/div[7]')
        self.assertEqual(base_info_label.text, '请输入正确的区号')

    # 详情页的手机号码为英文
    def test_login_detail_phone_english(self):
        url = 'https://test.xliane.com/html3/webapp/fast-issue-con/process_two.html'
        self.info_login_verify("上海科技馆有限公", "021", "695169m", "浦东新区来安路500号", "业务部", "120", "广兰路200号", url)
        base_info_label = self.driver.find_element_by_xpath('/html/body/div[7]')
        self.assertEqual(base_info_label.text, '请输入正确的电话号码')

    # 详情页的手机号码为中文
    def test_login_detail_phone_chinese(self):
        url = 'https://test.xliane.com/html3/webapp/fast-issue-con/process_two.html'
        self.info_login_verify("上海科技馆有限公", "021", "695169你", "浦东新区来安路500号", "业务部", "120", "广兰路200号", url)
        base_info_label = self.driver.find_element_by_xpath('/html/body/div[7]')
        self.assertEqual(base_info_label.text, '请输入正确的电话号码')

    # 详情页的手机号码为空
    def test_login_detail_phone_null(self):
        url = 'https://test.xliane.com/html3/webapp/fast-issue-con/process_two.html'
        self.info_login_verify("上海科技馆有限公", "021", "", "浦东新区来安路500号", "业务部", "120", "广兰路200号", url)
        base_info_label = self.driver.find_element_by_xpath('/html/body/div[7]')
        self.assertEqual(base_info_label.text, '电话号码不能为空')

    # 详情页的手机号码少一位
    def test_login_detail_phone_miss(self):
        url = 'https://test.xliane.com/html3/webapp/fast-issue-con/process_two.html'
        self.info_login_verify("上海科技馆有限公", "021", "695169", "浦东新区来安路500号", "业务部", "120", "广兰路200号", url)
        base_info_label = self.driver.find_element_by_xpath('/html/body/div[7]')
        self.assertEqual(base_info_label.text, '请输入正确的电话号码')

    # 详情页的手机号码9位时
    def test_login_detail_phone_more(self):
        url = 'https://test.xliane.com/html3/webapp/fast-issue-con/process_two.html'
        self.info_login_verify("上海科技馆有限公", "021", "695169567", "浦东新区来安路500号", "业务部", "120", "广兰路200号", url)
        base_info_label = self.driver.find_element_by_xpath('/html/body/div[7]')
        self.assertEqual(base_info_label.text, '请输入正确的电话号码')

    # 详情页的详细地址为空时
    def test_login_detail_home_null(self):
        url = 'https://test.xliane.com/html3/webapp/fast-issue-con/process_two.html'
        self.info_login_verify("上海科技馆有限公", "021", "695169567", "", "业务部", "120", "广兰路200号", url)
        base_info_label = self.driver.find_element_by_xpath('/html/body/div[7]')
        self.assertEqual(base_info_label.text, '详细地址不能为空')

    # 详情页的详细地址超过22个字时
    def test_login_detail_home_more(self):
        url = 'https://test.xliane.com/html3/webapp/fast-issue-con/process_two.html'
        self.info_login_verify("上海科技馆有限公", "021", "695169567", "浦东新区来安路500号，浦东新区来安路500号，浦东新区来安路500号", "业务部", "120", "广兰路200号", url)
        base_info_label = self.driver.find_element_by_xpath('/html/body/div[7]')
        self.assertEqual(base_info_label.text, '详细地址不能为空')

    # 详情页的年收入为空时
    def test_login_detail_salary_null(self):
        url = 'https://test.xliane.com/html3/webapp/fast-issue-con/process_two.html'
        self.info_login_verify("上海科技馆有限公", "021", "695169567", "浦东新区来安路500号", "业务部", "", "广兰路200号", url)
        base_info_label = self.driver.find_element_by_xpath('/html/body/div[7]')
        self.assertEqual(base_info_label.text, '请输入您的年收入')

    # 详情页的年收入为0时
    def test_login_detail_salary_zero(self):
        url = 'https://test.xliane.com/html3/webapp/fast-issue-con/process_two.html'
        self.info_login_verify("上海科技馆有限公", "021", "695169567", "浦东新区来安路500号", "业务部", "0", "广兰路200号", url)
        base_info_label = self.driver.find_element_by_xpath('/html/body/div[7]')
        self.assertEqual(base_info_label.text, '年收入不能为0')

    # 详情页的年收入带小数点时
    def test_login_detail_salary_point(self):
        url = 'https://test.xliane.com/html3/webapp/fast-issue-con/process_two.html'
        self.info_login_verify("上海科技馆有限公", "021", "695169567", "浦东新区来安路500号", "业务部", "1.5", "广兰路200号", url)
        base_info_label = self.driver.find_element_by_xpath('/html/body/div[7]')
        self.assertEqual(base_info_label.text, '年收入格式不正确')


    # 详情页的详细地址为空时
    def test_login_detail_address_null(self):
        url = 'https://test.xliane.com/html3/webapp/fast-issue-con/process_two.html'
        self.info_login_verify("上海科技馆有限公", "021", "695169567", "来安路500号", "业务部", "120", "", url)
        base_info_label = self.driver.find_element_by_xpath('/html/body/div[7]')
        self.assertEqual(base_info_label.text, '详细地址不能为空')


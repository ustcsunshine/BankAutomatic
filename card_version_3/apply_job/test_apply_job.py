from card_version_3.apply_job.apply_job import ApplyJobInfo
from model import unit_init
from time import sleep

from utils.phone_util import Phone
from utils.url import CardUrl


class ApplyInfoTest(unit_init.Base):

    def apply_info_job(self, username, phone, root, degree, major, company, now_major, salary, recommand,
                       recommand_phone, url):
        ApplyJobInfo(self.driver).open_login(username, phone, root, degree, major, company, now_major, salary,
                                             recommand, recommand_phone, url)
        return self.driver

    # TODO  报错 AssertionError: '{ "code": "000000", "msg": "应聘信息报文发送成功" }' not found in ''
    def test_apply_job(self):
        self.apply_info_job('测试姓名', Phone.create_phone(), '北京', '某某大学', '财务专业', '某公司', '网发测试', '1000', '李大大',
                            '13000000000', CardUrl.APPLY_JOB_URL)
        text = self.driver.find_element_by_xpath('//*[@id="mid"]/div/i').text
        sleep(1)
        self.assertIn('填报成功,感谢您的配合', text)

    # 校验姓名不填时
    def test_apply_username_null(self):
        self.apply_info_job('', Phone.create_phone(), '北京', '某某大学', '财务专业', '某公司', '网发测试', '1000', '李大大', Phone.create_phone(),
                            CardUrl.APPLY_JOB_URL)
        text=self.driver.find_element_by_class_name('a_msg').text
        self.assertIn('请填写完所有必填项', text)

    # 校验姓名为空时
    def test_apply_username_space(self):
        self.apply_info_job(' ', Phone.create_phone(), '北京', '某某大学', '财务专业', '某公司', '网发测试', '1000', '李大大', Phone.create_phone(),
                            CardUrl.APPLY_JOB_URL)
        text=self.driver.find_element_by_class_name('a_msg').text
        self.assertIn('请正确填写', text)

    # 校验姓名为一个字时
    def test_apply_username_one(self):
        self.apply_info_job('李', Phone.create_phone(), '北京', '某某大学', '财务专业', '某公司', '网发测试', '1000', '李大大', Phone.create_phone(),
                            CardUrl.APPLY_JOB_URL)
        text=self.driver.find_element_by_class_name('a_msg').text
        self.assertIn('请正确填写', text)

    # 校验姓名为数字时
    def test_apply_username_number(self):
        self.apply_info_job('12', Phone.create_phone(), '北京', '某某大学', '财务专业', '某公司', '网发测试', '1000', '李大大',
                            Phone.create_phone(), CardUrl.APPLY_JOB_URL)
        text=self.driver.find_element_by_class_name('a_msg').text
        self.assertIn('请正确填写', text)

    # 校验姓名为英文时
    def test_apply_username_english(self):
        self.apply_info_job('mrs li', Phone.create_phone(), '北京', '某某大学', '财务专业', '某公司', '网发测试', '1000', '李大大',
                            Phone.create_phone(), CardUrl.APPLY_JOB_URL)
        text=self.driver.find_element_by_class_name('a_msg').text
        self.assertIn('请正确填写', text)

    # 校验姓名为英文＋数字＋中文
    def test_apply_username_all(self):
        self.apply_info_job('mrs12李', Phone.create_phone(), '北京', '某某大学', '财务专业', '某公司', '网发测试', '1000', '李大大',
                            Phone.create_phone(), CardUrl.APPLY_JOB_URL)
        text=self.driver.find_element_by_class_name('a_msg').text
        self.assertIn('请正确填写', text)

    # 校验姓名包含特殊字符时
    def test_apply_username_character(self):
        self.apply_info_job('李？', Phone.create_phone(), '北京', '某某大学', '财务专业', '某公司', '网发测试', '1000', '李大大',
                            Phone.create_phone(), CardUrl.APPLY_JOB_URL)
        text=self.driver.find_element_by_class_name('a_msg').text
        self.assertIn('请正确填写', text)

    # 校验手机号码不填时
    def test_apply_phone_null(self):
        self.apply_info_job('李大大', '', '北京', '某某大学', '财务专业', '某公司', '网发测试', '1000', '李大大', Phone.create_phone(),
                            CardUrl.APPLY_JOB_URL)
        text=self.driver.find_element_by_class_name('a_msg').text
        self.assertIn('请填写完所有必填项', text)

    # 校验手机号码为空时
    def test_apply_phone_space(self):
        self.apply_info_job('李大大', ' ', '北京', '某某大学', '财务专业', '某公司', '网发测试', '1000', '李大大', Phone.create_phone(),
                            CardUrl.APPLY_JOB_URL)
        text=self.driver.find_element_by_class_name('a_msg').text
        self.assertIn('请正确填写', text)

    # 校验手机号码少于11位时
    def test_apply_phone_less(self):
        self.apply_info_job('李大大', '1200000000', '北京', '某某大学', '财务专业', '某公司', '网发测试', '1000', '李大大',
                            Phone.create_phone(), CardUrl.APPLY_JOB_URL)
        text=self.driver.find_element_by_class_name('a_msg').text
        self.assertIn('请正确填写', text)

    # 校验手机号码有中文
    def test_apply_phone_chinese(self):
        self.apply_info_job('李大大', '1200000000这', '北京', '某某大学', '财务专业', '某公司', '网发测试', '1000', '李大大',
                            Phone.create_phone(), CardUrl.APPLY_JOB_URL)
        text=self.driver.find_element_by_class_name('a_msg').text
        self.assertIn('请正确填写', text)

    # 校验手机号码有英文
    def test_apply_phone_english(self):
        self.apply_info_job('李大大', '1200000000m', '北京', '某某大学', '财务专业', '某公司', '网发测试', '1000', '李大大',
                            Phone.create_phone(), CardUrl.APPLY_JOB_URL)
        text=self.driver.find_element_by_class_name('a_msg').text
        self.assertIn('请正确填写', text)

    # 校验手机号码非1开头
    def test_apply_phone_number(self):
        self.apply_info_job('李大大', '21000000000', '北京', '某某大学', '财务专业', '某公司', '网发测试', '1000', '李大大',
                            Phone.create_phone(), CardUrl.APPLY_JOB_URL)
        text=self.driver.find_element_by_class_name('a_msg').text
        self.assertIn('请正确填写', text)

    # 校验籍贯为空格时
    def test_apply_root_null(self):
        self.apply_info_job('李大大', Phone.create_phone(), ' ', '某某大学', '财务专业', '某公司', '网发测试', '1000', '李大大',
                            Phone.create_phone(), CardUrl.APPLY_JOB_URL)
        text = self.driver.find_element_by_xpath('//*[@id="mid"]/div/i').text
        self.assertIn('填报成功,感谢您的配合', text)


    # 校验籍贯为中文时
    def test_apply_root_chinese(self):
        self.apply_info_job('李大大', Phone.create_phone(), '北京', '某某大学', '财务专业', '某公司', '网发测试', '1000', '李大大',
                            Phone.create_phone(), CardUrl.APPLY_JOB_URL)
        text = self.driver.find_element_by_xpath('//*[@id="mid"]/div/i').text
        self.assertIn('填报成功,感谢您的配合', text)

    # 校验籍贯为英文时
    def test_apply_root_english(self):
        self.apply_info_job('李大大', Phone.create_phone(), 'beijing ', '某某大学', '财务专业', '某公司', '网发测试', '1000', '李大大',
                            '13000000000', CardUrl.APPLY_JOB_URL)
        text = self.driver.find_element_by_xpath('//*[@id="mid"]/div/i').text
        self.assertIn('填报成功,感谢您的配合', text)

    # TODO 有符号<>，报  "msg": "应聘信息发送异常，请关闭页面重试"
    # TODO  报错 AssertionError: '{ "code": "000000", "msg": "应聘信息报文发送成功" }' not found in ''
    # 校验籍贯为特殊字符时
    def test_apply_root_character(self):
        self.apply_info_job('李大大', Phone.create_phone(), '<br> ', '某某大学', '财务专业', '某公司', '网发测试', '1000', '李大大',
                            Phone.create_phone(), CardUrl.APPLY_JOB_URL)
        text = self.driver.find_element_by_xpath('//*[@id="mid"]/div/i').text
        self.assertIn('填报成功,感谢您的配合', text)

    # 校验毕业院校为空时
    def test_apply_degree_null(self):
        self.apply_info_job('李大大', Phone.create_phone(), '北京', '', '财务专业', '某公司', '网发测试', '1000', '李大大', Phone.create_phone(),
                            CardUrl.APPLY_JOB_URL)
        sleep(1)
        text=self.driver.find_element_by_class_name('a_msg').text
        self.assertIn('请填写完所有必填项', text)

    # 校验毕业院校为空格时
    def test_apply_degree_space(self):
        self.apply_info_job('李大大', '11000000000', '北京', ' ', '财务专业', '某公司', '网发测试', '1000', '李大大', Phone.create_phone(),
                            CardUrl.APPLY_JOB_URL)
        text=self.driver.find_element_by_class_name('a_msg').text
        self.assertIn('应聘人员最高学历毕业院校为空:', text)

    # 校验毕业院校一个字时
    def test_apply_degree_number(self):
        self.apply_info_job('李大大', '11000000000', '北京', '学', '财务专业', '某公司', '网发测试', '1000', '李大大', Phone.create_phone(),
                            CardUrl.APPLY_JOB_URL)
        text = self.driver.find_element_by_xpath('//*[@id="mid"]/div/i').text
        self.assertIn('填报成功,感谢您的配合', text)

    # 校验毕业院校48个就截取
    def test_apply_degree_more(self):
        self.apply_info_job('神仙姐姐', Phone.create_phone(), '北京',
                            '上海华师大1上海华师大2上海华师大3上海华师大4上海华师大5上海华师大6上海华师大7上海华师大8上海华师大9上海华师大10', '财务专业', '某公司', '网发测试',
                            '1000', '李大大', Phone.create_phone(),
                            CardUrl.APPLY_JOB_URL)
        text = self.driver.find_element_by_xpath('//*[@id="mid"]/div/i').text
        self.assertIn('填报成功,感谢您的配合', text)

    # 校验毕业院校为英文时
    def test_apply_degree_english(self):
        self.apply_info_job('李大大', Phone.create_phone(), '北京',
                            'wuhandaxue', '财务专业', '某公司', '网发测试',
                            '1000', '李大大', Phone.create_phone(),
                            CardUrl.APPLY_JOB_URL)
        text = self.driver.find_element_by_xpath('//*[@id="mid"]/div/i').text
        self.assertIn('填报成功,感谢您的配合', text)


    # 校验毕业院校为英文中文
    def test_apply_degree_all(self):
        self.apply_info_job('李大大', Phone.create_phone(), '北京',
                            'wuhandaxue 武汉大学', '财务专业', '某公司', '网发测试',
                            '1000', '李大大', Phone.create_phone(),
                            CardUrl.APPLY_JOB_URL)
        text = self.driver.find_element_by_xpath('//*[@id="mid"]/div/i').text
        self.assertIn('填报成功,感谢您的配合', text)


    # 校验毕业专业为空时
    def test_apply_major_null(self):
        self.apply_info_job('李大大', Phone.create_phone(), '北京',
                            '上海大学', '', '某公司', '网发测试',
                            '1000', '李大大', Phone.create_phone(),
                            CardUrl.APPLY_JOB_URL)
        text=self.driver.find_element_by_class_name('a_msg').text
        self.assertIn('请填写完所有必填项', text)

    # 校验毕业专业为空格时
    def test_apply_major_space(self):
        self.apply_info_job('李大大', Phone.create_phone(), '北京',
                           '上海大学', ' ', '某公司', '网发测试',
                           '1000', '李大大', Phone.create_phone(),
                           CardUrl.APPLY_JOB_URL)
        text=self.driver.find_element_by_class_name('a_msg').text
        self.assertIn('应聘人员最高学历专业为空:', text)


    # 校验毕业专业为一个字时
    def test_apply_major_one(self):
        self.apply_info_job('李大大', Phone.create_phone(), '北京',
                            '上海大学', '业', '某公司', '网发测试',
                            '1000', '李大大', Phone.create_phone(),
                            CardUrl.APPLY_JOB_URL)
        text = self.driver.find_element_by_xpath('//*[@id="mid"]/div/i').text
        self.assertIn('填报成功,感谢您的配合', text)

    # 校验毕业专业为英文时
    def test_apply_major_english(self):
        self.apply_info_job('李大大', Phone.create_phone(), '北京',
                            '上海大学', 'finacl', '某公司', '网发测试',
                            '1000', '李大大', Phone.create_phone(),
                            CardUrl.APPLY_JOB_URL)
        text = self.driver.find_element_by_xpath('//*[@id="mid"]/div/i').text
        self.assertIn('填报成功,感谢您的配合', text)

    # 校验毕业专业为英文＋中文＋
    def test_apply_major_all(self):
        self.apply_info_job('李大大', Phone.create_phone(), '北京',
                            '上海大学', 'finacl专业', '某公司', '网发测试',
                            '1000', '李大大', Phone.create_phone(),
                            CardUrl.APPLY_JOB_URL)
        text = self.driver.find_element_by_xpath('//*[@id="mid"]/div/i').text
        self.assertIn('填报成功,感谢您的配合', text)

    # 校验现工作单位为空时
    def test_apply_company_null(self):
        self.apply_info_job('李大大', Phone.create_phone(), '北京',
                            '上海大学', '审计专业', '', '网发测试',
                            '1000', '李大大', Phone.create_phone(),
                            CardUrl.APPLY_JOB_URL)
        text=self.driver.find_element_by_class_name('a_msg').text
        self.assertIn('请填写完所有必填项', text)

    # 校验现工作单位有空格时
    def test_apply_company_space(self):
        self.apply_info_job('李大大', Phone.create_phone(), '北京',
                            '上海大学', '审计专业', '某 公司', '网发测试',
                            '1000', '李大大', Phone.create_phone(),
                            CardUrl.APPLY_JOB_URL)
        text = self.driver.find_element_by_xpath('//*[@id="mid"]/div/i').text
        self.assertIn('填报成功,感谢您的配合', text)

    # 校验现工作单位有英文时
    def test_apply_company_english(self):
        self.apply_info_job('李大大', Phone.create_phone(),'北京',
                            '上海大学', '审计专业', '某公司company', '网发测试',
                            '1000', '李大大', Phone.create_phone(),
                            CardUrl.APPLY_JOB_URL)
        text = self.driver.find_element_by_xpath('//*[@id="mid"]/div/i').text
        self.assertIn('填报成功,感谢您的配合', text)

    # 校验现工作单位有英文＋数字＋符号时
    # TODO  报错 AssertionError: '{ "code": "000000", "msg": "应聘信息报文发送成功" }' not found in ''
    def test_apply_company_all(self):
        self.apply_info_job('李大大', Phone.create_phone(), '北京',
                            '上海大学', '审计专业', 'nowcompany蓝天', '网发测试',
                            '1000', '李大大', Phone.create_phone(),
                            CardUrl.APPLY_JOB_URL)
        text = self.driver.find_element_by_xpath('//*[@id="mid"]/div/i').text
        self.assertIn('填报成功,感谢您的配合', text)

    # 校验现工作岗位为空时
    def test_apply_new_major_null(self):
        self.apply_info_job('李大大', Phone.create_phone(), '北京',
                            '上海大学', '审计专业', 'nowcompany蓝天', '',
                            '1000', '李大大', Phone.create_phone(),
                            CardUrl.APPLY_JOB_URL)
        text=self.driver.find_element_by_class_name('a_msg').text
        self.assertIn('请填写完所有必填项', text)

    # 校验现工作岗位有空格时
    def test_apply_new_major_space(self):
        self.apply_info_job('李大大', Phone.create_phone(), '北京',
                            '上海大学', '审计专业', 'nowcompany蓝天', '运营 岗',
                            '1000', '李大大', Phone.create_phone(),
                            CardUrl.APPLY_JOB_URL)
        text = self.driver.find_element_by_xpath('//*[@id="mid"]/div/i').text
        self.assertIn('填报成功,感谢您的配合', text)

    # 校验现工作岗位有英文时
    def test_apply_company_english(self):
        self.apply_info_job('李大大', Phone.create_phone(), '北京',
                            '上海大学', '审计专业', '某公司company', '运营岗 opt',
                            '1000', '李大大', Phone.create_phone(),
                            CardUrl.APPLY_JOB_URL)
        text = self.driver.find_element_by_xpath('//*[@id="mid"]/div/i').text
        self.assertIn('填报成功,感谢您的配合', text)

    # 校验薪资为空时
    def test_apply_salary_null(self):
        self.apply_info_job('李大大', Phone.create_phone(), '北京',
                            '上海大学', '审计专业', '某公司company', '运营岗 opt',
                            '', '李大大', Phone.create_phone(),
                            CardUrl.APPLY_JOB_URL)
        text = self.driver.find_element_by_xpath('//*[@id="mid"]/div/i').text
        self.assertIn('填报成功,感谢您的配合', text)

    # 校验薪资为9位时
    def test_apply_salary_number(self):
        self.apply_info_job('李大大', Phone.create_phone(), '北京',
                            '上海大学', '审计专业', '某公司company', '运营岗opt',
                            '111100000', '李大大', Phone.create_phone(),
                            CardUrl.APPLY_JOB_URL)
        text = self.driver.find_element_by_xpath('//*[@id="mid"]/div/i').text
        self.assertIn('填报成功,感谢您的配合', text)

    # 校验薪资0开头时
    def test_apply_salary_zero(self):
        self.apply_info_job('李大大', Phone.create_phone(), '北京',
                            '上海大学', '审计专业', '某公司company', '运营岗opt',
                            '01000', '李大大', Phone.create_phone(),
                            CardUrl.APPLY_JOB_URL)
        text=self.driver.find_element_by_class_name('a_msg').text
        self.assertIn('期望工资只能输入正整数且长度不能超过10位', text)

     # 校验推荐人姓名不填时
    def test_recommend_username_null(self):
        self.apply_info_job('姚大牙', Phone.create_phone(), '北京', '某某大学', '财务专业', '某公司', '网发测试', '1000', '',
                            Phone.create_phone(), CardUrl.APPLY_JOB_URL)
        text = self.driver.find_element_by_xpath('//*[@id="mid"]/div/i').text
        self.assertIn('填报成功,感谢您的配合', text)


    # 校验推荐人姓名为空时
    def test_recommend_username_space(self):
        self.apply_info_job('姚大牙', Phone.create_phone(), '北京', '某某大学', '财务专业', '某公司', '网发测试', '1000', '  ',
                            Phone.create_phone(), CardUrl.APPLY_JOB_URL)
        text=self.driver.find_element_by_class_name('a_msg').text
        self.assertIn('请正确填写', text)

    # 校验推荐人姓名为一个字时
    def test_recommend_username_one(self):
         self.apply_info_job('姚大牙', Phone.create_phone(), '北京', '某某大学', '财务专业', '某公司', '网发测试', '1000', '李',
                         Phone.create_phone(), CardUrl.APPLY_JOB_URL)
         text = self.driver.find_element_by_class_name('a_msg').text
         self.assertIn('请正确填写', text)

    # 校验推荐人姓名为数字时
    def test_recommend_username_number(self):
         self.apply_info_job('姚大牙', Phone.create_phone(), '北京', '某某大学', '财务专业', '某公司', '网发测试', '1000', '12李大',
                        Phone.create_phone(), CardUrl.APPLY_JOB_URL)
         text = self.driver.find_element_by_class_name('a_msg').text
         self.assertIn('请正确填写', text)

    # 校验姓名为英文时
    def test_recommend_username_english(self):
        self.apply_info_job('姚大牙', Phone.create_phone(), '北京', '某某大学', '财务专业', '某公司', '网发测试', '1000', 'miss li',
                        Phone.create_phone(), CardUrl.APPLY_JOB_URL)
        text=self.driver.find_element_by_class_name('a_msg').text
        self.assertIn('请正确填写', text)

    # 校验姓名为英文＋数字＋中文
    def test_recommend_username_all(self):
         self.apply_info_job('姚大牙', Phone.create_phone(), '北京', '某某大学', '财务专业', '某公司', '网发测试', '1000', 'miss李大大1',
                        Phone.create_phone(), CardUrl.APPLY_JOB_URL)
         text = self.driver.find_element_by_class_name('a_msg').text
         self.assertIn('请正确填写', text)

    # 校验姓名包含特殊字符时
    def test_recommend_username_character(self):
         self.apply_info_job('姚大牙', Phone.create_phone(), '北京', '某某大学', '财务专业', '某公司', '网发测试', '1000', '李大？大',
                        Phone.create_phone(), CardUrl.APPLY_JOB_URL)
         text = self.driver.find_element_by_class_name('a_msg').text
         self.assertIn('请正确填写', text)

   # 校验推荐人手机号码不填时
    def test_recommend_phone_null(self):
        self.apply_info_job('李大大', Phone.create_phone(), '北京', '某某大学', '财务专业', '某公司', '网发测试', '1000', '李大大', '',
                            CardUrl.APPLY_JOB_URL)
        text = self.driver.find_element_by_xpath('//*[@id="mid"]/div/i').text
        self.assertIn('填报成功,感谢您的配合', text)

    # 校验推荐人手机号码为空时
    def test_recommend_phone_space(self):
        self.apply_info_job('李大大', Phone.create_phone(),'北京', '某某大学', '财务专业', '某公司', '网发测试', '1000', '李大大', '  ',
                            CardUrl.APPLY_JOB_URL)
        text = self.driver.find_element_by_class_name('a_msg').text
        self.assertIn('请正确填写', text)

    # 校验手机号码少于11位时
    def test_recommend_phone_less(self):
        self.apply_info_job('李大大', Phone.create_phone(), '北京', '某某大学', '财务专业', '某公司', '网发测试', '1000', '李大大',
                            '1000000', CardUrl.APPLY_JOB_URL)
        text = self.driver.find_element_by_xpath('//*[@id="mid"]/div/i').text
        self.assertIn('填报成功,感谢您的配合', text)

    # 校验手机号码有中文
    def test_recommend_phone_chinese(self):
        self.apply_info_job('李大大', Phone.create_phone(), '北京', '某某大学', '财务专业', '某公司', '网发测试', '1000', '李大大',
                            '1300000000这', CardUrl.APPLY_JOB_URL)
        text = self.driver.find_element_by_class_name('a_msg').text
        self.assertIn('请正确填写', text)

    # 校验手机号码有英文
    def test_recommend_phone_english(self):
        self.apply_info_job('李大大', Phone.create_phone(), '北京', '某某大学', '财务专业', '某公司', '网发测试', '1000', '李大大',
                            '1300000000m', CardUrl.APPLY_JOB_URL)
        text = self.driver.find_element_by_class_name('a_msg').text
        self.assertIn('请正确填写', text)

    # 校验手机号码非1开头
    def test_recommend_phone_number(self):
        self.apply_info_job('李大大', Phone.create_phone(), '北京', '某某大学', '财务专业', '某公司', '网发测试', '1000', '李大大',
                            '23000000000', CardUrl.APPLY_JOB_URL)
        text = self.driver.find_element_by_xpath('//*[@id="mid"]/div/i').text
        self.assertIn('填报成功,感谢您的配合', text)

    # 所有必填项校验
    def test_all(self):
        self.apply_info_job('李大大', Phone.create_phone(), '', '某某大学', '财务专业', '某公司', '网发测试', '', '',
                            '', CardUrl.APPLY_JOB_URL)
        text = self.driver.find_element_by_xpath('//*[@id="mid"]/div/i').text
        self.assertIn('填报成功,感谢您的配合', text)
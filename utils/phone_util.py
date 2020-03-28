import random


class Phone:

    @staticmethod
    def create_phone():
        # 第一位为1，其余位为0-9
        # 第二位数字
        second = random.randint(0, 9)
        # 第三位数字
        third = random.randint(0, 9)

        # 最后八位数字
        suffix = random.randint(10000000, 99999999)

        # 拼接手机号
        return "1{}{}{}".format(second, third, suffix)


if __name__ == '__main__':
    phone = Phone.create_phone()
    print(phone)

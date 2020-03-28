from pykeyboard import PyKeyboard
from pymouse import PyMouse
import pyperclip
import time


def upload_file(self, file):
    # 定位上传按钮
    self.click(self.salon_banner_loc)
    k = PyKeyboard()
    m = PyMouse()
    # 模拟快捷键Command+Shift+G
    k.press_keys(['Command', 'Shift', 'G'])
    # 输入文件路径
    x_dim, y_dim = m.screen_size()
    m.click(x_dim // 2, y_dim // 2, 1)
    k.type_string(file)
    # 前往文件
    k.press_keys(['Return'])
    # 点击确定进行上传
    k.press_keys(['Return'])


import time
import pyperclip
from pykeyboard import PyKeyboard
from pymouse import PyMouse


def upload_file(click, url, location, file):
    click(url, location)
    k = PyKeyboard()
    m = PyMouse()
    filepath = '/'
    k.press_keys(['Command', 'Shift', 'G'])
    x_dim, y_dim = m.screen_size()
    m.click(x_dim // 2, y_dim // 2, 1)
    # 复制文件路径开头的斜杠/
    pyperclip.copy(filepath)
    # 粘贴斜杠/
    k.press_keys(['Command', 'V'])
    # 输入文件全路径进去
    k.type_string(file)
    k.press_key('Return')
    time.sleep(2)
    k.press_key('Return')
    time.sleep(2)


def load_file(click, location, file):
    click(location)
    k = PyKeyboard()
    m = PyMouse()
    filepath = '/'
    k.press_keys(['Command', 'Shift', 'G'])
    x_dim, y_dim = m.screen_size()
    m.click(x_dim // 2, y_dim // 2, 1)
    # 复制文件路径开头的斜杠/
    pyperclip.copy(filepath)
    # 粘贴斜杠/
    k.press_keys(['Command', 'V'])
    # 输入文件全路径进去
    k.type_string(file)
    k.press_key('Return')
    time.sleep(2)
    k.press_key('Return')
    time.sleep(2)

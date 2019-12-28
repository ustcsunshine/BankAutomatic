class BasePageOperator(object):

    def __init__(self, selenium_driver, parent=None):
        self.driver = selenium_driver
        self.timeout = 30
        self.parent = parent

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    def open(self, url):
        if url is None:
            return None
        self.driver.get(url)
        return 1

    def on_page(self):
        return self.driver.current_url == (self.base_url + self.url)

    def script(self, src):
        return self.driver.execute_script(src)

    def switch_frame(self, *frame):
        return self.dr.swtich_to_frame(*frame)

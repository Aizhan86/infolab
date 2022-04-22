from time import sleep
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from datetime import datetime


class BasePage(object):

    # Мы создаем конструктор, в котором передаются тело браузера и ссылка для дальнейшего использования

    def __init__(self, browser, url, timeout=10):
        super(BasePage, self).__init__()
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    # def get_environ(name, *args):
    #     environ = os.environ.get(name, "https://plhiv-demo.dec.kz/")
    #
    #     if str(environ).startswith('/run/secrets/'):
    #         if os.path.exists(environ):
    #             with open(environ, 'r') as secrets_file:
    #                 environ = secrets_file.read()
    #                 secrets_file.close()
    #
    #     return environ

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what, timeout=10):
        try:
            self.browser.find_element(how, what)
            self.browser.implicitly_wait(timeout)
        except NoSuchElementException:
            return False
        return True

    def make(self, action, timeout=10) -> object:
        try:
            self.browser.execute_script(action)
            self.browser.implicitly_wait(timeout)
        except NoSuchElementException:
            return False
        except TimeoutException:
            return False
        return True

    # def take_screenshot(self):
    #     now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    #     namefile = f"screenshot-{now}.png"
    #     self.browser.get_screenshot_as_file(namefile)
    #     self.browser.save_screenshot('C:\Work\plhiv-test\screenshots')
    #     print(f"Taked screenshot: {namefile}")

    def get_patient_id(self):
        enc = 0
        patient_id = self.browser.current_url.split('/')[-4]
        while patient_id == "0000000000":
            patient_id = self.browser.current_url.split('/')[-4]
            enc += 1
            sleep(1)
            if enc == 10:
                break
        return patient_id








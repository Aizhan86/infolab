from time import sleep
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from datetime import datetime

from .locators import AnalysisAddLocators


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

    def add_analysis(self, analysis_type, analysis_code):
        # открытие окна для добавления анализа
        self.make(f"{AnalysisAddLocators.ANALYSIS_ADD}.click()")
        sleep(2)
        # добавление анализа
        self.make(f"{AnalysisAddLocators.ANALYSIS_TYPE}.dropdown('set selected', '{analysis_type}');")
        sleep(3)
        if analysis_code == "6bad8d3e-02ca-4829-a6bd-d0110d0b2739":
            self.make(f"{AnalysisAddLocators.CLASSIFIER_GROUP_DROPDOWN}.dropdown('set selected', '{analysis_code}');")
            sleep(3)
            self.make(f"{AnalysisAddLocators.CHOOSE_IFA_IHLA_CHBX}.closest('.ui.checkbox').checkbox('check')")
        elif analysis_code == "ae231b40-89ed-4e39-ab0a-e05ecd7e3613":
            self.make(f"{AnalysisAddLocators.CLASSIFIER_GROUP_DROPDOWN}.dropdown('set selected', '{analysis_code}');")
            sleep(3)
            self.make(f"{AnalysisAddLocators.CHOOSE_A_APOLIPOPROTEN_CHBX}.closest('.ui.checkbox').checkbox('check')")
        elif analysis_code == "c3c9e575-2f8a-4f67-8410-f9de80519d60":
            self.make(f"{AnalysisAddLocators.ANALYSIS_GROUP_CHBX}.click()")
            sleep(5)
            self.make(f"{AnalysisAddLocators.CLASSIFIER_DD}.dropdown('set selected', '{analysis_code}');")
        elif analysis_code == "04b2311b-a744-4d50-a590-21b8b4eac9fe":
            self.make(f"{AnalysisAddLocators.CLASSIFIER_GROUP_DROPDOWN}.dropdown('set selected', '{analysis_code}');")
            sleep(3)
            self.make(f"{AnalysisAddLocators.CHOOSE_OAK_CHBX}.closest('.ui.checkbox').checkbox('check')")
        elif analysis_code == "7908a604-b5f2-4ea6-b903-add7d7812653":
            self.make(f"{AnalysisAddLocators.CLASSIFIER_GROUP_DROPDOWN}.dropdown('set selected', '{analysis_code}');")
            sleep(3)
            self.make(f"{AnalysisAddLocators.CHOOSE_OAM_CHBX}.closest('.ui.checkbox').checkbox('check')")
        sleep(3)
        self.make(f"{AnalysisAddLocators.ANALYSIS_SAVE}.click()")
        sleep(1)
        # получение id зарегистрированного пациента для осуществления дальнейших действий в других журналах

        BasePage.visit_id = self.browser.find_element(*AnalysisAddLocators.ANALYSIS_DATE_BTN).get_attribute("value")
        print(f'Код визита {BasePage.visit_id}')
        BasePage.analysis_id = self.browser.find_element(*AnalysisAddLocators.REFERRAL_TABLE).get_attribute("data-id")
        print(f'Код анализа {BasePage.analysis_id}')
        BasePage.patient_id = self.browser.current_url.split('/')[6]
        print(f'Код пациента {BasePage.patient_id}')
        # button1 = self.browser.find_element(*AnalysisAddLocators.REDUCT_BTN)
        self.make(f"{AnalysisAddLocators.CLOSE_BTN}.click()")
        sleep(2)







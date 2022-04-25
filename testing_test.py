from .pages.login_page import LoginPage
from .pages.work_page import WorkPage

def login(browser):
    LOGIN_URL = "https://infolab.dec.kz/ru/account/login?next=/ru/patient/"
    login_page = LoginPage(browser, LOGIN_URL)
    login_page.open()
    login_page.should_fill_login_form()
    login_page.go_to_work_page()

class TestIfaIhlaResultsModule():
    def test_register_form(self, browser):
        login(browser)
        work_page = WorkPage(browser, browser.current_url)
        work_page.should_fill_register_form()

    def test_addition_of_ifa_ihla(self, browser):
        work_page = WorkPage(browser, browser.current_url)
        work_page.should_add_ifa_ihla()

    def test_receipt_of_samples_form(self, browser):
        work_page = WorkPage(browser, browser.current_url)
        work_page.should_get_samples()

    def test_sorting_form(self, browser):
        work_page = WorkPage(browser, browser.current_url)
        work_page.should_send_samples_for_sorting()

    def test_results_of_ifa_ihla(self, browser):
        work_page = WorkPage(browser, browser.current_url)
        work_page.should_switch_to_results_page()
        work_page.should_submit_ifa_ihla_results()

class TestHbsagIfaAnalysisDiceModule():
    def test_dice_module(self, browser):
        login(browser)
        work_page = WorkPage(browser, browser.current_url)
        work_page.should_fill_register_form()
        work_page.should_add_hbsag_ifa_analysis()
        work_page.should_get_samples()
        work_page.should_send_samples_for_sorting()
        work_page.should_switch_to_dice_page()
        work_page.should_add_dice()

class TestBloodAnalysis():
    def test_gba_results(self, browser):
        login(browser)
        work_page = WorkPage(browser, browser.current_url)
        work_page.should_fill_register_form()
        work_page.should_add_blood_analysis()
        work_page.should_get_samples()
        work_page.should_send_samples_for_sorting()
        work_page.should_switch_to_results_page()
        work_page.should_submit_gba_results()

class TestUrineAnalysis():
    def test_gua_results(self, browser):
        login(browser)
        work_page = WorkPage(browser, browser.current_url)
        work_page.should_fill_register_form()
        work_page.should_add_urine_analysis()
        work_page.should_get_samples()
        work_page.should_send_samples_for_sorting()
        work_page.should_switch_to_results_page()
        work_page.should_submit_gua_results()

class TestBiochemistryAnalysis():
    def test_biochemistry_results(self, browser):
        login(browser)
        work_page = WorkPage(browser, browser.current_url)
        work_page.should_fill_register_form()
        work_page.should_add_biochemistry()
        work_page.should_get_samples()
        work_page.should_send_samples_for_sorting()
        work_page.should_switch_to_results_page()
        work_page.should_submit_biochemistry_results()
from .pages.login_page import LoginPage
from .pages.work_page import WorkPage

def login(browser):
    LOGIN_URL = "https://infolab.dec.kz/ru/account/login?next=/ru/patient/"
    login_page = LoginPage(browser, LOGIN_URL)
    login_page.open()
    login_page.should_fill_login_form()
    login_page.go_to_work_page()

class TestResultsModule():
    def test_register_form(self, browser):
        login(browser)
        work_page = WorkPage(browser, browser.current_url)
        work_page.should_fill_register_form()

    def test_addition_of_analysis_form(self, browser):
        work_page = WorkPage(browser, browser.current_url)
        work_page.should_add_IFA_analysis()

    def test_receipt_of_samples_form(self, browser):
        work_page = WorkPage(browser, browser.current_url)
        work_page.should_get_samples()

    def test_sorting_form(self, browser):
        work_page = WorkPage(browser, browser.current_url)
        work_page.should_send_samples_for_sorting()

    def test_results(self, browser):
        work_page = WorkPage(browser, browser.current_url)
        work_page.should_switch_to_results_page()
        work_page.should_submit_analysis_results()


class TestDiceModule():
    def test_dices_module(self, browser):
        login(browser)
        work_page = WorkPage(browser, browser.current_url)
        work_page.should_fill_register_form()
        work_page.should_add_IFA_analysis()
        work_page.should_get_samples()
        work_page.should_send_samples_for_sorting()
        work_page.should_switch_to_dice_page()
        work_page.should_add_dice()
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    user_name = 'spid.almaty'
    user_pass = '!Q2w3e4r5t6y7'
    login_url = "https://infolab.dec.kz/ru/account/login?next=/ru/patient/"

    def should_fill_login_form(self):
        # заполнение формы логина
        self.make(f"{LoginPageLocators.USER_NAME}.val('{self.user_name}')")
        self.make(f"{LoginPageLocators.USER_PASS}.val('{self.user_pass}')")
        self.make(f"{LoginPageLocators.LOGIN_BTN}.click()")

    def check_login_form(self):
        assert self.browser.execute_script(f"return {LoginPageLocators.LOGIN_FORM}.length"), "The login form is not accessible"

    def check_user_name(self):
        assert self.browser.execute_script(f"return {LoginPageLocators.USER_NAME}.length"), "No field for User's name"
        self.make(f"{LoginPageLocators.USER_NAME}.val('{self.user_name}')")
        assert self.browser.execute_script(f"return {LoginPageLocators.USER_NAME}.val()") == self.user_name, "The object User name didn't accept the value"

    def check_user_pass(self):
        assert self.browser.execute_script(f"return {LoginPageLocators.USER_PASS}.length"), "No field for User's password"
        self.make(f"{LoginPageLocators.USER_PASS}.val('{self.user_pass}')")
        assert self.browser.execute_script(f"return {LoginPageLocators.USER_PASS}.val()") == self.user_pass, "The object User password didn't accept the value"

    def check_login_btn(self):
        assert self.browser.execute_script(f"return {LoginPageLocators.LOGIN_BTN}.length"), "No Login button"
        self.make(f"{LoginPageLocators.LOGIN_BTN}.click()")
        # assert self.browser.current_url == "https://infolab.dec.kz/ru/queuenumber/", "Login button is not active"

    def go_to_work_page(self):
        assert self.browser.execute_script(f"return $('#journal_patients').length"), "No Patients module"
        self.make(f"window.location = $('#journal_patients').attr('href')") #переход на журнал "Пациенты"



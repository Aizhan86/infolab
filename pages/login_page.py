from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import PatientPageLocators


class LoginPage(BasePage):
    def should_fill_login_form(self):
        # проверка, что есть форма логина и объекты на ней
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not accessible"
        assert self.is_element_present(*LoginPageLocators.USER_NAME), "No field for the User's IIN"
        assert self.is_element_present(*LoginPageLocators.USER_PASS), "No field for the User's password"
        assert self.is_element_present(*LoginPageLocators.LOGIN_BTN), "No Login button"

        self.browser.find_element(*LoginPageLocators.USER_NAME).send_keys("spid.almaty")
        self.browser.find_element(*LoginPageLocators.USER_PASS).send_keys("!Q2w3e4r5t6y7")
        self.browser.find_element(*LoginPageLocators.LOGIN_BTN).click()

    def go_to_work_page(self):
        self.browser.find_element(*PatientPageLocators.PATIENT_LINK).click()
        # return PatientPage(browser=self.browser, url=self.browser.current_url)

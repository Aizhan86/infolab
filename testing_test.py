from .pages.login_page import LoginPage
from .pages.work_page import WorkPage

def login(browser):
    LOGIN_URL = "https://infolab.dec.kz/ru/account/login?next=/ru/patient/"
    login_page = LoginPage(browser, LOGIN_URL)
    login_page.open()
    login_page.should_fill_login_form()
    login_page.go_to_work_page()


# class TestLoginForm():
#     def test_presence_of_login_form(self, browser):
#         LOGIN_URL = "https://infolab.dec.kz/ru/account/login?next=/ru/patient/"
#         login_page = LoginPage(browser, LOGIN_URL)
#         login_page.open()
#         login_page.check_login_form()
#
#     def test_user_name(self, browser):
#         login_page = LoginPage(browser, browser.current_url)
#         login_page.check_user_name()
#
#     def test_user_pass(self, browser):
#         login_page = LoginPage(browser, browser.current_url)
#         login_page.check_user_pass()
#
#     def test_login_btn(self, browser):
#         login_page = LoginPage(browser, browser.current_url)
#         login_page.check_login_btn()
#
#
# class TestRegisterForm():
#     def test_register_form(self, browser):
#         login(browser)
#         work_page = WorkPage(browser, browser.current_url)
#         work_page.register_new_donor()
#
#     def test_birth_date(self, browser):
#         work_page = WorkPage(browser, browser.current_url)
#         work_page.check_birth_date()
#
#     def test_iin(self, browser):
#         work_page = WorkPage(browser, browser.current_url)
#         work_page.check_iin()
#
#     def test_surname(self, browser):
#         work_page = WorkPage(browser, browser.current_url)
#         work_page.check_surname()
#
#     def test_name(self, browser):
#         work_page = WorkPage(browser, browser.current_url)
#         work_page.check_name()
#
#     def test_middle_name(self, browser):
#         work_page = WorkPage(browser, browser.current_url)
#         work_page.check_middle_name()
#
#     def test_gender(self, browser):
#         work_page = WorkPage(browser, browser.current_url)
#         work_page.check_gender()
#
#     def test_name_in_transliteration(self, browser):
#         work_page = WorkPage(browser, browser.current_url)
#         work_page.check_name_in_transliteration()
#
#     def test_citizenship(self, browser):
#         work_page = WorkPage(browser, browser.current_url)
#         work_page.check_citizenship()
#
#     def test_name_of_country_origin(self, browser):
#         work_page = WorkPage(browser, browser.current_url)
#         work_page.check_name_of_country_origin()
#
#     def test_patient_document(self, browser):
#         work_page = WorkPage(browser, browser.current_url)
#         work_page.check_patient_document()
#
#     def test_series_of_document(self, browser):
#         work_page = WorkPage(browser, browser.current_url)
#         work_page.check_series_of_document()
#
#     def test_number_of_document(self, browser):
#         work_page = WorkPage(browser, browser.current_url)
#         work_page.check_number_of_document()
#
#     def test_country_of_living(self, browser):
#         work_page = WorkPage(browser, browser.current_url)
#         work_page.check_country_of_living()
#
#     def test_region_of_living(self, browser):
#         work_page = WorkPage(browser, browser.current_url)
#         work_page.check_region_of_living()
#
#     def test_area_unit_of_living(self, browser):
#         work_page = WorkPage(browser, browser.current_url)
#         work_page.check_area_unit_of_living()
#
#     def test_locality_of_living(self, browser):
#         work_page = WorkPage(browser, browser.current_url)
#         work_page.check_locality_of_living()
#
#     def test_street_of_living(self, browser):
#         work_page = WorkPage(browser, browser.current_url)
#         work_page.check_street_of_living()
#
#     def test_house_of_living(self, browser):
#         work_page = WorkPage(browser, browser.current_url)
#         work_page.check_house_of_living()
#
#     def test_apartment_of_living(self, browser):
#         work_page = WorkPage(browser, browser.current_url)
#         work_page.check_apartment_of_living()
#
#     def test_phone_number_of_patient(self, browser):
#         work_page = WorkPage(browser, browser.current_url)
#         work_page.check_phone_number_of_patient()
#
#     def test_mobile_number_of_patient(self, browser):
#         work_page = WorkPage(browser, browser.current_url)
#         work_page.check_mobile_number_of_patient()
#
#     def test_patient_company_name(self, browser):
#         work_page = WorkPage(browser, browser.current_url)
#         work_page.check_patient_company_name()
#
#     def test_register_save_button(self, browser):
#         work_page = WorkPage(browser, browser.current_url)
#         work_page.check_register_save_btn()
#
#
# class TestVisitsForm():
#     def test_visits_form(self, browser):
#         login(browser)
#         work_page = WorkPage(browser, browser.current_url)
#         work_page.register_new_donor()
#         work_page.register_visit()
#
#     def test_doctor_name(self, browser):
#         work_page = WorkPage(browser, browser.current_url)
#         work_page.check_doctor_name_in_visits()
#
#     def test_cabinet_number(self, browser):
#         work_page = WorkPage(browser, browser.current_url)
#         work_page.check_cabinet_number_in_visits()
#
#     def test_visits_save_button(self, browser):
#         work_page = WorkPage(browser, browser.current_url)
#         work_page.check_visits_save_btn()
#
# class TestIfaIhlaAnalysisResultsModule():
#     def test_ifa_ihla_result_module(self, browser):
#         login(browser)
#         work_page = WorkPage(browser, browser.current_url)
#         work_page.should_fill_register_form()
#         work_page.should_add_ifa_ihla()
#         work_page.should_get_samples()
#         work_page.should_send_samples_for_sorting()
#         work_page.should_switch_to_results_page()
#         work_page.should_submit_ifa_ihla_results()
#         work_page.check_results_modal()
#
# # class TestHbsagIfaAnalysisDiceModule():
# #     def test_ifa_hbsag_result_module(self, browser):
# #         login(browser)
# #         work_page = WorkPage(browser, browser.current_url)
# #         work_page.should_fill_register_form()
# #         work_page.should_add_hbsag_ifa_analysis()
# #         work_page.should_get_samples()
# #         work_page.should_send_samples_for_sorting()
# #         work_page.should_switch_to_dice_page()
# #         work_page.should_add_dice()
# #         work_page.check_dice_modal()
# #         work_page.check_save_dice_button()
#
# class TestBloodAnalysisResultsModule():
#     def test_gba_results(self, browser):
#         login(browser)
#         work_page = WorkPage(browser, browser.current_url)
#         work_page.should_fill_register_form()
#         work_page.should_add_blood_analysis()
#         work_page.should_get_samples()
#         work_page.should_send_samples_for_sorting()
#         work_page.should_switch_to_results_page()
#         work_page.should_submit_gba_results()
#         work_page.check_results_modal()
#
# class TestUrineAnalysisResultsModule():
#     def test_gua_results(self, browser):
#         login(browser)
#         work_page = WorkPage(browser, browser.current_url)
#         work_page.should_fill_register_form()
#         work_page.should_add_urine_analysis()
#         work_page.should_get_samples()
#         work_page.should_send_samples_for_sorting()
#         work_page.should_switch_to_results_page()
#         work_page.should_submit_gua_results()
#         work_page.check_results_modal()
#
# class TestBiochemistryAnalysisResultsModule():
#     def test_biochemistry_results(self, browser):
#         login(browser)
#         work_page = WorkPage(browser, browser.current_url)
#         work_page.should_fill_register_form()
#         work_page.should_add_biochemistry()
#         work_page.should_get_samples()
#         work_page.should_send_samples_for_sorting()
#         work_page.should_switch_to_results_page()
#         work_page.should_submit_biochemistry_results()
#         work_page.check_results_modal()

class TestBiochemistryAnalysisResultsRejection():
    def test_biochemistry_results(self, browser):
        login(browser)
        work_page = WorkPage(browser, browser.current_url)
        work_page.should_fill_register_form()
        work_page.should_add_biochemistry()
        work_page.should_get_samples()
        work_page.should_send_samples_for_sorting()
        work_page.should_switch_to_results_page()
        work_page.should_reject_biochemistry_results()

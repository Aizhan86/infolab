from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import RegisterPageLocators, VisitLocators, AnalysisAddLocators, ProcedurePageLocators, \
    ResultsPageLocators, SortingPageLocators, DicePageLocators
from time import sleep
from selenium.webdriver.support.ui import Select
from random import randrange
from datetime import datetime, timedelta
import random
import string


global visit_id
global referral_id
global patient_id


class WorkPage(BasePage):
    d1 = datetime.strptime('01.01.1970', '%d.%m.%Y')
    d2 = datetime.strptime('01.12.2021', '%d.%m.%Y')
    delta = d2 - d1
    int_delta = delta.days
    random_date = d1 + timedelta(randrange(int_delta))
    birthday = random_date.strftime('%d.%m.%Y')
    first_numbers = random_date.strftime('%y%m%d')
    others = random.randrange(100000, 999999)
    iin = f'{first_numbers}{others}'
    surname = ''.join(random.choices(string.ascii_uppercase, k=10))
    name = ''.join(random.choices(string.ascii_uppercase, k=5))
    midname = ''.join(random.choices(string.ascii_uppercase, k=10))
    gen_choice = random.choice(['female', 'male'])
    document_choice = random.choice(['33808b7d-3b4d-4a35-a902-76ccadf1f309', 'fa8b13f7-389b-476d-bb48-480c63df636b',
                                     '2cbdbadf-3451-45d3-b298-425fe3fb23e0', '41c2d6ff-59bc-4732-b975-39bb3a3ba233',
                                     '294167b2-7f74-4693-859b-8d451d50da7d'])

    def should_fill_register_form(self):
        self.register_new_donor()
        self.register_visit()

    def register_new_donor(self):
        # переход на страницу с регистрационной формой
        self.make(f"window.location = $('#patient-add').attr('href')")
        sleep(2)
        # автозаполнение формы регистрации
        self.make(f"{RegisterPageLocators.PATIENT_BIRTH_DATE}.val('{self.birthday}')")
        self.make(f"{RegisterPageLocators.PATIENT_IIN}.val('{self.iin}')")
        self.make(f"{RegisterPageLocators.LAB_EMPLOYEE}.click()")
        self.make(f"{RegisterPageLocators.PATIENT_SURNAME}.val('{self.surname}')")
        self.make(f"{RegisterPageLocators.PATIENT_NAME}.val('{self.name}')")
        self.make(f"{RegisterPageLocators.PATIENT_MIDDLE_NAME}.val('{self.midname}')")
        self.make(f"{RegisterPageLocators.PATIENT_GENDER}.dropdown('set selected', '{self.gen_choice}');")
        self.make(f"{RegisterPageLocators.NAME_TRANSLITERATION}.val('{self.surname} {self.name} {self.midname}')")
        self.make(f"{RegisterPageLocators.PATIENT_CITIZENSHIP}.dropdown('set selected', '2');")
        self.make(f"{RegisterPageLocators.PATIENT_COUNTRY_ORIGIN}.dropdown('set selected', 'АВСТРАЛИЯ');")
        self.make(f"{RegisterPageLocators.PATIENT_DOC}.dropdown('set selected', '{self.document_choice}');")
        self.make(f"{RegisterPageLocators.PATIENT_DOC_SERIES}.val('852')")
        self.make(f"{RegisterPageLocators.PATIENT_DOC_NUM}.val('456')")
        self.make(f"{RegisterPageLocators.COUNTRY}.dropdown('set selected', '145751');")
        self.make(f"{RegisterPageLocators.REGION}.dropdown('set selected', '4');")
        # sleep(2)
        # self.make(f"{RegisterPageLocators.AREA_UNIT}.click();")
        # sleep(1)
        # self.make(f"{RegisterPageLocators.AREA_UNIT}.dropdown('set selected', '71');")
        # sleep(1)
        # self.make(f"{RegisterPageLocators.AREA_UNIT}.dropdown('hide');")
        self.make(f"{RegisterPageLocators.LOCALITY}.val('Косшы')")
        self.make(f"{RegisterPageLocators.STREET}.val('Абай')")
        self.make(f"{RegisterPageLocators.HOUSE}.val('5')")
        self.make(f"{RegisterPageLocators.APT}.val('45')")
        self.make(f"{RegisterPageLocators.PHONE_NO}.val('87172245789')")
        self.make(f"{RegisterPageLocators.MOBILE_NO}.val('87070245789')")
        self.make(f"{RegisterPageLocators.COMPANY_NAME}.val('INFORM')")
        self.make(f"{RegisterPageLocators.REGISTER_SAVE}.click()")
        sleep(3)

    def check_birth_date(self):
        assert self.browser.execute_script(f"return {RegisterPageLocators.PATIENT_BIRTH_DATE}.length"), "Patient's birth date object is not accessible"
        assert self.browser.execute_script(f"return {RegisterPageLocators.PATIENT_BIRTH_DATE}.val()") == self.birthday, "Patient's birth date object didn't take a value"

    def check_iin(self):
        assert self.browser.execute_script(f"return {RegisterPageLocators.PATIENT_IIN}.length"), "Patient's IIN object is not accessible"
        assert self.browser.execute_script(f"return {RegisterPageLocators.PATIENT_IIN}.val()") == self.iin, "Patient's IIN object didn't take the value"

    def check_surname(self):
        assert self.browser.execute_script(f"return {RegisterPageLocators.PATIENT_SURNAME}.length"), "Patient's surname object is not accessible"
        assert self.browser.execute_script(f"return {RegisterPageLocators.PATIENT_SURNAME}.val()") == self.surname, "Patient's surname object doesn't take a value"

    def check_name(self):
        assert self.browser.execute_script(f"return {RegisterPageLocators.PATIENT_NAME}.length"), "Patient's name object is not accessible"
        assert self.browser.execute_script(f"return {RegisterPageLocators.PATIENT_NAME}.val()") == self.name, "Patient's name object doesn't take a value"

    def check_middle_name(self):
        assert self.browser.execute_script(f"return {RegisterPageLocators.PATIENT_MIDDLE_NAME}.length"), "Patient's middle name object is not accessible"
        assert self.browser.execute_script(f"return {RegisterPageLocators.PATIENT_MIDDLE_NAME}.val()") == self.midname, "Patient's  middle name object doesn't take a value"

    def check_gender(self):
        assert self.browser.execute_script(f"return {RegisterPageLocators.PATIENT_GENDER}.length"), "Patient's gender object is not accessible"
        assert self.browser.execute_script(f"return {RegisterPageLocators.PATIENT_GENDER}.find('option:selected').val()") == self.gen_choice, "Patient's gender object doesn't take a value"

    def check_name_in_transliteration(self):
        assert self.browser.execute_script(f"return {RegisterPageLocators.NAME_TRANSLITERATION}.length"), "Patient's name in transliteration object is not accessible"
        assert self.browser.execute_script(f"return {RegisterPageLocators.NAME_TRANSLITERATION}.val()") == f'{self.surname} {self.name} {self.midname}', "Patient's name in transliteration object doesn't take a value"

    def check_citizenship(self):
        assert self.browser.execute_script(f"return {RegisterPageLocators.PATIENT_CITIZENSHIP}.length"), "Patient's citizenship object is not accessible"
        assert self.browser.execute_script(f"return {RegisterPageLocators.PATIENT_CITIZENSHIP}.find('option:selected').val()") == '2', "Patient's citizenship object doesn't take a value"

    def check_name_of_country_origin(self):
        assert self.browser.execute_script(f"return {RegisterPageLocators.PATIENT_COUNTRY_ORIGIN}.length"), "The object for the name of Patient's country origin is not accessible"
        assert self.browser.execute_script(f"return {RegisterPageLocators.PATIENT_COUNTRY_ORIGIN}.find('option:selected').val()") == "АВСТРАЛИЯ", "The object for the name of Patient's country origin doesn't take a value"

    def check_patient_document(self):
        assert self.browser.execute_script(f"return {RegisterPageLocators.PATIENT_DOC}.length"), "The object for the document is not accessible"
        assert self.browser.execute_script(f"return {RegisterPageLocators.PATIENT_DOC}.find('option:selected').val()") == self.document_choice, "The object for the document doesn't take a value"

    def check_series_of_document(self):
        assert self.browser.execute_script(f"return {RegisterPageLocators.PATIENT_DOC_SERIES}.length"), "The object for the document's series is not accessible"
        assert self.browser.execute_script(f"return {RegisterPageLocators.PATIENT_DOC_SERIES}.val()") == '852', "The object for the document's series doesn't take a value"

    def check_number_of_document(self):
        assert self.browser.execute_script(f"return {RegisterPageLocators.PATIENT_DOC_NUM}.length"), "The object for the document's number is not accessible"
        assert self.browser.execute_script(f"return {RegisterPageLocators.PATIENT_DOC_NUM}.val()") == '456', "The object for the document's number doesn't take a value"

    def check_country_of_living(self):
        assert self.browser.execute_script(f"return {RegisterPageLocators.COUNTRY}.length"), "Patient's country of living object is not accessible"
        assert self.browser.execute_script(f"return {RegisterPageLocators.COUNTRY}.find('input').val()") == '145751', "Patient's country of living object doesn't take a value"

    def check_region_of_living(self):
        assert self.browser.execute_script(f"return {RegisterPageLocators.REGION}.length"), "Patient's region of living object is not accessible"
        assert self.browser.execute_script(f"return {RegisterPageLocators.REGION}.find('input').val()") == '4', "Patient's region of living object doesn't take a value"

    def check_area_unit_of_living(self):
        assert self.browser.execute_script(f"return {RegisterPageLocators.AREA_UNIT}.length"), "Patient's area unit of living object is not accessible"
        assert self.browser.execute_script(f"return {RegisterPageLocators.AREA_UNIT}.find('input').val()") == '71', "Patient's area unit of living object doesn't take a value"

    def check_locality_of_living(self):
        assert self.browser.execute_script(f"return {RegisterPageLocators.LOCALITY}.length"), "Patient's locality of living object is not accessible"
        assert self.browser.execute_script(f"return {RegisterPageLocators.LOCALITY}.val()") == 'Косшы', "Patient's locality of living object doesn't take a value"

    def check_street_of_living(self):
        assert self.browser.execute_script(f"return {RegisterPageLocators.STREET}.length"), "Patient's street object is not accessible"
        assert self.browser.execute_script(f"return {RegisterPageLocators.STREET}.val()") == 'Абай', "Patient's street object doesn't take a value"

    def check_house_of_living(self):
        assert self.browser.execute_script(f"return {RegisterPageLocators.HOUSE}.length"), "Patient's house of living object is not accessible"
        assert self.browser.execute_script(f"return {RegisterPageLocators.HOUSE}.val()") == '5', "Patient's house of living object doesn't take a value"

    def check_apartment_of_living(self):
        assert self.browser.execute_script(f"return {RegisterPageLocators.APT}.length"), "Patient's  apartment of living object is not accessible"
        assert self.browser.execute_script(f"return {RegisterPageLocators.APT}.val()") == '45', "Patient's apartment of living object doesn't take a value"

    def check_phone_number_of_patient(self):
        assert self.browser.execute_script(f"return {RegisterPageLocators.PHONE_NO}.length"), "Patient's phone number object is not accessible"
        assert self.browser.execute_script(f"return {RegisterPageLocators.PHONE_NO}.val()") == '87172245789', "Patient's phone number object doesn't take a value"

    def check_mobile_number_of_patient(self):
        assert self.browser.execute_script(f"return {RegisterPageLocators.MOBILE_NO}.length"), "Patient's mobile number object is not accessible"
        assert self.browser.execute_script(f"return {RegisterPageLocators.MOBILE_NO}.val()") == '87070245789', "Patient's mobile number object doesn't take a value"

    def check_patient_company_name(self):
        assert self.browser.execute_script(f"return {RegisterPageLocators.COMPANY_NAME}.length"), "Patient's company object is not accessible"
        assert self.browser.execute_script(f"return {RegisterPageLocators.COMPANY_NAME}.val()") == 'INFORM', "The object for Patient's company name doesn't take a value"

    def check_register_save_btn(self):
        assert self.browser.execute_script(f"return {RegisterPageLocators.REGISTER_SAVE}.length"), "No Save button for registering patients"
        # assert self.browser.current_url == "https://infolab.dec.kz/ru/queuenumber/", "Login button is not active"

    def register_visit(self):
        # регистрация визита пациента
        self.make(f"{VisitLocators.VISIT_ADD}.click()") # кликает на кнопку "Добавить визит"
        self.make(f"{VisitLocators.DOCTOR_NAME_DROPDOWN}.dropdown('set selected', 'dfdfsdf');")
        self.make(f"{VisitLocators.CABINET_NUMBER_DROPDOWN}.dropdown('set selected', '238fa20c-c417-4ac9-916e-c0e0a9e66c1b');")
        self.make(f"{VisitLocators.VISIT_SAVE}.click()")
        sleep(2)

    def should_add_ifa_ihla(self):
        # открытие окна для добавления анализа
        # self.browser.execute_script("window.scrollBy(0, 500);")
        self.make(f"{AnalysisAddLocators.ANALYSIS_ADD}.click()")
        sleep(2)
        # добавление анализа
        self.make(f"{AnalysisAddLocators.CLASSIFIER_GROUP_DROPDOWN}.dropdown('set selected', '6bad8d3e-02ca-4829-a6bd-d0110d0b2739');")
        sleep(3)
        self.make(f"{AnalysisAddLocators.CHOOSE_IFA_IHLA_CHBX}.closest('.ui.checkbox').checkbox('check')")
        self.make(f"{AnalysisAddLocators.ANALYSIS_SAVE}.click()")
        sleep(1)
        # получение id зарегистрированного пациента для осуществления дальнейших действий в других журналах
        global visit_id
        visit_id = self.browser.find_element(*AnalysisAddLocators.ANALYSIS_DATE_BTN).get_attribute("value")
        print(visit_id)
        global referral_id
        referral_id = self.browser.find_element(*AnalysisAddLocators.REFERRAL_TABLE).get_attribute("data-id")
        print(referral_id)
        global patient_id
        patient_id = self.browser.current_url.split('/')[6]
        print(patient_id)
        # button1 = self.browser.find_element(*AnalysisAddLocators.REDUCT_BTN)
        self.make(f"{AnalysisAddLocators.CLOSE_BTN}.click()")
        sleep(2)

    def should_add_hbsag_ifa_analysis(self):
        # открытие окна для добавления анализа
        # self.browser.execute_script("window.scrollBy(0, 500);")
        self.make(f"{AnalysisAddLocators.ANALYSIS_ADD}.click()")
        sleep(2)
        # добавление анализа
        self.make(f"{AnalysisAddLocators.ANALYSIS_GROUP_CHBX}.click()")
        sleep(5)
        self.make(f"{AnalysisAddLocators.CLASSIFIER_DD}.dropdown('set selected', 'c3c9e575-2f8a-4f67-8410-f9de80519d60');")
        sleep(3)
        self.make(f"{AnalysisAddLocators.ANALYSIS_SAVE}.click()")
        sleep(1)
        # получение id зарегистрированного пациента для осуществления дальнейших действий в других журналах
        global visit_id
        visit_id = self.browser.find_element(*AnalysisAddLocators.ANALYSIS_DATE_BTN).get_attribute("value")
        print(visit_id)
        global referral_id
        referral_id = self.browser.find_element(*AnalysisAddLocators.REFERRAL_TABLE).get_attribute("data-id")
        print(referral_id)
        global patient_id
        patient_id = self.browser.current_url.split('/')[6]
        print(patient_id)
        # button1 = self.browser.find_element(*AnalysisAddLocators.REDUCT_BTN)
        self.make(f"{AnalysisAddLocators.CLOSE_BTN}.click()")
        sleep(2)

    def should_add_blood_analysis(self):
        # открытие окна для добавления анализа
        # self.browser.execute_script("window.scrollBy(0, 500);")
        self.make(f"{AnalysisAddLocators.ANALYSIS_ADD}.click()")
        sleep(2)
        # добавление анализа
        self.make(f"{AnalysisAddLocators.ANALYSIS_TYPE}.dropdown('set selected', 'contract');")
        self.make(f"{AnalysisAddLocators.CLASSIFIER_GROUP_DROPDOWN}.dropdown('set selected', '04b2311b-a744-4d50-a590-21b8b4eac9fe');")
        sleep(3)
        self.make(f"{AnalysisAddLocators.CHOOSE_OAK_CHBX}.closest('.ui.checkbox').checkbox('check')")
        self.make(f"{AnalysisAddLocators.ANALYSIS_SAVE}.click()")
        sleep(1)
        # получение id зарегистрированного пациента для осуществления дальнейших действий в других журналах
        global visit_id
        visit_id = self.browser.find_element(*AnalysisAddLocators.ANALYSIS_DATE_BTN).get_attribute("value")
        print(visit_id)
        global referral_id
        referral_id = self.browser.find_element(*AnalysisAddLocators.REFERRAL_TABLE).get_attribute("data-id")
        print(referral_id)
        global patient_id
        patient_id = self.browser.current_url.split('/')[6]
        print(patient_id)
        # button1 = self.browser.find_element(*AnalysisAddLocators.REDUCT_BTN)
        self.make(f"{AnalysisAddLocators.CLOSE_BTN}.click()")
        sleep(2)

    def should_add_urine_analysis(self):
        # открытие окна для добавления анализа
        # self.browser.execute_script("window.scrollBy(0, 500);")
        self.make(f"{AnalysisAddLocators.ANALYSIS_ADD}.click()")
        sleep(2)
        # добавление анализа
        self.make(f"{AnalysisAddLocators.ANALYSIS_TYPE}.dropdown('set selected', 'paid');")
        self.make(f"{AnalysisAddLocators.CLASSIFIER_GROUP_DROPDOWN}.dropdown('set selected', '7908a604-b5f2-4ea6-b903-add7d7812653');")
        sleep(3)
        self.make(f"{AnalysisAddLocators.CHOOSE_OAM_CHBX}.closest('.ui.checkbox').checkbox('check')")
        self.make(f"{AnalysisAddLocators.ANALYSIS_SAVE}.click()")
        sleep(1)
        # получение id зарегистрированного пациента для осуществления дальнейших действий в других журналах
        global visit_id
        visit_id = self.browser.find_element(*AnalysisAddLocators.ANALYSIS_DATE_BTN).get_attribute("value")
        print(visit_id)
        global referral_id
        referral_id = self.browser.find_element(*AnalysisAddLocators.REFERRAL_TABLE).get_attribute("data-id")
        print(referral_id)
        global patient_id
        patient_id = self.browser.current_url.split('/')[6]
        print(patient_id)
        # button1 = self.browser.find_element(*AnalysisAddLocators.REDUCT_BTN)
        self.make(f"{AnalysisAddLocators.CLOSE_BTN}.click()")
        sleep(2)

    def should_add_biochemistry(self):
        # открытие окна для добавления анализа
        # self.browser.execute_script("window.scrollBy(0, 500);")
        self.make(f"{AnalysisAddLocators.ANALYSIS_ADD}.click()")
        sleep(2)
        # добавление анализа
        self.make(f"{AnalysisAddLocators.ANALYSIS_TYPE}.dropdown('set selected', 'agreed');")
        self.make(f"{AnalysisAddLocators.CLASSIFIER_GROUP_DROPDOWN}.dropdown('set selected', 'ae231b40-89ed-4e39-ab0a-e05ecd7e3613');")
        sleep(3)
        self.make(f"{AnalysisAddLocators.CHOOSE_A_APOLIPOPROTEN_CHBX}.closest('.ui.checkbox').checkbox('check')")
        self.make(f"{AnalysisAddLocators.ANALYSIS_SAVE}.click()")
        sleep(1)
        # получение id зарегистрированного пациента для осуществления дальнейших действий в других журналах
        global visit_id
        visit_id = self.browser.find_element(*AnalysisAddLocators.ANALYSIS_DATE_BTN).get_attribute("value")
        print(visit_id)
        global referral_id
        referral_id = self.browser.find_element(*AnalysisAddLocators.REFERRAL_TABLE).get_attribute("data-id")
        print(referral_id)
        global patient_id
        patient_id = self.browser.current_url.split('/')[6]
        print(patient_id)
        # button1 = self.browser.find_element(*AnalysisAddLocators.REDUCT_BTN)
        self.make(f"{AnalysisAddLocators.CLOSE_BTN}.click()")
        sleep(2)

    def should_get_samples(self):
        self.should_switch_to_procedure_page()
        self.should_get_biomaterial()
        # self.should_check_color_of_label()

    def should_switch_to_procedure_page(self):
        # переход в журнал "Процедурный кабинет"
        self.make(f"window.location = $('#journal_procedure_cab').attr('href')")
        # assert self.is_element_present(*ProcedurePageLocators.PROCEDURE_LINK), \
           # "Incorrect link to Procedure cabinet journal"

    def should_get_biomaterial(self):
        # открывает окно для приглашения пациента и отмечает, что биоматериал забран
        sleep(3)
        self.make(f"$('a[data-procedure_id={referral_id}]').click();")  # приглашение пацента для забора биоматериала
        sleep(2)
        self.make(f"{ProcedurePageLocators.CHECKBOX_GET_MATERIAL}.click()")  # отмечает, что материал забран
        self.make(f"{ProcedurePageLocators.INVITATION_SAVE_BTN}.click()")  # сохранение данных и закрытие окна
        sleep(2)

    def should_send_samples_for_sorting(self):
        self.should_switch_to_sorting_page()
        self.send_samples_for_sorting()

    def should_switch_to_sorting_page(self):
        # переход в журнал "Сортировка"
        self.make(f"window.location = $('#journal_sorting').attr('href')")
        # assert self.is_element_present(*SortingPageLocators.SORTING_LINK), \
        # "Incorrect link for Sorting journal"
        sleep(2)

    def send_samples_for_sorting(self):
        self.make(f"""$('a[data-id="{referral_id}"][title="Отправить биоматериал"]').click();""")
        sleep(2)
        self.make(f"$('#id_department_id').dropdown('set selected', '2ce16f7d-765a-4ed0-acdb-59dc79b71c2f')")
        self.make(f"{SortingPageLocators.SEND_BTN}.click()")
        sleep(2)

    def should_switch_to_results_page(self):
        # переход в журнал "Результаты"
        self.make(f"window.location = $('#journal_results').attr('href')")
        sleep(3)
        # assert self.is_element_present(*SortingPageLocators.SORTING_LINK), \
            #"Incorrect link for Results journal"

    def should_submit_ifa_ihla_results(self):
        self.browser.get(f"https://infolab.dec.kz/ru/analysis/results/{patient_id}/all?encounter={visit_id}")
        sleep(2)
        self.make(f"""$('div[data-id="{referral_id}"]').click();""")
        sleep(3)
        self.make(f"{ResultsPageLocators.RESULT_IFA}.dropdown('set selected', 'Отрицательный');")
        self.make(f"{ResultsPageLocators.NOTE_IFA}.val('Good')")
        self.make(f"{ResultsPageLocators.RESULT_IFA_NOTE}.val('10')")
        self.make(f"{ResultsPageLocators.KHILEZ_CHECKBOX}.click()")
        self.make(f"{ResultsPageLocators.HEMOLYSIS_CHECKBOX}.click()")
        self.make(f"{ResultsPageLocators.ANOTHER_CHECKBOX}.click()")
        self.make(f"{ResultsPageLocators.CONFIRM_CHECKBOX_RES}.click()")
        self.make(f"{ResultsPageLocators.RESULT_SAVE}.click()")
        sleep(2)
        self.browser.execute_script(f"window.location = $('#buttons_div a').attr('href')")
        sleep(2)

    def check_ifa_ihla_results(self):
        assert self.browser.execute_script(f"return $('#gridContainer').dxDataGrid('instance').getDataSource().items().filter((e) => e.encounter_id == '{visit_id}')[0].status_code") == 5, "Результат не проставлен"

    def should_submit_gba_results(self):
        self.browser.get(f"https://infolab.dec.kz/ru/analysis/results/{patient_id}/all?encounter={visit_id}")
        sleep(2)
        self.make(f"""$('div[data-id="{referral_id}"]').click();""")
        sleep(3)
        self.make(f"{ResultsPageLocators.LEUKOCYTES}.val('10')")
        self.make(f"{ResultsPageLocators.ERYTHROCYTES}.val('4')")
        self.make(f"{ResultsPageLocators.HEMOGLOBIN}.val('120')")
        self.make(f"{ResultsPageLocators.NOTES_GBA}.val('Good')")
        self.make(f"{ResultsPageLocators.CONFIRM_CHECKBOX_RES}.click()")
        self.make(f"{ResultsPageLocators.RESULT_SAVE}.click()")
        sleep(2)
        self.browser.execute_script(f"window.location = $('#buttons_div a').attr('href')")
        sleep(2)
        assert self.browser.execute_script(f"return $('#gridContainer').dxDataGrid('instance').getDataSource().items().filter((e) => e.encounter_id == '{visit_id}')[0].status_code") == 5, "Результат не проставлен"
        # assert self.browser.find_element(By.ID, 'confirm-results')  # проверка, Результат анализа проставлен

    def should_submit_gua_results(self):
        self.browser.get(f"https://infolab.dec.kz/ru/analysis/results/{patient_id}/all?encounter={visit_id}")
        sleep(2)
        self.make(f"""$('div[data-id="{referral_id}"]').click();""")
        sleep(3)
        self.make(f"{ResultsPageLocators.AMOUNT}.val('100')")
        self.make(f"{ResultsPageLocators.COLOR}.val('YELLOW')")
        self.make(f"{ResultsPageLocators.YEAST}.click()")
        self.make(f"{ResultsPageLocators.NOTE_GUA}.val('Good')")
        self.make(f"{ResultsPageLocators.CONFIRM_CHECKBOX_RES}.click()")
        self.make(f"{ResultsPageLocators.RESULT_SAVE}.click()")
        sleep(2)
        self.browser.execute_script(f"window.location = $('#buttons_div a').attr('href')")
        sleep(2)
        assert self.browser.execute_script(f"return $('#gridContainer').dxDataGrid('instance').getDataSource().items().filter((e) => e.encounter_id == '{visit_id}')[0].status_code") == 5, "Результат не проставлен"

    def should_submit_biochemistry_results(self):
        self.browser.get(f"https://infolab.dec.kz/ru/analysis/results/{patient_id}/all?encounter={visit_id}")
        sleep(2)
        self.make(f"""$('div[data-id="{referral_id}"]').click();""")
        sleep(3)
        self.make(f"{ResultsPageLocators.CONCENTRATION}.val('100')")
        self.make(f"{ResultsPageLocators.NOTES_BIOCHEMISTRY}.val('Good')")
        self.make(f"{ResultsPageLocators.CONFIRM_CHECKBOX_RES}.click()")
        self.make(f"{ResultsPageLocators.RESULT_SAVE}.click()")
        sleep(2)
        self.browser.execute_script(f"window.location = $('#buttons_div a').attr('href')")
        sleep(2)
        assert self.browser.execute_script(f"return $('#gridContainer').dxDataGrid('instance').getDataSource().items().filter((e) => e.encounter_id == '{visit_id}')[0].status_code") == 5, "Результат не проставлен"

    def should_switch_to_dice_page(self):
        # переход в журнал "Плашки"
        self.make(f"window.location = $('#journal_plashki').attr('href')")
        sleep(3)
        # assert self.is_element_present(*DicePageLocators.SORTING_LINK), \
        # "Incorrect link for Dice journal"

    numbers3 = ''.join(random.choices(string.digits, k=3))
    numbers4 = ''.join(random.choices(string.digits, k=4))

    def should_add_dice(self):
        # Добавить плашки
        self.make(f"{DicePageLocators.DICE_ADD_BTN}.click()")
        sleep(2)
        self.make(f"{DicePageLocators.ANALYSIS_TYPE}.dropdown('set selected', 'B06.125.005');")
        # self.make(f"{DicePageLocators.ANALYSIS_TYPE}.dropdown('set selected', 'B06.855.005');")
        self.make(f"{DicePageLocators.TUBE_TYPE}.dropdown('set selected', 'free');")
        self.make(f"{DicePageLocators.PATIENTS_WITH_IB}.click()")
        self.browser.find_element(*DicePageLocators.DICE_OK_BTN).click()
        sleep(2)
        self.make(f"{DicePageLocators.ADDITIONAL_NUM}.val('{self.numbers3}')")
        self.make(
            f"{DicePageLocators.TEST_SYSTEM_TYPE}.dropdown('set selected', '34a78353-7b70-4fd7-9e8b-b992d9104bdb');")
        self.make(f"{DicePageLocators.SERIES}.val('{self.numbers4}')")
        sleep(2)
        self.make(f"{DicePageLocators.PERIOD}.click()")
        self.make(f"{DicePageLocators.DICE_ORG}.dropdown('set selected', '1d880468-58a4-4056-b571-68e713beab71');")
        self.make(f"{DicePageLocators.APPLY_BTN}.click()")
        sleep(2)
        self.make(f"$('#dice_list_adding_tubes div[data-request_id={referral_id}] .ui.checkbox input').click();")  # выбираем пробирку для перемещения на плашку
        self.make(f"{DicePageLocators.REPLACE}.click()")  # перемещаем выбранную пробирку
        sleep(5)
        # проверка, находится ли пробирка на плашке
        assert self.browser.execute_script(f"return {DicePageLocators.DICE_A1}.val()") == f"{referral_id}", "The tube is not in dice"
        # assert self.browser.find_element(*DicePageLocators.DICE_A1).get_attribute("value") == f"{referral_id}", "The tube is not in dice"
        self.make(f"{DicePageLocators.DICE_SAVE_BTN}.click()")









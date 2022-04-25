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
    def should_fill_register_form(self):
        self.should_switch_to_register_page()
        self.register_new_donor()
        self.register_visit()
        self.open_window_for_adding_analysis()

    def should_switch_to_register_page(self):
        # переход на страницу с регистрационной формой
        assert self.is_element_present(*RegisterPageLocators.REGISTER_LINK), "Incorrect link to Patient registration"
        self.browser.find_element(*RegisterPageLocators.REGISTER_LINK).click()

    def register_new_donor(self):
        # автозаполнение формы регистрации
        d1 = datetime.strptime('01.01.1970', '%d.%m.%Y')
        d2 = datetime.strptime('01.12.2021', '%d.%m.%Y')
        delta = d2 - d1
        int_delta = delta.days
        random_date = d1 + timedelta(randrange(int_delta))
        birthday = random_date.strftime('%d.%m.%Y')
        self.browser.find_element(*RegisterPageLocators.PATIENT_BIRTH_DATE).send_keys(birthday)
        first_numbers = random_date.strftime('%y%m%d')
        others = random.randrange(100000, 999999)
        iin = f'{first_numbers}{others}'
        self.browser.find_element(*RegisterPageLocators.PATIENT_IIN).send_keys(iin)
        surname = ''.join(random.choices(string.ascii_uppercase, k=10))
        self.browser.find_element(*RegisterPageLocators.PATIENT_SURNAME).send_keys(surname)
        name = ''.join(random.choices(string.ascii_uppercase, k=5))
        self.browser.find_element(*RegisterPageLocators.PATIENT_NAME).send_keys(name)
        gen_choice = random.choice(['female', 'male'])
        self.make(f"{RegisterPageLocators.PATIENT_GENDER_DROPDOWN}.dropdown('set selected', '{gen_choice}');")
        # cit_choice = random.choice(["1", "2", "3", "4"])
        Select(self.browser.find_element(*RegisterPageLocators.PATIENT_CITIZENSHIP)).select_by_value("1")
        self.browser.find_element(*RegisterPageLocators.REGISTER_SAVE_BTN).click()
        sleep(3)

    def register_visit(self):
        # регистрация визита пациента
        visit_button = self.browser.find_element(*VisitLocators.VISIT_ADD_BTN) # поиск кнопки "Добавить визит"
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", visit_button) # скролит экран до кнопки "Добавить визит"
        visit_button.click() # кликает на кнопку "Добавить визит"
        self.make(f"{VisitLocators.DOCTOR_NAME_DROPDOWN}.dropdown('set selected', 'dfdfsdf');")
        self.make(f"{VisitLocators.CABINET_NUMBER_DROPDOWN}.dropdown('set selected', '238fa20c-c417-4ac9-916e-c0e0a9e66c1b');")
        self.browser.execute_script("window.scrollBy(0, 500);")
        self.browser.find_element(*VisitLocators.VISIT_SAVE_BTN).click()
        sleep(3)

    def open_window_for_adding_analysis(self):
        # открытие окно для добавления анализа
        self.browser.execute_script("window.scrollBy(0, 500);")
        self.make(f"{AnalysisAddLocators.ANALYSIS_ADD}.click()")

    def should_add_ifa_ihla(self):
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
        self.browser.find_element(*AnalysisAddLocators.CLOSE_BTN).click()
        sleep(2)

    def should_add_hbsag_ifa_analysis(self):
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
        self.browser.find_element(*AnalysisAddLocators.CLOSE_BTN).click()
        sleep(2)

    def should_add_blood_analysis(self):
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
        self.browser.find_element(*AnalysisAddLocators.CLOSE_BTN).click()
        sleep(2)

    def should_add_urine_analysis(self):
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
        self.browser.find_element(*AnalysisAddLocators.CLOSE_BTN).click()
        sleep(2)

    def should_add_biochemistry(self):
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
        self.browser.find_element(*AnalysisAddLocators.CLOSE_BTN).click()
        sleep(2)

    def should_get_samples(self):
        self.should_switch_to_procedure_page()
        self.should_get_biomaterial()
        # self.should_check_color_of_label()

    def should_switch_to_procedure_page(self):
        # переход в журнал "Процедурный кабинет"
        self.browser.find_element(*ProcedurePageLocators.PROCEDURE_LINK).click()
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
        assert self.browser.find_element(By.ID, 'confirm-results') # проверка, Результат анализа проставлен

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
        assert self.browser.find_element(By.ID, 'confirm-results')  # проверка, Результат анализа проставлен

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
        assert self.browser.find_element(By.ID, 'confirm-results')  # проверка, Результат анализа проставлен

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
        assert self.browser.find_element(By.ID, 'confirm-results')  # проверка, Результат анализа проставлен

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
        assert self.browser.find_element(*DicePageLocators.DICE_A1).get_attribute("value") == f"{referral_id}", "The tube is not in dice"
        self.make(f"{DicePageLocators.DICE_SAVE_BTN}.click()")









from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    LOGIN_URL = "https://infolab.dec.kz/ru/account/login?next=/ru/patient/"
    LOGIN_LINK = "https://infolab.dec.kz/ru/account/login?next=/ru/patient/"
    LOGIN_FORM = (By.CSS_SELECTOR, 'form[name="form"]')
    USER_NAME = (By.ID, "identification")
    USER_PASS = (By.ID, "password")
    LOGIN_BTN = (By.ID, "entrance")

class PatientPageLocators(object):
    PATIENT_URL = "https://infolab.dec.kz/ru/patient/"
    PATIENT_LINK = (By.CSS_SELECTOR, 'a[href="/ru/patient/"]')

class RegisterPageLocators(object):
    REGISTER_LINK = (By.CSS_SELECTOR, 'a[href="/ru/patient/add"]')
    PATIENT_IIN = (By.NAME, "iin")
    PATIENT_SURNAME = (By.CSS_SELECTOR, 'input[name="last_name"]')
    PATIENT_NAME = (By.CSS_SELECTOR, 'input[name="first_name"]')
    PATIENT_BIRTH_DATE = (By.CSS_SELECTOR, 'input[name="birthDate"]')
    PATIENT_GENDER_DROPDOWN = "$('form[name=form-add-patient] div[data-field=patient__gender] .ui.dropdown')"
    PATIENT_CITIZENSHIP = (By.CSS_SELECTOR, 'select[name="citizenship_id"]')
    REGISTER_SAVE_BTN = (By.ID, "save_patient_id")

class VisitLocators(object):
    VISIT_ADD_BTN = (By.ID, "visit_add")
    DOCTOR_NAME_DROPDOWN = "$('form[name=form-add-visit] div[data-field=visit__individual_id] .ui.dropdown')"
    CABINET_NUMBER_DROPDOWN = "$('form[name=form-add-visit] div[data-field=visit__cab_number_id] .ui.dropdown')"
    VISIT_SAVE_BTN = (By.CSS_SELECTOR, "#windowAddVisit .actions .ui.ok.green.button.visual")


class AnalysisAddLocators(object):
    ANALYSIS_ADD = "$('#add_analysis')"
    ANALYSIS_TYPE = "$('#windowProcedure div[data-field=analyse_type] .ui.dropdown')"
    ANALYSIS_GROUP_CHBX ="$('#windowProcedure div[data-field=is_pre_test_counseling] .ui.checkbox')"
    CLASSIFIER_DD = "$('#windowProcedure div[data-field=classifier_id] .ui.dropdown')"
    CLASSIFIER_GROUP_DROPDOWN = "$('#windowProcedure div[data-field=classifier_group] .ui.dropdown')"
    CHOOSE_IFA_IHLA_CHBX = "$('div[data-field=classifier_block] .ui.table.study-list .classifier_often_used_body tr[data-value=e6306d2c-d53a-434b-8030-46eba52f0dac] input]')"
    CHOOSE_OAK_CHBX = "$('div[data-field=classifier_block] .ui.table.study-list .classifier_often_used_body tr[data-value=cc7231ba-07b7-45a3-9d97-6c622fad90a2] input')"
    CHOOSE_OAM_CHBX = "$('div[data-field=classifier_block] .ui.table.study-list .classifier_often_used_body tr[data-value=6ca6f3b1-677d-4c36-bf1a-2b9f6316b58a] input')"
    CHOOSE_A_APOLIPOPROTEN_CHBX = "$('div[data-field=classifier_block] .ui.table.study-list .classifier_often_used_body tr[data-value=1689e775-6caa-463f-ad84-d8f7c607050c] input')"
    ANALYSIS_SAVE = "$('#windowProcedure .actions .ok.green.button')"
    ANALYSIS_DATE_BTN = (By.CSS_SELECTOR, 'div[class="content"] input[name=id]')
    REFERRAL_TABLE = (By.CSS_SELECTOR, 'table.ui.attached.celled.table tbody.table-analisis-list tr')
    REDUCT_BTN = (By.CSS_SELECTOR, 'div[onclick="$(this).editAnalisis()"]')
    CLOSE_BTN = (By.ID, "close_patient")

class ProcedurePageLocators(object):
    PROCEDURE_URL = "https://infolab.dec.kz/ru/procedure_cab_index"
    PROCEDURE_LINK = (By.CSS_SELECTOR, 'a[href="/ru/procedure_cab_index"]')
    CHECKBOX_GET_MATERIAL = "$('div[data-field=CheckBoxGetMaterial]')"
    INVITATION_SAVE_BTN = "$('.modal.top.aligned.scrolling.front.transition .approve.green.button')"

class SortingPageLocators(object):
    SORTING_URL = "https://infolab.dec.kz/ru/analysis/sorting"
    SORTING_LINK = "$('a[href=/ru/analysis/sorting]')"
    OPEN_SORT_BTN = (By.CSS_SELECTOR, 'a[onclick="$(this).sendSelected();"]')
    SEND_BIOMAT_BTN = (By.CLASS_NAME, '.write.icon')
    CHOOSE_LAB = "$('form[name=form-send-biomaterial] div[data-field=analysis__department_id]')"
    SEND_BTN = "$('#windowSendBiomaterial .ok.green.button')"
    JOURNALS_BTN = (By.CSS_SELECTOR, 'i[class="ellipsis horizontal icon"]')

class ProtocolUploadPageLocators(object):
    RESULTS_URL = "https://infolab.dec.kz/ru/analysis/results"
    RESULTS_LINK = (By.CSS_SELECTOR, 'a[href="/ru/equipment_upload"]')


class ResultsPageLocators(object):
    RESULTS_URL = "https://infolab.dec.kz/ru/analysis/results"
    RESULTS_LINK = "$('a[href=/ru/analysis/results]')"

    RESULT_IFA = "$('div[data-field=testing__e6306d2c_d53a_434b_8030_46eba52f0dac] .ui.dropdown')"
    NOTE_IFA = "$('div[data-field=testing__934c7675_e4d6_479d_9b3d_bfc05ed49f9d] input')"
    RESULT_IFA_NOTE = "$('div[data-field=testing__372eded2_7bf0_481e_9d1d_b8cc1dc01924] input')"
    KHILEZ_CHECKBOX = "$('div[data-field=testing__a240deaa_b2f2_4547_b4eb_247d80811b96] .ui.checkbox')"
    HEMOLYSIS_CHECKBOX = "$('div[data-field=testing__c32c6b5f_2c97_4467_b295_6426ec9fcdc1] .ui.checkbox')"
    ANOTHER_CHECKBOX = "$('div[data-field=testing__769d9b8d_9f31_4172_b989_e149337730e5] .ui.checkbox')"
    CONFIRM_CHECKBOX_RES = "$('div[data-field=testing__check_analyze] .ui.checkbox')"

    AMOUNT = "$('div[data-field=testing__6ca6f3b1_677d_4c36_bf1a_2b9f6316b58a] input')"
    COLOR = "$('div[data-field=testing__77d881c7_ecd1_4994_9dba_aabfe162ec13] input')"
    YEAST = "$('div[data-field=testing__d1826c16_f0f5_4adf_995a_cc86a5acc4eb] .ui.checkbox')"
    NOTE_GUA = "$('div[data-field=testing__482a5b04_beb8_4f46_bc4b_734c96190359] input')"

    LEUKOCYTES = "$('div[data-field=testing__cc7231ba_07b7_45a3_9d97_6c622fad90a2] input')"
    ERYTHROCYTES = "$('div[data-field=testing__32c4b30f_ecd8_4163_80b2_fe2e8b6c9cfb] input')"
    HEMOGLOBIN = "$('div[data-field=testing__ffaa0b37_6960_4f8d_9347_ca034508066b] input')"
    NOTES_GBA = "$('div[data-field=testing__5041e5a4_41ec_43a4_aebe_fe5ce9266f5c] input')"

    CONCENTRATION = "$('div[data-field=testing__1689e775_6caa_463f_ad84_d8f7c607050c] input')"
    NOTES_BIOCHEMISTRY = "$('div[data-field=testing__42d7c036_21bb_4241_8c01_f73eeae1edf8] input')"

    REQUEST_BTN = (By.CLASS_NAME, ".file.medical.icon")
    RESULT_1 = "$('div[data-field=testing_res1] .ui.dropdown')"
    RESULT_2 = "$('div[data-field=testing_res2] .ui.dropdown')"
    RESULT_3 = "$('div[data-field=testing_res3] .ui.dropdown')"
    RESULT_4 = "$('div[data-field=testing_res4] .ui.dropdown')"
    CHECKBOX_CONFIRM_RES2 = (By.CSS_SELECTOR, 'input[name="testing__check_analyze_confirming"]')
    RESULT_SAVE = "$('#windowTesting .ok.green.button')"
    RESULT_CLOSE = "$('#buttons_div a')"

class DicePageLocators(object):
    DICE_URL = "https://infolab.dec.kz/ru/dice/"
    DICE_LINK = (By.ID, "journal_plashki")
    DICE_ADD_BTN = "$('#dice-add')"
    ANALYSIS_TYPE = "$('div[data-field=dice__type_analyzes] .ui.dropdown')"
    TUBE_TYPE = "$('div[data-field=dice__tube_type] .ui.dropdown')"
    PATIENTS_WITH_IB = "$('div[data-field=dice__is_immunoblot] .ui.checkbox input')"
    DICE_OK_BTN = (By.CSS_SELECTOR, "#windowParametersAddDice .ok.green.button")
    ADDITIONAL_NUM = "$('div[data-field=dice__number_add] input')"
    TEST_SYSTEM_TYPE = "$('div[data-field=dice__type_test_system] .ui.dropdown')"
    SERIES = "$('div[data-field=dice__serial] input')"
    PERIOD = "$('div.ui.dice-filter a.ui.text.border.dotted.italic')"
    DICE_ORG = "$('div[data-field=dice_filter__orgs] .ui.dropdown')"
    APPLY_BTN = "$('#windowFilter .ok.green.button')"
    REPLACE = "$('#move_div')"
    TUBE_DRAGGABLE = (By.CLASS_NAME, '.item.dice.drag.drop.visual')
    DICE_A1 = (By.CSS_SELECTOR, '#node_dice_1 input[name=dice-1-request_id]')
    DICE_SAVE_BTN = "$('#save_form')"
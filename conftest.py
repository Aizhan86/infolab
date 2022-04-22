import pytest
import sentry_sdk
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")

    sentry_sdk.init(
        "https://974bf7b634a249f2bf3324d1d4e4387b@debug.ico.kz/27",
        traces_sample_rate=1.0,
    )
    browser = webdriver.Remote(desired_capabilities=DesiredCapabilities.CHROME, command_executor="http://127.0.0.1:4444/wd/hub")
    # browser = webdriver.Remote(desired_capabilities=DesiredCapabilities.CHROME, command_executor="http://172.18.0.1:4444/wd/hub")
    # browser = webdriver.Chrome(service=Service('C:/Work/tools/chromedriver/chromedriver.exe'))
    # browser.maximize_window()

    # pytest --dist=loadscope --tx 2*popen//python=python3.10 -n 2 --reruns 2 --only-rerun JavascriptException --only-rerun ElementClickInterceptedException testing_test.py

    yield browser
    print("\nquit browser..")
    browser.quit()


import pytest
import sentry_sdk
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")

    sentry_sdk.init(
        "https://66b5be3a02ea4c4c844821a44ab86204@debug.ico.kz/12",
        traces_sample_rate=1.0,
    )

    caps = DesiredCapabilities().CHROME
    # caps["pageLoadStrategy"] = "none"
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument('headless')
    # browser = webdriver.Remote(command_executor="http://127.0.0.1:4444/wd/hub", desired_capabilities=caps, options=options)

    browser = webdriver.Remote(command_executor="http://172.18.0.1:4444/wd/hub", desired_capabilities=caps, options=options)

    # browser = webdriver.Chrome(service=Service('C:/Work/tools/chromedriver/chromedriver.exe'))
    # browser.maximize_window()

    # pytest --dist=loadscope --tx 8*popen//python=python3.10 -n 8 --reruns 1 --only-rerun JavascriptException --only-rerun ElementClickInterceptedException testing_test.py

    yield browser
    print("\nquit browser..")
    browser.quit()


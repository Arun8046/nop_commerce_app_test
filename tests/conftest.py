import pytest
from selenium import webdriver
from utilities.custom_logger import log_gen
logger = log_gen.loggen()


@pytest.fixture()
def setUp(browser):

    if browser=='chrome':
        driver = webdriver.Chrome(executable_path='C:\\Users\\sas\\Downloads\\chromedriver.exe')
        logger.info("*** Launching Chrome Browser ***")
    elif browser=='firefox':
        driver = webdriver.Chrome(executable_path='C:\\Users\\sas\\Downloads\\chromedriver.exe')
        logger.info("*** Launching firefox Browser ***")
    else:
        driver = webdriver.Chrome(executable_path='C:\\Users\\sas\\Downloads\\chromedriver.exe')
        logger.info("*** Launching IE Browser ***")
    return driver


def pytest_addoption(parser):
    """This will get value from cli"""
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    """This will return the browser value to setup"""
    return request.config.getoption("--browser")


""" Pytest HTML report generation"""

def pytest_configure(config):
    """
    It is hook for adding envrionment info
    """
    config._metadata['Project Name'] = 'NOP Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Arun Bhilare'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    """ it will delete/modify environment info"""
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
from pageObjects.login_page import login_page
import pytest
from selenium import webdriver
from utilities.read_properties import read_props
from utilities.custom_logger import log_gen

class Test_login:
    baseUrl = read_props.get_url()
    username = read_props.get_username()
    password = read_props.get_password()
    logger = log_gen.loggen()

    @pytest.mark.sanity
    def test_verify_home_page_title(self,setUp):
        self.driver = setUp
        self.logger.info("*** test_verify_home_page_title Execution Started***")
        self.logger.info("*** Initiated Browser ***")
        self.logger.info((self.baseUrl))
        self.driver.get(self.baseUrl)
        actual_title = self.driver.title


        if actual_title == "Your store. Login":

            self.driver.close()
            assert True
            self.logger.info("*** test_verify_home_page_title passed ***")
        else:
            self.driver.save_screenshot(".\\screenshots\\"+"test_verify_home_page_title.png")
            self.driver.close()
            self.logger.info("*** test_verify_home_page_title failed ***")
            assert False

    @pytest.mark.sanity
    def test_verify_login_with_valid_creds(self,setUp):
        self.driver = setUp
        self.logger.info("*** test_verify_login_with_valid_creds Execution Started ***")
        self.driver.get(self.baseUrl)
        self.lp = login_page(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        actual_title = self.driver.title

        if actual_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("*** test_verify_login_with_valid_creds passed ***")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\"+"test_verify_login_with_valid_creds.png")
            self.driver.close()
            self.logger.info("*** test_verify_login_with_valid_creds failed ***")
            assert False
import time

from pageObjects.login_page import login_page
import pytest
from selenium import webdriver
from utilities.read_properties import read_props
from utilities.custom_logger import log_gen
from utilities import xl_utils

class Test_login_invalid:
    baseUrl = read_props.get_url()
    path=".//testData/LoginData.xlsx"
    logger = log_gen.loggen()

    @pytest.mark.regression
    def test_verify_login_with_invalid_creds(self,setUp):
        self.driver = setUp
        self.logger.info("*** test_verify_login_with_invalid_creds Execution Started ***")
        self.driver.get(self.baseUrl)
        self.lp = login_page(self.driver)

        self.rows = xl_utils.getRowCount(self.path,'Sheet1')
        lst_status = []
        for r in range(2,self.rows+1):
            time.sleep(5)
            self.user =xl_utils.readData(self.path,'Sheet1',r,1)
            self.password = xl_utils.readData(self.path, 'Sheet1', r, 2)
            self.exp_result = xl_utils.readData(self.path, 'Sheet1', r, 3)

            self.lp.set_username(self.user)
            self.lp.set_password(self.password)
            self.lp.click_login()
            time.sleep(5)
            actual_title = self.driver.title

            if actual_title == "Dashboard / nopCommerce administration":
                if self.exp_result == "Pass":
                    self.logger.info("*** test_verify_login_with_valid_creds passed ***")
                    self.lp.click_logout()
                    lst_status.append("Pass")

                elif self.exp_result == "Fail":
                    self.logger.info("*** test_verify_login_with_valid_creds failed ***")
                    lst_status.append("Fail")
                    self.driver.save_screenshot(".\\screenshots\\" + "test_verify_login_with_valid_creds.png")
            elif actual_title != "Dashboard / nopCommerce administration":
                if self.exp_result == "Pass":
                    self.logger.info("*** test_verify_login_with_valid_creds failed ***")
                    lst_status.append("Fail")
                    self.driver.save_screenshot(".\\screenshots\\" + "test_verify_login_with_valid_creds.png")
                elif self.exp_result == "Fail":
                    self.logger.info("*** test_verify_login_with_valid_creds Passed ***")
                    lst_status.append("Pass")


        if "Fail" not in lst_status:
            self.logger.info("Login test with multiple creds passed")
            self.driver.close()
            assert True
        else:
            self.logger.info("Login test with multiple creds failed")
            self.driver.close()
            assert False
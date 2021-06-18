import time
import pytest
from pageObjects.login_page import login_page
from pageObjects.add_customer_page import AddCustomer
from pageObjects.search_customer_page import SearchCustomer
from utilities.read_properties import read_props
from utilities.custom_logger import log_gen

class Test_SearchCustomerByEmail_004:
    baseUrl = read_props.get_url()
    username = read_props.get_username()
    password = read_props.get_password()
    logger = log_gen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByEmail(self,setUp):
        self.logger.info("************* SearchCustomerByEmail_004 **********")
        self.driver=setUp
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.lp = login_page(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting Search Customer By Email **********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.logger.info("************* searching customer by emailID **********")
        searchcust = SearchCustomer(self.driver)
        searchcust.setEmail("victoria_victoria@nopCommerce.com")
        searchcust.clickSearch()
        time.sleep(5)
        status=searchcust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        self.driver.close()
        assert True==status
        self.logger.info("***************  TC_SearchCustomerByEmail_004 Finished  *********** ")

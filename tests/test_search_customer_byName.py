import time
import pytest
from pageObjects.login_page import login_page
from pageObjects.add_customer_page import AddCustomer
from pageObjects.search_customer_page import SearchCustomer
from utilities.read_properties import read_props
from utilities.custom_logger import log_gen

class Test_SearchCustomerByName_005:
    baseUrl = read_props.get_url()
    username = read_props.get_username()
    password = read_props.get_password()
    logger = log_gen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByName(self,setUp):
        self.logger.info("************* SearchCustomerByName_005 **********")
        self.driver=setUp
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.lp = login_page(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting Search Customer By Name **********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()
        time.sleep(2)

        self.logger.info("************* searching customer by Name **********")
        searchcust = SearchCustomer(self.driver)
        searchcust.setFirstName("Victoria")
        searchcust.setLastName("Terces")
        searchcust.clickSearch()
        time.sleep(5)
        status=searchcust.searchCustomerByName("Victoria Terces")
        self.driver.close()
        assert True==status
        self.logger.info("***************  TC_SearchCustomerByName_005 Finished  *********** ")
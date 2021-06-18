

class login_page:
    txtbox_username_id = "Email"
    txtbox_password_id = "Password"
    btn_login_xpath = "//button[contains(text(),'Log in')]"
    link_logout_linktxt = "Logout"


    def __init__(self,driver):
        self.driver = driver


    def set_username(self,username):
        self.driver.find_element_by_id(self.txtbox_username_id).clear()
        self.driver.find_element_by_id(self.txtbox_username_id).send_keys(username)


    def set_password(self,password):
        self.driver.find_element_by_id(self.txtbox_password_id).clear()
        self.driver.find_element_by_id(self.txtbox_password_id).send_keys(password)


    def click_login(self):
        self.driver.find_element_by_xpath(self.btn_login_xpath).click()


    def click_logout(self):
        self.driver.find_element_by_link_text(self.link_logout_linktxt).click()
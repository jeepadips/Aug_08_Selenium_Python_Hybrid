from selenium.webdriver.common.by import By


class LoginPage:
    #textbox_username_id="Email"
    textbox_username_name = "username"
    #textbox_password_id="Password"
    textbox_password_name = "password"
    button_login_tagname="submit"

    link_logout_linktext="Logout"

    def __init__(self,driver):
        self.driver =driver

    def setUserName(self,username):
        self.driver.find_element(by=By.NAME, value=self.textbox_username_name).clear()
        self.driver.find_element(by=By.NAME, value=self.textbox_username_name).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(by=By.NAME, value=self.textbox_password_name).clear()
        self.driver.find_element(by=By.NAME, value=self.textbox_password_name).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_css_selector(self.button_login_tagname).click()

    def clickLogout(self):
        self.driver.find_element_by_link_text(self.link_logout_linktext).click()


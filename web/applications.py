
from features.pom.Login_Page import LoginPage


class Application:

    def __init__(self, driver):
        self.LoginPage = LoginPage(driver)
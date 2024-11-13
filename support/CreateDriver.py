
from configurations.config import Datatest
from support.WebdriverFactory import WebDriverFactory


class CreateDriver(WebDriverFactory):

    @staticmethod
    def set_up_config():
        print("##############################")
        print("[ POM CONFIGURATION ] - Lee la configuracion de propiedades basicas del archivo config.py")
        print("##############################")
        browser = Datatest.BROWSER
        print("[ POM CONFIGURATION ] - | Browser: ", browser , " |")
        print("##############################")

        driver = WebDriverFactory.CreateNewWebDriver(browser)
        return driver
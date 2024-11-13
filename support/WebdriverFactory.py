from selenium import webdriver

from configurations.config import Datatest
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as GeckoService

from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

class WebDriverFactory:

    @staticmethod
    def CreateNewWebDriver(browser_value):

        if browser_value.upper() == "FIREFOX":

            firefox_options = webdriver.FirefoxOptions()
            service_firefox = GeckoService(GeckoDriverManager().install())
            firefox_options.add_argument("--start-maximized")
            if Datatest.HEADLESS_MODE:
                firefox_options.add_argument("--headless")
            driver = webdriver.Firefox(firefox_options, service_firefox)
        elif browser_value.upper() == "CHROME":
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--disable-cache")
            service_chrome = ChromeService(ChromeDriverManager().install())
            if Datatest.HEADLESS_MODE:
                chrome_options.add_argument("--headless")
            driver = webdriver.Chrome(options=chrome_options, service=service_chrome)
        elif browser_value.upper() == "MICROSOFT EDGE":
            explorer_options = webdriver.EdgeOptions()
            service_edge = EdgeService(EdgeChromiumDriverManager().install())
            if Datatest.HEADLESS_MODE:
                explorer_options.add_argument("--headless")
            driver = webdriver.Edge(explorer_options, service_edge)

        else:
            print(
                "El driver no esta seleccionado en las propiedades, nombre invalido: " + browser_value)
            return None
        driver.maximize_window()
        return driver
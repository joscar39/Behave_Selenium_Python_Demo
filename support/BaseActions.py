import time

import allure
from allure_commons.types import AttachmentType
from selenium.common import NoSuchElementException, TimeoutException, ElementNotInteractableException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from configurations.config import Datatest


class BaseActions:

    def __init__(self, driver):
        self.driver = driver
        act = ActionChains(driver)
        self.act = act


    ########################## CONFIGURATION OF BROWSER AND SET VALUES OR DATA ###############################

    @staticmethod
    def time_wait(seconds):
        time.sleep(seconds)

    ##################################### SEARCH AND SEND; INPUTS, ELEMENTS, TEXT AND SELECTORS ################


    def SendTextBySelector(self, by_type: str, selector: str, text: str, seconds:float):
        """
        Metodo que permite enviar texto sobre un input a traves de localizador por selectores

        :param by_type: tipo de atributo BY a utilizar (XPATH, ID, CSS, ETC)
        :param selector: Localizador utilizado para identificar el selector
        :param text: Texto que se enviara al input, sea numerico o alfabetico se envia en formato str
        :param seconds: segundos que tardara el metodo en esperar que el input a recibir el texto este presente
        """

        try:
            ele = None
            ele = WebDriverWait(self.driver, seconds).until(EC.visibility_of_element_located((by_type, selector)))
            ele.clear()
            ele.send_keys(text)
            BaseActions.time_wait(1)
            print(f"Cargado el texto {text} correctamente")
            allure.attach(f"Cargado el texto {text} correctamente", "Envio de texto en input")
        except NoSuchElementException as ex:
            assert False, (f"No se pudo enviar el texto en el input, debido a que no se localizo\n"
                           f" el elemento {selector} de tipo {by_type}\nLog: ", ex)
        except ElementNotInteractableException as ex:
            assert False, (f"No se pudo enviar el texto en el input, debido a que no se puede\n"
                           f"interactuar con el elemento {selector} de tipo {by_type}\nLog: ", ex)
        except TimeoutException as ex:
            assert False, ("No se pudo enviar el texto debido que el tiempo de espera\n"
                           f" fue excedido para encontrar el elemento {selector} de tipo {by_type}\nLog: ", ex)
        except Exception as ex:
            assert False, (f"Fallo Desconocido al intentar enviar el texto en el input\n"
                           f" con el elemento {selector} de tipo {by_type}\nLog: ", ex)


    def getTitleWeb(self):
        """
        Metodo para Obtener el title de una pagina web
        :return: Retorna el valor del title
        """
        try:
            val = None
            self.driver.implicitly_wait(Datatest.IMPLICIT_WAIT)
            val = self.driver.title
            print(f"Se encontro el title: {val}")
            allure.attach(val, "Obtencion de title")
            return str(val)
        except Exception as ex:
            assert False, f"Fallo Desconocido al intentar obtener el title: {ex}"


    #################### CLICK ON ELEMENT #################################################


    def clickOnElementByText(self, text: str, seconds: float):
        """
        Metodo para Hacer click sobre un elemento que contenga un texto en especifico
        :param text: texto que se desea ubicar para que se genere la accion de click
        :param seconds: tiempo de espera mientras se localiza el elemento
        """

        try:
            ele = None
            ele = WebDriverWait(self.driver, seconds).until(EC.visibility_of_element_located
                                                            ((By.XPATH, f"//*[contains(text(), '{text}')]")))
            ele.click()
            print(f"Se realizo click sobre el elemento con el texto: {text}")
            allure.attach(f"Se realizo click sobre el elemento con el texto: {text}",
                          "Click sobre elemento que contiene texto")
            BaseActions.time_wait(1)
        except NoSuchElementException as ex:
            assert False, (f"No se pudo hacer click sobre el elemento, debido a que no se localizo\n"
                           f" el texto {text}\nLog: ", ex)
        except ElementNotInteractableException as ex:
            assert False, (f"No se pudo hacer click sobre el elemento, debido a que no se puede\n"
                           f"interactuar con el elementoque contiene el texto  {text}\nLog: ", ex)
        except TimeoutException as ex:
            assert False, ("No se pudo hacer click sobre el elemento debido que el tiempo de espera\n"
                           f" fue excedido para encontrar el elemento con el texto {text}\nLog: ", ex)
        except Exception as ex:
            assert False, (f"Fallo Desconocido al intentar hacer click "
                           f"sobre el elemento con el texto {text}en el input\nLog: ", ex)

    ####################### EVALUATE ELEMENT TO RETURN BOOLEAN ####################################

    def findElementIsDisplayed(self, by_type: str, selector: str, seconds: float):
        """
        Metodo que permite localizar un elemento a travez de un selector y retorna True si es localizado exitosamente

        :param by_type: tipo de atributo BY a utilizar (XPATH, ID, CSS, ETC)
        :param selector: Localizador utilizado para identificar el selector
        :param seconds: Tiempo de espera para que el elemento sea localizado
        :return: True si localiza el elemento, o False si no lo encuentra
        """

        try:
            element = None
            element = WebDriverWait(self.driver, seconds).until(EC.visibility_of_element_located
                                                            ((by_type, selector)))
            if element.is_displayed():
                print(f"Se encontro en pantalla el elemento: {selector} de tipo {by_type}")
                allure.attach(f"Se encontro en pantalla el elemento: {selector} de tipo {by_type}", "verificacion de elemento")
                return True
        except TimeoutException:
            print(f"Error: Tiempo de espera agotado mientras se buscaba el elemento: {selector} de tipo {by_type}")
            return False
        except NoSuchElementException:
            print(f"Error: No se encontró el elemento: {selector} de tipo {by_type}")
            return False
        except ElementNotInteractableException:
            print(f"Error: No se puede interactuar con el elemento: {selector} de tipo {by_type}")
            return False
        except Exception:
            print(f"Error desconocido: No se localizo el elemento")
            return False

    #################### ALLURE SCREENSHOT AND UPLOAD FILE #################################

    def screenshot(self, name:str):
        """
        Metodo para capturar evidencia en allure
        :param name: nombre que se le asignara a la evidencia
        """

        allure.attach(self.driver.get_screenshot_as_png(), name=name, attachment_type=AttachmentType.PNG )

import time
import allure
import colorama
from allure_commons.types import AttachmentType
from configurations.config import Datatest
from support.CreateDriver import CreateDriver

from support.BaseActions import BaseActions

def before_scenario(context, scenario):
    # Configuracion del driver de selenium
    print("##############################")
    print("[ CONFIGURATION ] - Inicializando la configuracion del controlador")
    print("##############################")
    context.driver = CreateDriver.set_up_config()
    context.driver.get(Datatest.URL_WEB)
    context.driver.implicitly_wait(Datatest.IMPLICIT_WAIT)
    print("##############################")
    print("[ SCENARIO ] - " + scenario.name)
    print("##############################")

def after_scenario(context, scenario):
# Cierre del driver de Selenium
    global failed_step_name
    if scenario.status == "failed":
        scenario_name = scenario.name
        for step in scenario.steps:
            if step.status == "failed":
                failed_step_name = step.name
        current_time = time.strftime("%Y-%m-%d_%H-%M-%S", time.gmtime())
        screenshot_name = f"{scenario_name}_{failed_step_name}_{current_time}.png"
        allure.attach(context.driver.get_screenshot_as_png(), name=screenshot_name, attachment_type=AttachmentType.PNG)
        context.driver.close()
        colorama.init()
        print(f"{colorama.Fore.RED}###############################################{colorama.Fore.RED}")
        print(f"{colorama.Fore.RED}[  DRIVER STATUS  ] - Limpiando y cerrando instancia del"
              f" controlador debido a un error del scenario{colorama.Fore.RED}")
        print(f"{colorama.Fore.RED}{scenario_name}{colorama.Fore.RED}")
        print(f"{colorama.Fore.RED}###############################################{colorama.Fore.RESET}")
        print("____________________________________________________________________________")
    elif scenario.status == "passed":
        print(f"{colorama.Fore.GREEN}----------------------")
        print(f"[  SCENARIO STATUS  ] - Prueba Exitosa (PASS): {scenario.name}")
        print(f"----------------------{colorama.Fore.RESET}")
        context.driver.close()
        context.driver.quit()


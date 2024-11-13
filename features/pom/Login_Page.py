from support.BaseActions import BaseActions


class LoginPage(BaseActions):

    def __init__(self, driver):
        super().__init__(driver)


    """
    FUNCIONES PARA GESTOS Y ACCIONES
    """




    """
    FUNCIONES PARA VALIDADORES
    """

    def ValidateInitLoginPage(self, title):
        val = BaseActions.getTitleWeb(self)
        if val == title:
            BaseActions.screenshot(self, "Validado el title de la web correctamente")
        else:
            assert False, "No se mostro el title del home como se esperaba"
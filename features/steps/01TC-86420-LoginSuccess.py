from behave import *

from web.applications import Application


@given(u'Acceder a la URL del aplicativo DEMO QA')
def step_impl(context):
    try:
        context.application = Application(context.driver)
    except Exception as ex:
        assert False, f"Fallo el step al intentar acceder la URL Seleccionada \n El motivo: {ex}"


@then(u'Mostrar el login de la web IAC con el title:"{Title}"')
def step_impl(context, Title):
    try:
        context.application.LoginPage.ValidateInitLoginPage(Title)
    except Exception as ex:
        assert False, f"Fallo el step al intentar validar el title de la web \n El motivo: {ex}"

@precondition
Feature: 01 Login
  Background:
    Given Acceder a la URL del aplicativo DEMO QA

  Scenario Outline: 01TC-86420 - Login Iniciar sesion exitoso con usuario valido
    # TC-86420: Login Iniciar sesion exitoso con usuario valido
    Then Mostrar el login de la web IAC con el title:"<Title>"

    Examples:
      |    Title        |
      |     DEMOQA      |
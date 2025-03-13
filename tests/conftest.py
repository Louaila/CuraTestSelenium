import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture
def driver():

    # Tout ce qui vient avant le yield sera exécuté avant
    # le lancement des tests.

    # Instancier le driver Chrome avec ses options
    browser = webdriver.Chrome()
    
    # Aller sur la page de Décathlon
    browser.get("https://katalon-demo-cura.herokuapp.com/")

    # Maximiser la fenêtre
    browser.maximize_window()

    yield browser  # Provide the driver to the test

    # Tout ce qui vient après le yield sera exécuté
    # à la fin des tests
    browser.quit()  # Fermeture du navigateur


@pytest.fixture
def wait(driver):
    # Instancier le wait explicit pour le driver
    return WebDriverWait(driver, 10)
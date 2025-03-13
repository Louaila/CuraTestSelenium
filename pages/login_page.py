from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class LoginPage:
    def __init__(self, driver, wait):
        
        # | ENVIRONNEMENT
        # |
        # v Ici, on met le driver et le wait

        self.driver = driver
        self.wait = wait

        # | LOCATORS
        # |
        # v Ici, vous pouvez mettre les locators

        self.input_username = (By.ID, "txt-username")
        self.input_password = (By.ID, "txt-password")
        self.bouton_login = (By.ID, "btn-login")


    # | FONCTIONS
    # | Ici, vous pouvez définir les fonctions pour interagir avec les éléments,
    # v et effectuer des actions utilisateurs
    
    def entrer_username(self, username):
        username_element = self.wait.until(EC.element_to_be_clickable(self.input_username))
        username_element.clear()
        username_element.send_keys(username)
        valeur_champ = username_element.get_attribute("value")
        assert valeur_champ == username, f"Le  username devrait être {username} mais est {valeur_champ}"
    
    def entrer_password(self, password):
        password_element = self.wait.until(EC.element_to_be_clickable(self.input_password))
        password_element.clear()
        password_element.send_keys(password)
        valeur_champ = password_element.get_attribute("value")
        assert valeur_champ == password, f"Le  password devrait être {password} mais est {valeur_champ}"

    def cliquer_bouton_login(self):
        self.wait.until(EC.element_to_be_clickable(self.bouton_login)).click()

    def se_connecter(self, username, password):
        self.entrer_username(username)
        self.entrer_password(password)
        self.cliquer_bouton_login()
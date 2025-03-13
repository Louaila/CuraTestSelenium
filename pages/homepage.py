from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class HomePage:
    def __init__(self, driver, wait):
        
        # | ENVIRONNEMENT
        # |
        # v Ici, on met le driver et le wait

        self.driver = driver
        self.wait = wait

        # | LOCATORS
        # |
        # v Ici, vous pouvez mettre les locators

        self.homepage_header = (By.TAG_NAME, "h1")
        self.bouton_prendre_rdv = (By.ID, "btn-make-appointment")
        self.confirmation_rdv = (By.TAG_NAME, "h2")


    # | FONCTIONS
    # | Ici, vous pouvez définir les fonctions pour interagir avec les éléments,
    # v et effectuer des actions utilisateurs

    def verifier_titre_homepage(self, titre):
        actual_title = self.wait.until(EC.visibility_of_element_located(self.homepage_header)).text
        assert actual_title == titre, f"Le titre attendu devrait être '{titre}', mais le résultat est '{actual_title}'"
    

    def cliquer_sur_prendre_un_rdv(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.bouton_prendre_rdv)).click()
        except TimeoutException:
            print("Cookies pop-up is not present")
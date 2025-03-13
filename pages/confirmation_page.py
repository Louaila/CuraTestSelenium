from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class ConfirmationPage:
    def __init__(self, driver, wait):
        
        # | ENVIRONNEMENT
        # |
        # v Ici, on met le driver et le wait

        self.driver = driver
        self.wait = wait

        # | LOCATORS
        # |
        # v Ici, vous pouvez mettre les locators

        self.confirmation_rdv = (By.TAG_NAME, "h2")
        self.bouton_go_homepage = (By.LINK_TEXT, "Go to Homepage")
        self.texte_facility = (By.ID, "facility")
        self.texte_admission_hopital = (By.ID, "hospital_readmission")
        self.texte_program = (By.ID, "program")
        self.texte_date = (By.ID, "visit_date")
        self.texte_facility = (By.ID, "facility")
        self.texte_comment = (By.ID, "comment")


    # | FONCTIONS
    # | Ici, vous pouvez définir les fonctions pour interagir avec les éléments,
    # v et effectuer des actions utilisateurs
    def verifier_confirmation_rdv(self):
        # Récupérer le message de confirmation et vérifier s'il est affiché et que le texte est bon
        try:
            message_confirmation = self.wait.until(EC.visibility_of_element_located(self.confirmation_rdv))
            assert message_confirmation.text == "Appointment Confirmation",\
                f"Le message de confirmation doit être 'Appointment Confirmation' mais est {message_confirmation.text}"
        except TimeoutException:
            # Si le message n'est pas affiché, on fail le test exprès
            assert message_confirmation.is_displayed(), "Le message de confirmation n'est pas affiché"


    def verifier_informations_formulaire(self, facility, admission, programme, date, commentaire):
        info_facility = self.driver.find_element(*self.texte_facility).text
        assert info_facility == facility, f"La facility doit être {facility} mais est {info_facility}"

        info_admission = self.driver.find_element(*self.texte_admission_hopital).text
        attendu = "Yes" if admission else "No"
        assert info_admission == attendu, f"L'admission à l'hôpital doit être {attendu} mais est {info_admission}"

        info_programme = self.driver.find_element(*self.texte_program).text
        assert info_programme == programme, f"Le programme doit être {programme} mais est {info_programme}"

        info_date = self.driver.find_element(*self.texte_date).text
        assert info_date == date, f"La date doit être {date} mais est {info_date}"

        info_commentaire = self.driver.find_element(*self.texte_comment).text
        assert info_commentaire == commentaire, f"Le commentaire doit être {commentaire} mais est {info_commentaire}"


    def cliquer_bouton_retour_homepage(self):
        # Cliquer sur le bouton Go to Homepage
        self.wait.until(EC.element_to_be_clickable(self.bouton_go_homepage)).click()
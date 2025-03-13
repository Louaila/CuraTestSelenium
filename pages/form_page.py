from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select

class FormPage:
    def __init__(self, driver, wait):
        
        # | ENVIRONNEMENT
        # |
        # v Ici, on met le driver et le wait

        self.driver = driver
        self.wait = wait

        # | LOCATORS
        # |
        # v Ici, vous pouvez mettre les locators

        self.select_facility = (By.ID, "combo_facility")
        self.checkbox_apply_hospital = (By.ID, "chk_hospotal_readmission")
        self.input_date = (By.ID, "txt_visit_date")
        self.input_commentaire = (By.ID, "txt_comment")
        self.bouton_confirmation_rdv = (By.ID, "btn-book-appointment")

    # | FONCTIONS
    # | Ici, vous pouvez définir les fonctions pour interagir avec les éléments,
    # v et effectuer des actions utilisateurs

    def choisir_facility(self, choix_facility):
        # Récupérer le menu déroulant pour choisir la facility
        facility_element = self.wait.until(EC.element_to_be_clickable(self.select_facility))
        
        # Instancier une classe Select
        menu = Select(facility_element)
        
        # Choisir le type en utilisant le texte visible
        menu.select_by_visible_text(choix_facility)

        # Vérifier le choix du select
        texte_selectionne = menu.first_selected_option.text
        assert texte_selectionne == choix_facility, f"Le type de facility doit être {choix_facility} mais est {texte_selectionne}"


    def postuler_admission_hopital(self, postuler):
        # Récupérer la case à cocher pour l'admission
        case_admission = self.wait.until(EC.element_to_be_clickable(self.checkbox_apply_hospital))

        # Si on veut postuler à l'admission mais que la case à cocher n'est pas cochée
        # par défaut, alors on clique dessus pour la sélectionner
        if postuler and not case_admission.is_selected():
            case_admission.click()
            assert case_admission.is_selected(), "La case d'admission à l'hôpital doit être cochée"

        # Si on ne veut pas postuler à l'admission mais que la case à cocher est cochée
        # par défaut, alors on clique dessus pour la désélectionner
        elif not postuler and case_admission.is_selected():
            case_admission.click(), "La case d'admission à l'hôpital ne doit pas être cochée"


    def choisir_programme(self, choix_programme):
        # Récupérer le bouton radio correspondant en utilisant son ID variabilisé
        bouton_choix = self.wait.until(EC.element_to_be_clickable((By.ID, f"radio_program_{choix_programme.lower()}")))

        # Cliquer sur le bouton radio récupéré
        bouton_choix.click()

        # Vérifier que le bouton radio es bien sélectionné
        assert bouton_choix.is_selected(), f"Le bouton radio {choix_programme.capitalize()} doit être sélectionné"


    def saisir_une_date(self, date):
        # Récupérer le champ de date
        champ_date = self.wait.until(EC.element_to_be_clickable(self.input_date))

        # Saisir la date
        champ_date.clear()
        champ_date.send_keys(date)
        champ_date.send_keys(Keys.ESCAPE)

        # Vérifier que la date saisie est bonne
        date_actuelle = champ_date.get_attribute("value")
        assert date_actuelle == date, f"La date saisie doit être {date} mais est {date_actuelle}"


    def ecrire_commentaire(self, commentaire):
        # Récupérer le champ de commentaire
        champ_comm = self.wait.until(EC.element_to_be_clickable(self.input_commentaire))

        # Saisir un commentaire
        champ_comm.clear()
        champ_comm.send_keys(commentaire)

        # Vérifier la saisie du commentaire
        commentaire_saisi = champ_comm.get_attribute("value")
        assert commentaire_saisi == commentaire, f"Le commentaire saisi doit être {commentaire} mais est {commentaire_saisi}"
    
    
    def cliquer_confirmation_rdv(self):
        # Récupérer le bouton de prise de rendez-vous
        self.wait.until(EC.element_to_be_clickable(self.bouton_confirmation_rdv)).click()

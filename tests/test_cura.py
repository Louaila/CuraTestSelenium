from pages.homepage import HomePage
from pages.login_page import LoginPage
from pages.form_page import FormPage
from pages.confirmation_page import ConfirmationPage

# Je définis des variables que je vais utiliser dans mon test
facility = "Hongkong CURA Healthcare Center"
admission = True
programme = "Medicaid"
date = "15/08/2024"
commentaire = "Ceci n'est pas un test"


def test_prendre_rdv(driver, wait):

    # Instancier la page d'accueil
    homepage = HomePage(driver, wait)

    # Vérifier le titre de la page
    homepage.verifier_titre_homepage("CURA Healthcare Service")

    # Cliquer sur le bouton pour prendre un RDV
    homepage.cliquer_sur_prendre_un_rdv()

    # Instancier la page de login
    login_page = LoginPage(driver, wait)

    # Se connecter avec l'utilisateur
    login_page.se_connecter("John Doe", "ThisIsNotAPassword")

    # Instancier la page du formulaire
    form_page = FormPage(driver, wait)

    # Saisir les informations du formulaire
    form_page.choisir_facility(facility)
    form_page.postuler_admission_hopital(admission)
    form_page.choisir_programme(programme)
    form_page.saisir_une_date(date)
    form_page.ecrire_commentaire(commentaire)
    form_page.cliquer_confirmation_rdv()

    # Instanciation de la page
    confirmation_page = ConfirmationPage(driver, wait)

    # Vérifier la confirmation et les informations du RDV
    confirmation_page.verifier_confirmation_rdv()
    confirmation_page.verifier_informations_formulaire(facility, admission, programme, date, commentaire)

    # Cliquer sur le bouton retour à la page d'accueil
    confirmation_page.cliquer_bouton_retour_homepage()

    # Vérifier le titre de la page d'accueil
    homepage.verifier_titre_homepage("CURA Healthcare Service")
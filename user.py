# PYSIDE6-MALLINE SOVELLUKSEN PÄÄIKKUNAN LUOMISEEN
# KÄÄNNETYSTÄ KÄYTTÖLIITTYMÄTIEDOSTOSTA (mainWindow_ui.py)
# =====================================================

# KIRJASTOJEN JA MODUULIEN LATAUKSET
# ----------------------------------
import os # Polkumääritykset
import sys # Käynnistysargumentit
import json # JSON-tiedostojen käsittely

from PySide6 import QtWidgets # Qt-vimpaimet
from PySide6.QtCore import QThreadPool, Slot

from lendingModules import sound # Äänitoiminnot
from lendingModules import dbOperations # Tietokantatoiminnot
from lendingModules import cipher # Salausmoduuli

# mainWindow_ui:n tilalle käännetyn pääikkunan tiedoston nimi
# ilman .py-tiedostopäätettä
from user_ui import Ui_MainWindow # Käännetyn käyttöliittymän luokka

# Määritellään luokka, joka perii QMainWindow- ja Ui_MainWindow-luokan
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """A class for creating a main window for the application"""
    
    # Määritellään olionmuodostin ja kutsutaan yliluokkien muodostimia
    def __init__(self):
        super().__init__()

        # Luodaan käyttöliittymä konvertoidun tiedoston perusteella MainWindow:n ui-ominaisuudeksi. Tämä suojaa lopun MainWindow-olion ylikirjoitukselta, kun ui-tiedostoa päivitetään
        self.ui = Ui_MainWindow()

        # Kutsutaan käyttöliittymän muodostusmetodia setupUi
        self.ui.setupUi(self)

        # Rutiini, joka lukee asetukset, jos ne ovat olemassa
        try:
            # Avataam asetustiedosto ja muutetaan se Python sanakirjaksi
            with open('settings.json', 'rt') as settingsFile: # With sulkee tiedoston automaattisesti
                
                jsonData = settingsFile.read()
                self.currentSettings = json.loads(jsonData)
            
            # Puretaan salasana tietokantaoperaatioita varten  
            self.plainTextPassword = cipher.decryptString(self.currentSettings['password'])
        
        except Exception as error:
            self.openWarning()


        # Äänet oletuksena käytössä
        self.soundOn = True

        # Ohjelman käynnistyksessä piilotetaan tarpeettomat elementit
        self.setInitialElements()


        # OHJELMOIDUT SIGNAALIT
        # ---------------------
        
        # Kun Lainaa-painiketta painetaan, kutsutaan activateLender-metodia
        self.ui.takeCarPushButton.clicked.connect(self.activateLender)

        # Kun ajokortin viivakoodi on luettu, kutsutaan activateKey-metodia
        self.ui.ssnLineEdit.returnPressed.connect(self.activateKey)
        
        # Kun avaimenperä on luettu, kutsutaan setLendingData-metodia
        self.ui.keyBarcodeLineEdit.returnPressed.connect(self.setLendingData)

        # Kun OK-painiketta on painettu, tallenna tiedot 
        # ja palauta käyttöliittymä alkutilaan
        self.ui.okPushButton.clicked.connect(self.saveLendingData)

        # Kun palauta-painiketta on painettu, kutsutaan activateReturnCar-metodia
        self.ui.returnCarPushButton.clicked.connect(self.activateReturnCar)

        # Kun avaimenperä on luettu palutettaessa, kutsutaan saveReturnData-metodia
        self.ui.keyReturnBarcodeLineEdit.returnPressed.connect(self.saveReturnData)
    
        # Kun mykistä painiketta painetaan, kutsutaan mute-metodia
        self.ui.soundOffPushButton.clicked.connect(self.mute)

        # Kun äänipäiniketta painetaan, kutsutaan unmute-metodia
        self.ui.soundOnPushButton.clicked.connect(self.unmute)

        # Kun kumoa painiketta painetaan palautetaan UI-alkutilaan
        self.ui.goBackPushButton.clicked.connect(self.goBack)
    
    # OHJELMOIDUT SLOTIT
    # ------------------
   

    # Palauta käyttöliittymä alkutilanteeseen
    def setInitialElements(self):
        self.ui.returnCarPushButton.show()
        self.ui.takeCarPushButton.show()
        self.ui.okPushButton.hide()
        self.ui.calendarLabel.hide()
        self.ui.clockLabel.hide()
        self.ui.dateLabel.hide()
        self.ui.goBackPushButton.hide()
        self.ui.keyBarcodeLineEdit.clear()
        self.ui.keyBarcodeLineEdit.hide()
        self.ui.keyReturnBarcodeLineEdit.clear()
        self.ui.keyReturnBarcodeLineEdit.hide()
        self.ui.keyPictureLabel.hide()
        self.ui.lenderPictureLabel.hide()
        self.ui.soundOnPushButton.hide()
        self.ui.ssnLineEdit.clear()
        self.ui.ssnLineEdit.hide()
        self.ui.statusLabel.hide()
        self.ui.timeLabel.hide()
        self.ui.lenderNameLabel.hide()
        self.ui.carInfoLabel.hide()

    # Näyttää lainaajan kuvakkeen ja henkilötunnuksen kentän
    def activateLender(self):
        self.ui.statusLabel.setText('Auton lainaus')
        self.ui.lenderPictureLabel.show()
        self.ui.ssnLineEdit.show()
        self.ui.goBackPushButton.show()
        self.ui.ssnLineEdit.setFocus()
        self.ui.returnCarPushButton.hide()
        self.ui.takeCarPushButton.hide()
        self.ui.statusLabel.show()
        self.ui.statusbar.showMessage('Syötä ajokortti koneeseen')
        if self.soundOn:
            sound.playWav('sounds\\drivingLicence.WAV')
        

    # Näyttää avaimen kuvakkeen, rekisterikenttä ja lainaajan tiedot
    def activateKey(self):
        self.ui.ssnLineEdit.hide()
        self.ui.keyPictureLabel.show()
        self.ui.keyBarcodeLineEdit.show()
        self.ui.keyBarcodeLineEdit.setFocus()
        self.ui.lenderNameLabel.show()
        self.ui.statusbar.showMessage('Syötä avaimenperä koneeseen')
        if self.soundOn:
            sound.playWav('sounds\\readKey.WAV')

    # Näyttää lainauksen loput tiedot
    def setLendingData(self):
        self.ui.carInfoLabel.show()
        self.ui.dateLabel.show()
        self.ui.calendarLabel.show()
        self.ui.timeLabel.show()
        self.ui.clockLabel.show()
        self.ui.okPushButton.show()
        self.ui.statusbar.showMessage('Jos tiedot ovat oikein paina OK')
        if self.soundOn:
            sound.playWav('sounds\\saveData.WAV')

    # Tallennetaan lainauksen tiedot ja palautetaan käyttöliittymä alkutilaan
    def saveLendingData(self):
        # Save data to the database
        # Luetaan tietokanta-asetukset paikallisiin muuttujiin
        dbSettings = self.currentSettings
        plainTextPassword = self.plainTextPassword
        dbSettings['password'] = plainTextPassword # Vaidetaan selväkieliseksi

        try:
            # Luodaan tietokantayhteys-olio
            dbConnection = dbOperations.DbConnection(dbSettings)
            ssn = self.ui.ssnLineEdit.text()
            key = self.ui.keyBarcodeLineEdit.text()
            dataDictionary = {'hetu': ssn,
                            'rekisterinumero': key}
            dbConnection.addToTable('lainaus', dataDictionary)

            self.setInitialElements()
            self.ui.statusbar.showMessage('Auton lainaustiedot tallennettiin', 5000)
            if self.soundOn:
                sound.playWav('sounds\\lendingOk.WAV')
        except Exception as e:
            title = 'Lainaustietojen tallentaminen ei onnistu'
            text = 'Ajokorttin tai auton tiedot virheelliset, ota yhteys henkilökuntaan!'
            detailedText = str(e)
            self.openWarning(title, text, detailedText)
        

    # Näytetään palautukseen liittyvät kentät ja kuvat
    def activateReturnCar(self):
        self.ui.takeCarPushButton.hide()
        self.ui.returnCarPushButton.hide()
        self.ui.statusLabel.setText('Auton palautus')
        self.ui.keyPictureLabel.show()
        self.ui.keyReturnBarcodeLineEdit.show()
        self.ui.keyReturnBarcodeLineEdit.setFocus()
        self.ui.statusbar.showMessage('Lue avaimen viivakoodi')
        if self.soundOn:
            sound.playWav('sounds\\readKey.WAV')

    # Tallennetaan palautuksen tiedot tietokantaan ja palautetaan UI alkutilaan
    def saveReturnData(self):
        self.ui.statusbar.showMessage('Auto palautettu')
        self.setInitialElements()
        if self.soundOn:
            sound.playWav('sounds\\returnOk.WAV')

    # Mykistetään äänet
    def mute(self):
        self.ui.soundOffPushButton.hide()
        self.ui.soundOnPushButton.show()
        self.ui.statusbar.showMessage('Äänet mykistetty')
        self.soundOn = False
    
    # Poistetaan mykistys
    def unmute(self):
        self.ui.soundOffPushButton.show()
        self.ui.soundOnPushButton.hide()
        self.ui.statusbar.showMessage('Äänet käytössä')
        self.soundOn = True
    
    def goBack(self):
        self.setInitialElements()
        self.ui.statusbar.showMessage('Toiminto peruutettiin', 5000)
        
    # Avataan MessageBox
    # Malli mahdollista virheilmoitusta varten
    def openWarning(self, title: str, text:str, detailedText:str) -> None: 
        """Opens a message box for errors

        Args:
            title (str): The title of the message box
            text (str): Error message
            detailedText (str): Detailed error message typically from source
        """
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Critical)
        msgBox.setWindowTitle(title)
        msgBox.setText(text)
        msgBox.setDetailedText(detailedText)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec()


# LUODAAN VARSINAINEN SOVELLUS
# ============================
app = QtWidgets.QApplication(sys.argv)

# Luodaan objekti pääikkunalle ja tehdään siitä näkyvä
window = MainWindow()
window.show()

# Käynnistetään sovellus ja tapahtumienkäsittelijä (event loop)
app.exec()

    
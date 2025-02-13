# PYSIDE6-MALLINE SOVELLUKSEN PÄÄIKKUNAN LUOMISEEN
# KÄÄNNETYSTÄ KÄYTTÖLIITTYMÄTIEDOSTOSTA (mainWindow_ui.py)
# =====================================================

# KIRJASTOJEN JA MODUULIEN LATAUKSET
# ----------------------------------
import os # Polkumääritykset
import sys # Käynnistysargumentit
import json # JSON-tiedostojen käsittely

from PySide6 import QtWidgets # Qt-vimpaimet
from PySide6.QtCore import QThreadPool, Slot # Säikeistys ja Slot-dekoraattori

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

        # Luodaan säikeistystä varten uusi säievaranto
        self.threadPool = QThreadPool().globalInstance()

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
        
        # Jos asetusten luku ei onnistu, näytetään virhedialogi
        except Exception as error:
            title = 'Tietokanta-asetusten luku ei onnistunut'
            text = 'Tietokanta-asetuksien avaaminen ja salasanan purku ei onnistunut'
            detailedText = str(error)
            self.openWarning(title, text, detailedText)


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
   
    # Soita parametrina annettu äänistiedosto (työfunktio)
    @Slot(str)
    def playSoundFile(self, soundFileName):
        fileAndPath = 'sounds\\' + soundFileName
        sound.playWav(fileAndPath)
    
    # Säikeen käynnistävä funktio 
    @Slot(str)
    def playSoundInTread(self, soundFileName):
        self.threadPool.start(lambda: self.playSoundFile(soundFileName))

    # Palauta käyttöliittymä alkutilanteeseen ja päivittää vapaiden ja 
    # ajossa olevien autojen katalogit
    def setInitialElements(self):
        self.ui.returnCarPushButton.show()
        self.ui.takeCarPushButton.show()
        self.ui.statusFrame.show()
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
        
        # Luetaan tietokanta-asetukset paikallisiin muuttujiin
        dbSettings = self.currentSettings
        plainTextPassword = self.plainTextPassword
        dbSettings['password'] = plainTextPassword # Vaidetaan selväkieliseksi

        
        
        try:
            # Luodaan tietokantayhteys-olio
            dbConnection = dbOperations.DbConnection(dbSettings)
            inUseVehicles = dbConnection.readAllColumnsFromTable('ajossa')
            
            # Muodostetaan luettelo vapaista autoista createCatalog-metodilla
            catalogData = self.createCatalog(inUseVehicles)
            self.ui.inUsePlainTextEdit.setPlainText(catalogData)

        except Exception as e:
            title = 'Autotietojen lukeminen ei onnistunut'
            text = 'Ajossa olevien autojen tiedot eivät ole saatavissa'
            detailedText = str(e)
            self.openWarning(title, text, detailedText) 
    
    # Näyttää lainaajan kuvakkeen ja henkilötunnuksen kentän
    @Slot()
    def activateLender(self):
        self.ui.statusFrame.hide()
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
            self.playSoundInTread('drivingLicence.wav')
            
        

    # Näyttää avaimen kuvakkeen, rekisterikentän ja lainaajan tiedot
    @Slot()
    def activateKey(self):
        self.ui.ssnLineEdit.hide()
        self.ui.keyPictureLabel.show()
        self.ui.keyBarcodeLineEdit.show()
        self.ui.keyBarcodeLineEdit.setFocus()
        self.ui.lenderNameLabel.show()
        self.ui.statusbar.showMessage('Syötä avaimenperä koneeseen')
        if self.soundOn:
            self.playSoundInTread('readKey.wav')

        # TODO: Luetaan tietokannasta lainaajan nimi
        # Tietokanta-asetukset
        dbSettings = self.currentSettings
        plainTextPassword = self.plainTextPassword
        dbSettings['password'] = plainTextPassword # Vaidetaan selväkieliseksi
        # luetaan lainaajan tiedoista etunimi ja sukunimi
        try:
            # Luodaan tietokantayhteys-olio
            dbConnection = dbOperations.DbConnection(dbSettings)
            criteria = f"hetu = '{self.ui.ssnLineEdit.text()}'"
            resultSet = dbConnection.filterColumsFromTable('lainaaja',['etunimi', 'sukunimi'], criteria)
            row = resultSet[0]
            lenderName = f'{row[0]} {row[1]}'
            self.ui.lenderNameLabel.setText(lenderName)

        except Exception as e:
            title = 'Ajokortin lukeminen ei onnistunut'
            text = 'Ajokortin tietoja ei löytynyt, ota yhteys henkilökuntaan'
            detailedText = str(e)
            self.openWarning(title, text, detailedText)

    # Näyttää lainauksen loput tiedot
    @Slot()
    def setLendingData(self):
        self.ui.carInfoLabel.show()
        self.ui.dateLabel.show()
        self.ui.calendarLabel.show()
        self.ui.timeLabel.show()
        self.ui.clockLabel.show()
        self.ui.okPushButton.show()
        self.ui.statusbar.showMessage('Jos tiedot ovat oikein paina OK')
        if self.soundOn:
            self.playSoundInTread('saveData.wav')

        # Päivitetään auton tiedot 
         # TODO: Luetaan tietokannasta auton perustiedot
        # Tietokanta-asetukset
        dbSettings = self.currentSettings
        plainTextPassword = self.plainTextPassword
        dbSettings['password'] = plainTextPassword # Vaidetaan selväkieliseksi
        # luetaan lainaajan tiedoista etunimi ja sukunimi
        try:
            # Luodaan tietokantayhteys-olio
            dbConnection = dbOperations.DbConnection(dbSettings)
            criteria = f"rekisterinumero = '{self.ui.keyBarcodeLineEdit.text()}'"
            resultSet = dbConnection.filterColumsFromTable('auto',['merkki', 'malli', 'henkilomaara'], criteria)
            row = resultSet[0]
            carData = f'{row[0]} {row[1]} \n {row[2]}-paikkainen'
            self.ui.carInfoLabel.setText(carData)

        except Exception as e:
            title = 'Avaimenperän lukeminen ei onnistunut'
            text = 'Auton tietoja ei löytynyt, ota yhteys henkilökuntaan'
            detailedText = str(e)
            self.openWarning(title, text, detailedText)
        
        try:
            dbConnection = dbOperations.DbConnection(dbSettings)
            timeStamp = dbConnection.getPgTimestamp()
            rowValue = timeStamp[0]
            columnValue = rowValue[0]
            # Ensimmäiset 10 merkkiä on päivämäärä
            date = columnValue[0:10]
            # Merkit 12-17 ovat kellonaika minuuttien tarkkuudella
            time = columnValue[11:16]

            # Näytetään aikaleima käyttöliittymässä
            self.ui.dateLabel.setText(date)
            self.ui.timeLabel.setText(time)
            
        except Exception as e:
            title = 'Aikaleiman lukeminen ei onnistunut'
            text = 'Yhteys palvelimeen on katkennut, tee lainaus uudelleen'
            detailedText = str(e)
            self.openWarning(title, text, detailedText)

    # Tallennetaan lainauksen tiedot ja palautetaan käyttöliittymä alkutilaan
    @Slot()
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

        if self.soundOn:
            self.playSoundInTread('lendingOK.wav')
        

    # Näytetään palautukseen liittyvät kentät ja kuvat
    @Slot()
    def activateReturnCar(self):
        self.ui.statusFrame.hide()
        self.ui.takeCarPushButton.hide()
        self.ui.returnCarPushButton.hide()
        self.ui.statusLabel.setText('Auton palautus')
        self.ui.keyPictureLabel.show()
        self.ui.keyReturnBarcodeLineEdit.show()
        self.ui.keyReturnBarcodeLineEdit.setFocus()
        self.ui.statusbar.showMessage('Lue avaimen viivakoodi')
        if self.soundOn:
            sound.play('sounds\\readKey.WAV')

    # Tallennetaan palautuksen tiedot tietokantaan ja palautetaan UI alkutilaan
    @Slot()
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
    @Slot()
    def unmute(self):
        self.ui.soundOffPushButton.show()
        self.ui.soundOnPushButton.hide()
        self.ui.statusbar.showMessage('Äänet käytössä')
        self.soundOn = True
    
    @Slot()
    def goBack(self):
        self.setInitialElements()
        self.ui.statusbar.showMessage('Toiminto peruutettiin', 5000)
    
    # Metodi monirivisen luettelon muodostamiseen taulun tai näkymän datasta
    def createCatalog(self, tupleList: list, suffix='') -> str:
        """Creates a catalog like text for plainText edits from list of tuples.
        Typically list comes from a database table or view.

        Args:
            tupleList (list): list of tuples containing table data
            suffix (str, optional): a phrase to add to the end of the line. Defaults to ''.

        Returns:
            str: Plain text for the catalog
        """
        # Määritellään vapaana oleliven autojen tiedot
        # availablePlainTextEdit-elementtiin
        catalogData = ''
        rowText = ''
            
        for vehiclTtuple in tupleList:
            rowData = ''
            for vehicleData in vehiclTtuple:
                rowData = rowData + f'{vehicleData} '
            rowText = rowData + f'{suffix}\n'
            catalogData = catalogData + rowText
        return catalogData
    
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

    
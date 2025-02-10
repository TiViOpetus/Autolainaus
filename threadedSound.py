# PYSIDE6-MALLINE SOVELLUKSEN PÄÄIKKUNAN LUOMISEEN
# KÄÄNNETYSTÄ KÄYTTÖLIITTYMÄTIEDOSTOSTA (mainWindow_ui.py)
# =====================================================

# KIRJASTOJEN JA MODUULIEN LATAUKSET
# ----------------------------------
import os # Polkumääritykset
import sys # Käynnistysargumentit

from PySide6 import QtWidgets # Qt-vimpaimet
from PySide6.QtCore import QThreadPool, Slot # Säikeistys ja Slot-dekoraattori
from threadedSound_ui import Ui_MainWindow # Käännetyn käyttöliittymän luokka

from lendingModules import sound # Äänipalaute

# Määritellään luokka, joka perii QMainWindow- ja Ui_MainWindow-luokan
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """A class for creating main window for the application"""
    
    # Määritellään olionmuodostin ja kutsutaan yliluokkien muodostimia
    def __init__(self):
        super().__init__()

        # Luodaan säievaranto (thread pool)
        self.threadPool = QThreadPool()

        # Luodaan käyttöliittymä konvertoidun tiedoston perusteella MainWindow:n ui-ominaisuudeksi. Tämä suojaa lopun MainWindow-olion ylikirjoitukselta, kun ui-tiedostoa päivitetään
        self.ui = Ui_MainWindow()

        # Kutsutaan käyttöliittymän muodostusmetodia setupUi
        self.ui.setupUi(self)

        # OHJELMOIDUT SIGNAALIT
        # ---------------------
        
        # Kun Lainaaja-kentästä poistutaan soitetaan äänitiedosto readKey.WAV
        self.ui.lenderLineEdit.returnPressed.connect(self.playWavFileThread)

        
   
   
    # OHJELMOIDUT SLOTIT
    # ------------------


    # Soitetaan äänitiedosto, huom! @Slot() dekoraattori
    # Äänelle luodaan oma slot dekoraattoria käyttäen, jotta säikeistys
    # onnistuu. Jos yritetään kutsua suoraan sound.playWav-metodia, sen suoritus
    # jäädyttää käyttöliittumän. Tästä syystä on tehty erillinen slot, jota ei kutsuta
    # suoraan vaan playWavFileThread slotin kautta.

    # Työfunktio, joka halutaan suorittaa säikeenä
    @Slot()
    def playWavFile(self):
        sound.playWav('sounds\\readKey.wav')

    # Luodaan uusi säie, joka kutsuu työfunktiota  
    @Slot()
    def playWavFileThread(self):
        self.ui.carLineEdit.setFocus()
        self.threadPool.start(self.playWavFile)


# Luodaan sovellus
app = QtWidgets.QApplication(sys.argv)

# Luodaan objekti pääikkunalle ja tehdään siitä näkyvä
window = MainWindow()
window.show()

# Käynnistetään sovellus ja tapahtumienkäsittelijä
app.exec()

    
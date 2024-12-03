# PYSIDE6-MALLINE SOVELLUKSEN PÄÄIKKUNAN LUOMISEEN
# KÄÄNETYSTÄ KÄYTTÖLITTYMÄTIEDOSTOSTA (mainWindow_ui.py)
# ===================================================

# KIRJASTOJEN JA MODUULIEN LATAUKSET
# ----------------------------------
import os # Polkumääräykset
import sys # Käynistysargumentit

from PySide6 import QtWidgets #Qt-vimpaimet
from administrative_ui import Ui_MainWindow # Käänetyn käyttöliitymän luokka

# Märitellään luokka, joka perii QMainWindow- ja UI_MainWindow luokan
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """A class for creating main window for the application"""

    # Määritellään oliomuodostin ja kutsutaan yliluokkien muodostimia
    def __init__(self):
        super().__init__()

        # Luodaan käyttöliitymä konvertoidun tiedoston perusteella MainWindown ui-ominaisuudeksi. Tämä suojaa lopun MainWindow-olion ylikirjoitukselta
        self.ui = Ui_MainWindow()

        # Kutsutaan käyttöliittymän muodostusmetodia setupUi
        self.ui.setupUi(self)

        # OHJELMOIDUT SINGAALIT
        # ---------------------
        

      
    # OHJELMOIDUT SLOTIT
    # ------------------

    # Avataan MessageBox
    def openWarning(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Critical)
        msgBox.setWindowTitle('Hirveetä!')
        msgBox.setText('Jotian kamalaa tapahtui')
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec()

if __name__ == "__main__":
    
    # Luodaan sovellus
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('fusion')

    # Luodaan objekti pääikkunalle ja tehdään siitä näkyvä
    window = MainWindow()
    window.show()

    # Käynistetään sovellus ja tapahtumienkäsittelijä
    app.exec()
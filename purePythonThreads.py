# PYTHONIN PERUSSÄIKEISTYS
# ========================

import threading # Säikeistyksen tuki
import time

def longLastingFucntion(parameter):
    time.sleep(10) # Odotetaan 10 sekuntia
    print(parameter)

if __name__ == "__main__":

    # Luodaan säie, joka kutsuu longLastingFunktiota, funktion argumentit annetaan monikkona, vaikka niitä on vain yksi -> args=('hippopotamus',)
    thread1 = threading.Thread(target=longLastingFucntion, args=('Hippopotamus',))
    thread1.start()
    thread1.join() # Odotetaan kunnes säikeen suoritus päättyy
    print('Valmis')
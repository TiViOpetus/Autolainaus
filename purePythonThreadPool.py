# PYTHONIN SÄIEVARANTO
# ====================

import concurrent.futures # Säievarantojen luominen
import time # Viiveiden tuottaminen

# Työfunktio, jota suoritetaan säikeessä
def longLastingFucntion(parameter):
    time.sleep(10) # Odotetaan 10 sekuntia
    print(parameter)

if __name__ == "__main__":
    
    # Luodaan säievaranto
    pool = concurrent.futures.ThreadPoolExecutor()

    # Luodaan säie, jossa suoritetaan työfunktiota
    pool.submit(longLastingFucntion('Hippopotamus'))

    # Tulostetaan pääsäikeen olevan valmis
    print('Valmis')
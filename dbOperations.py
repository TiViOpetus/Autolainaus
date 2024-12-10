# MODUULI POSTGRESQL TIETOKANTAPALVELIMEN KÄYTTÄMISEEN
<<<<<<< HEAD
# ==================================================== 
=======
# ====================================================
>>>>>>> 07b16a6a85c7ac39b1c1e5023662ba758a545000

# KIRJASTOT JA MODUULIT
# ---------------------

import psycopg2

# LUOKAT
# ------

class DbConnection():
<<<<<<< HEAD
    """A class to create PostgreSQL Database connection and various data operations"""
    def __init__(self, settings: dict):
        self.server = settings['server']
        self.port = settings['port']
        self.database = settings['database']
        self.userName = settings['username']
        self.password = settings['password']
=======
    """A class to crate PostgreSQL Database connections and various data operations"""
    
    # Konstruktori
    def __init__(self, settings: dict):
        self.server = settings['server']
        self.port = settings['port']
        self.databaseName = settings['database']
        self.userName = settings['username']
        self.password = settings['password']
    

    
>>>>>>> 07b16a6a85c7ac39b1c1e5023662ba758a545000

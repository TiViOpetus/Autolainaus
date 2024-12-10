# MODUULI POSTGRESQL TIETOKANTAPALVELIMEN KÄYTTÄMISEEN
# ==================================================== 

# KIRJASTOT JA MODUULIT
# ---------------------

import psycopg2

# LUOKAT
# ------

class DbConnection():
    """A class to create PostgreSQL Database connection and various data operations"""
    def __init__(self, settings: dict):
        self.server = settings['server']
        self.port = settings['port']
        self.database = settings['database']
        self.userName = settings['username']
        self.password = settings['password']
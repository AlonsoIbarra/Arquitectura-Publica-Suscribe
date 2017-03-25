import sqlite3

rutadb = "datos/Monitor.sqlite"


class Conexion():
    def __init__(self):
        self.con = sqlite3.connect(rutadb)

    def abrir(self):
        self.cursor = self.con.cursor()

    def ejecutaSQL(self, sSQL):
        self.cursor.execute(sSQL)
        self.con.commit()

    def ejecutaSELECT(self, sSQL):
        self.cursor.execute(sSQL)
        return self.cursor.fetchall()

    def ejecutaBusqueda(self, sSQL):
        self.cursor.execute(sSQL)
        return self.cursor.fetchone()

    def cerrar(self):
        self.cursor.close()
        self.con.close()

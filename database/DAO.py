from database.DB_connect import DBConnect
from model.fermata import Fermata
from model.connessione import Connessione

class DAO():


    @staticmethod
    def readAllFermate():
        cnx = DBConnect.get_connection()

        result = []
        if cnx is None:
            print('Connection failed.')
            return None
        else :
            cursor = cnx.cursor(dictionary=True)
            query = """ SELECT * FROM fermata"""
            cursor.execute(query)

            for row in cursor :
                fermata = Fermata(row['id_fermata'], row['nome'])
                result.append(fermata)

        return result

    @staticmethod
    def searchViciniAFermata(u : Fermata):
        cnx = DBConnect.get_connection()

        result = []
        if cnx is None:
            print('Connection failed.')
            return None
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT *
                       FROM connessione
                       WHERE id_stazP = %s
"""
            cursor.execute(query, (u.id_fermata,))

            for row in cursor:
                fermata = Connessione(row['id_connessione'], row['id_linea'], row['id_stazP'], row['id_stazA'])
                result.append(fermata)

        return result
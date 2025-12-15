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
                fermata = Fermata(row['id_fermata'], row['nome'], row['coordX'], row['coordY'])
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
                connessione = Connessione(row['id_connessione'], row['id_linea'], row['id_stazP'], row['id_stazA'])
                result.append(connessione)

            cursor.close()
            cnx.close()
            return result

    @staticmethod
    def readAllConnessioni():
        cnx = DBConnect.get_connection()

        result = []
        if cnx is None:
            print('Connection failed.')
            return None
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """ SELECT * FROM connessione """
            cursor.execute(query)

            for row in cursor:
                connessione = Connessione(row['id_connessione'], row['id_linea'], row['id_stazP'], row['id_stazA'])
                result.append(connessione)

            cursor.close()
            cnx.close()
            return result

    @staticmethod
    def readVelocita(linea):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print('Connection failed.')
            return None
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """ SELECT * FROM linea WHERE id_linea = %s"""
            cursor.execute(query, (linea,))

            for row in cursor:
                result.append(row['velocita'])

            cursor.close()
            cnx.close()
            return result[0]
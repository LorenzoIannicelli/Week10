from database.DB_connect import DBConnect
from model.fermata import Fermata

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
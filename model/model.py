from database.DAO import DAO

class Model:
    def __init__(self):
        self._lista_fermate = []
        self._dizionario_fermate = {}       # key = id_fermata ; value = oggetto fermata

    def get_all_fermate(self):
        fermate = DAO.readAllFermate()
        self._lista_fermate = fermate

        for fermata in fermate :
            self._dizionario_fermate[fermata.id_fermata] = fermata

        return self._lista_fermate
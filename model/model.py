from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._lista_fermate = []
        self._dizionario_fermate = {}       # key = id_fermata ; value = oggetto fermata
        self._grafo = None

    def get_all_fermate(self):
        fermate = DAO.readAllFermate()
        self._lista_fermate = fermate

        for fermata in fermate :
            self._dizionario_fermate[fermata.id_fermata] = fermata

        return self._lista_fermate

    def creaGrafo(self):
        self._grafo = nx.Graph()
        for fermata in self._lista_fermate:
            self._grafo.add_node(fermata)

        for fermata in self._grafo :
            connessioni = DAO.searchViciniAFermata(fermata)

            for fermata_vicina in connessioni:
                fermata_connessa = self._dizionario_fermate[fermata_vicina.id_stazA]
                self._grafo.add_edge(fermata, fermata_connessa)
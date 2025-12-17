from database.DAO import DAO
import networkx as nx
from geopy.distance import geodesic

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
        self._grafo = nx.DiGraph()
        for fermata in self._lista_fermate:
            self._grafo.add_node(fermata)

        '''for fermata in self._grafo :
            connessioni = DAO.searchViciniAFermata(fermata)

            for fermata_vicina in connessioni:
                fermata_connessa = self._dizionario_fermate[fermata_vicina.id_stazA]
                self._grafo.add_edge(fermata, fermata_connessa)'''


        connessioni = DAO.readAllConnessioni()

        for c in connessioni :
            stazP = self._dizionario_fermate[c.id_stazP]
            stazA = self._dizionario_fermate[c.id_stazA]
            velocita = DAO.readVelocita(c.id_linea)

            punto_P = (stazP.coordX, stazP.coordY)
            punto_A = (stazA.coordX, stazA.coordY)

            distanza = geodesic(punto_P, punto_A).km

            # Calcolo del tempo di percorrenza in minuti
            tempo_perc = distanza / velocita * 60

            #print(stazP, stazA, punto_P, punto_A)

            if (self._grafo.has_edge(punto_P, punto_A)):
                if (self._grafo[stazP][stazA] > tempo_perc):
                    self._grafo[stazP][stazA]['tempo'] = tempo_perc
            else:
                self._grafo.add_edge(stazP, stazA, tempo = tempo_perc)

            #print(f'Aggiunto arco tra {stazP} e {stazA}, tempo: {self._grafo[stazP][stazA]}')

        print('Grafo creato con successo!')


    def getRaggiungibili(self, idStazP):
        result = []
        stazP = self._dizionario_fermate[idStazP]
        for u, v in nx.bfs_edges(self._grafo, stazP):
            result.append(v)

        return result

    def getPercorsoMinimo(self, idStazP, idStazA):
        objStazP = self._dizionario_fermate[idStazP]
        objStazA = self._dizionario_fermate[idStazA]

        tempo, perc_min = nx.single_source_dijkstra(self._grafo, objStazP, objStazA)

        return tempo, perc_min
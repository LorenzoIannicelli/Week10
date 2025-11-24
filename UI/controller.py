import flet as ft

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCreaGrafo(self,e):
        pass

    def handleCercaRaggiungibili(self,e):
        pass

    def populate_dropdown(self, dd):
        fermate = self._model.get_all_fermate()
        for fermata in fermate:
            dd.options.append(ft.dropdown.Option(text=fermata.nome, key=fermata.id_fermata))
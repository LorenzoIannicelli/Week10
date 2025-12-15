import flet as ft

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCreaGrafo(self,e):
        self._model.creaGrafo()
        self._view.lst_result.controls.clear()
        self._view.lst_result.controls.append(ft.Text(f'{self._model._grafo}'))

        for f1, f2, w in self._model._grafo.edges(data=True):
            temp_perc = w['tempo']
            self._view.lst_result.controls.append(ft.Text(f'{f1} -> {f2}, Tempo percorrenza: {temp_perc}'))

        self._view.update_page()

    def handleCercaRaggiungibili(self,e):
        idStazP = int(self._view._ddStazPartenza.value)
        raggiungibili = self._model.getRaggiungibili(idStazP)
        self._view.lst_result.controls.clear()

        for f in raggiungibili:
            self._view.lst_result.controls.append(ft.Text(f'{f}'))

        self._view.update_page()

    def populate_dropdown(self, dd):
        fermate = self._model.get_all_fermate()
        for fermata in fermate:
            dd.options.append(ft.dropdown.Option(text=fermata.nome, key=fermata.id_fermata))
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore

import AppLoop
import Models
import SignalMng
import Store
from Utils import EditorModelDict
from resources.Main import Ui_MainWindow


class UIMainViewControl(QMainWindow):
    curr_factory: Store.FactoryModel = None

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.content = Ui_MainWindow()
        self.content.setupUi(self)

        m = EditorModelDict(Store.facts)
        self.content.list_facts.setModel(m)

        self.content.bar_current.setMinimum(0)

        self.content.list_facts.selectionModel().currentChanged.connect(self.on_fact_changed)

        SignalMng.TICK += self.on_tick
        SignalMng.FACTORY_STARTED += self.on_factory_started
        SignalMng.FACTORY_COLLECTED += self.on_factory_collected

    def on_factory_started(self, id):
        if self.curr_factory is not None and self.curr_factory.id == id:
            self.update_current_progress_bar()

    def on_factory_collected(self, id):
        if self.curr_factory is not None and self.curr_factory.id == id:
            self.update_current_progress_bar()

    def __exit__(self, exc_type, exc_value, traceback):
        SignalMng.TICK -= self.on_tick
        SignalMng.FACTORY_STARTED -= self.on_factory_started
        SignalMng.FACTORY_COLLECTED -= self.on_factory_collected

    def on_tick(self, delta_time):
        if self.curr_factory is not None:
            self.content.bar_current.setValue(AppLoop.cur_time)

    def on_fact_changed(self, current, prev):
        fct = current.model().data(current, QtCore.Qt.UserRole)
        self.update_factory_view(fct)

    def update_factory_view(self, factory: Store.FactoryModel):
        self.curr_factory = factory

        if self.curr_factory is None:
            self.content.txt_name.setText("")
            self.content.txt_per_sec.setText("")
        else:
            recipe = Store.get_recipe(self.curr_factory.recipe)
            self.content.txt_name.setText(factory.name)
            self.content.txt_per_sec.setText(str(round((1 / recipe.time) * 1000, 2)))

        self.update_current_progress_bar()

    def update_current_progress_bar(self):
        recipe = Store.get_recipe(self.curr_factory.recipe)
        if self.curr_factory is None:
            self.content.bar_current.setMinimum(0)
            self.content.bar_current.setMaximum(0)
        elif self.curr_factory.state == Models.FACTORY_STATE_EMPTY:
            self.content.bar_current.setMinimum(0)
            self.content.bar_current.setMaximum(recipe.time)
            self.content.bar_current.setValue(0)
        else:
            self.content.bar_current.setMinimum(self.curr_factory.start_time)
            self.content.bar_current.setMaximum(self.curr_factory.start_time + recipe.time)
            self.content.bar_current.setValue(AppLoop.cur_time)

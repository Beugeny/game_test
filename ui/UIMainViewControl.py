from typing import TypeVar

from PyQt5.QtCore import QItemSelectionModel
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore

import AppLoop
from FactoryController import FactoryController
import Models
import SignalMng
import Store
from Utils import ModelDict, ModelList
from resources.Main import Ui_MainWindow


def get_item_name(item: Store.ItemPoint):
    m = Store.get_item(item.id)
    if m:
        return m.name
    return ""


class UIMainViewControl(QMainWindow):
    curr_factory = None  # TODO type annotations

    curr_factory_control = None  # TODO type annotations

    def cfc(self) -> FactoryController:
        return self.curr_factory_control

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.content = Ui_MainWindow()
        self.content.setupUi(self)

        self.content.tabs.setCurrentIndex(0)
        self.content.tabs.currentChanged.connect(self.on_tab_changed)

        m = ModelDict(Store.facts)
        self.content.list_facts.setModel(m)
        self.content.list_facts.selectionModel().currentChanged.connect(self.on_fact_changed)
        self.content.list_facts.setCurrentIndex(m.index(0, 0))

        self.content.bar_current.setMinimum(0)
        self.content.cbx_enable.stateChanged.connect(self.change_fact_enabled)

        SignalMng.TICK += self.on_tick

    def on_tab_changed(self):
        print(self.content.tabs.currentIndex())

    def change_fact_enabled(self, v):
        if self.cfc() is not None:
            self.cfc().change_enabled(self.content.cbx_enable.isChecked())

    def __exit__(self, exc_type, exc_value, traceback):
        SignalMng.TICK -= self.on_tick
        SignalMng.FACTORY_CRAFT_STARTED -= self.on_factory_started
        SignalMng.FACTORY_COLLECTED -= self.on_factory_collected

    def on_tick(self, delta_time):
        if self.curr_factory is not None:
            self.update_current_progress_bar()

    def on_fact_changed(self, current, prev):
        fct = current.model().data(current, QtCore.Qt.UserRole)
        self.update_factory_view(fct)

    def update_factory_view(self, factory: Store.FactoryModel):
        self.curr_factory = factory
        self.curr_factory_control = Store.get_fact_control(factory.id)

        if self.curr_factory is None:
            self.content.txt_name.setText("")
            self.content.txt_per_sec.setText("")
        else:
            recipe = Store.get_recipe(self.curr_factory.recipe)
            self.content.txt_name.setText(factory.name)
            self.content.txt_per_sec.setText(str(round((1 / recipe.time) * 1000, 2)))

        self.update_current_progress_bar()
        self.update_current_recipe()
        self.update_enabled()

    def update_enabled(self):
        self.content.cbx_enable.setChecked(self.curr_factory.enabled)
        if self.content.cbx_enable.isChecked():
            self.content.cbx_enable.setText("Включено")
        else:
            self.content.cbx_enable.setText("Выключено")

    def update_current_recipe(self):
        if self.curr_factory is None:
            self.content.list_out.setModel(None)
        else:
            recipe = Store.get_recipe(self.curr_factory.recipe)
            m_in = ModelList(recipe.input, label_field=get_item_name) if recipe.input is not None else ModelList(
                [], label_field=get_item_name)
            m_out = ModelList(recipe.out, label_field=get_item_name) if recipe.out is not None else ModelList(
                [], label_field=get_item_name)

            self.content.list_out.setModel(m_in)
            self.content.list_in.setModel(m_out)

    def update_current_progress_bar(self):
        if self.curr_factory is None:
            return
        curr, min, max = self.cfc().get_progress()
        self.content.bar_current.setValue(curr)
        self.content.bar_current.setMaximum(max)

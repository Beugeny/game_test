from functools import partial

from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow

import Models
import SignalMng
import StorageController
import Store
from FactoryController import FactoryController
from Utils import ModelDict, ModelList
from resources.Main import Ui_MainWindow


def get_item_label(item: Store.ItemPoint):
    m = Store.get_item(item.id)
    if m:
        return "{0} {1}шт.".format(m.name, item.count)
    return ""


def get_item_label_with_cost(item: Store.ItemPoint):
    m = Store.get_item(item.id)
    if m:
        return "{0} {1}шт. ={2} монет".format(m.name, item.count, m.cost * item.count)
    return ""


class UIMainViewControl(QMainWindow):
    curr_factory = None
    curr_factory_control = None
    curr_storage = None

    def get_fact_control(self) -> FactoryController:
        return self.curr_factory_control

    def get_storage(self) -> Models.StorageModel:
        return self.curr_storage

    def get_fact(self) -> Models.FactoryModel:
        return self.curr_factory

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)

        self.content = Ui_MainWindow()
        self.content.setupUi(self)

        self.content.tabs.setCurrentIndex(0)
        self.content.tabs.currentChanged.connect(self.on_tab_changed)

        self.content.btn_factory_upgrade.clicked.connect(self.upg_fact)

        m = ModelDict(Store.facts)
        self.content.list_facts.setModel(m)
        self.content.list_facts.selectionModel().currentChanged.connect(self.on_fact_changed)
        self.content.list_facts.setCurrentIndex(m.index(0, 0))

        self.content.bar_current.setMinimum(0)
        self.content.cbx_enable.stateChanged.connect(self.change_fact_enabled)

        m = ModelDict(Store.storages)
        self.content.list_storages.setModel(m)
        self.content.list_storages.selectionModel().currentChanged.connect(self.on_storage_changed)
        self.content.list_storages.setCurrentIndex(m.index(0, 0))

        self.content.btn_sell_1.clicked.connect(partial(self.on_sell_clicked, 1))
        self.content.btn_sell_10.clicked.connect(partial(self.on_sell_clicked, 10))
        self.content.btn_sell_all.clicked.connect(partial(self.on_sell_clicked, -1))

        self.on_coins_changed()

        SignalMng.TICK += self.on_tick
        SignalMng.PROCESS_ITEM += self.on_proccess_item
        SignalMng.COINS_CHANGED += self.on_coins_changed

    def upg_fact(self):
        if Store.playerResources.coins >= self.get_fact().upg_cost():
            Store.playerResources.coins -= self.get_fact().upg_cost()
            self.get_fact().current_upgrade_index += 1
            self.update_factory_view()

    def update_fact_upgrade(self):
        d = self.get_fact().get_next_delta_time() / self.get_fact().get_recipe_time() * 100
        self.content.txt_fact_next.setText("Время производства {0}%".format(round(d, 2)))

        self.content.btn_factory_upgrade.setText("Улучшить {0} монет".format(self.get_fact().next_upg_cost()))

    def on_sell_clicked(self, count):
        l = self.content.list_storage_elements
        indexes = l.selectedIndexes()

        items = [l.model().data(index, QtCore.Qt.UserRole) for index in indexes]
        if count < 0:
            [StorageController.sell_item(item.id, item.count) for item in items]
        else:
            [StorageController.sell_item(item.id, count) for item in items]

    def on_coins_changed(self):
        self.content.txt_player_coins.setText("Ресурсов игрока {0}".format(Store.playerResources.coins))

    def on_proccess_item(self, item: Models.ItemPoint):
        if self.content.tabs.currentIndex() == 1:
            if self.get_storage() and self.get_storage().is_storage_item(item.id):
                self.update_storage_capacity()

    def on_tab_changed(self):
        if self.content.tabs.currentIndex() == 0:
            self.update_factory_view()
        elif self.content.tabs.currentIndex() == 1:
            self.update_storage_view()

    def change_fact_enabled(self, v):
        if self.get_fact_control() is not None:
            self.get_fact_control().change_enabled(self.content.cbx_enable.isChecked())

    def __exit__(self, exc_type, exc_value, traceback):
        SignalMng.TICK -= self.on_tick
        SignalMng.PROCESS_ITEM -= self.on_proccess_item

    def on_tick(self, delta_time):
        if self.curr_factory is not None:
            self.update_current_progress_bar()

    def on_fact_changed(self, current, prev):
        self.curr_factory = current.model().data(current, QtCore.Qt.UserRole)
        self.curr_factory_control = Store.get_fact_control(self.curr_factory.id)
        self.update_factory_view()

    def on_storage_changed(self, current, prev):
        self.curr_storage = current.model().data(current, QtCore.Qt.UserRole)
        self.update_storage_view()

    def update_storage_view(self):
        self.content.txt_storage_name.setText(self.get_storage().name)
        m = ModelList(self.get_storage().get_item_points(), label_field=get_item_label_with_cost)
        self.content.list_storage_elements.setModel(m)

        self.update_storage_capacity()

    def update_storage_capacity(self):
        self.content.txt_storage_capacity.setText(
            "{0}/{1}".format(self.get_storage().current_count(), self.get_storage().max_count))
        self.content.bar_storage_capacity.setMaximum(self.get_storage().max_count)
        self.content.bar_storage_capacity.setValue(self.get_storage().current_count())

    def update_factory_view(self):
        self.content.txt_name.setText(self.curr_factory.name)
        self.content.txt_per_sec.setText(str(round((1 / self.curr_factory.get_recipe_time()) * 1000, 2)))

        self.update_current_progress_bar()
        self.update_current_recipe()
        self.update_enabled()
        self.update_fact_upgrade()

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
            m_in = ModelList(recipe.input, label_field=get_item_label) if recipe.input is not None else ModelList(
                [], label_field=get_item_label)
            m_out = ModelList(recipe.out, label_field=get_item_label) if recipe.out is not None else ModelList(
                [], label_field=get_item_label)

            self.content.list_out.setModel(m_in)
            self.content.list_in.setModel(m_out)

    def update_current_progress_bar(self):
        if self.curr_factory is None:
            return
        curr, min, max = self.get_fact_control().get_progress()
        self.content.bar_current.setValue(curr)
        self.content.bar_current.setMaximum(max)

import AppLoop
import Models
import SignalMng
import Store
from StorageController import *
import time, threading

from Utils import TimeControl


class FactoryController:
    def __init__(self, factory: Store.FactoryModel):
        super().__init__()
        self.timer = TimeControl()
        self.timer = TimeControl()
        factory.state = Models.FACTORY_STATE_EMPTY
        self.locked = False
        self.factory = factory
        self.recipe = Store.get_recipe(factory.recipe)

        SignalMng.PROCESS_ITEM += self.on_proccess_item
        self.timer += self.on_time_complete

    def state_empty(self):
        if has_recipe_needs(self.recipe):
            self.factory.start_time = AppLoop.cur_time
            self.factory.state = Models.FACTORY_STATE_CURRENT
            self.locked = True
            process_items(self.recipe.input, False)
            self.locked = False

            self.timer.start(AppLoop.cur_time + self.recipe.time - self.factory.start_time)
            SignalMng.FACTORY_STARTED.dispatch(self.factory.id)
            self.state_current()

    def state_current(self):
        if self.is_time_complete():
            self.state_collect()

    def is_time_complete(self):
        AppLoop.cur_time + self.recipe.time <= self.factory.start_time

    def state_collect(self):
        if check_storage_for_recipe(self.recipe):
            self.locked = True
            process_items(self.recipe.out)
            self.locked = False
            self.factory.state = Models.FACTORY_STATE_EMPTY
            SignalMng.FACTORY_COLLECTED.dispatch(self.factory.id)
            self.state_empty()

    def on_proccess_item(self, item: Store.ItemPoint):
        if self.locked is True:
            return
        if self.factory.state == Models.FACTORY_STATE_EMPTY:
            self.state_empty()
        elif self.factory.state == Models.FACTORY_STATE_WAIT_COLLECT:
            self.state_collect()

    def on_time_complete(self):
        self.factory.state = Models.FACTORY_STATE_WAIT_COLLECT
        SignalMng.FACTORY_CRAFT_COMPLETE.dispatch(self.factory.id)
        self.state_collect()

    def destroy(self):
        if self.timer is not None:
            self.timer.reset()
        SignalMng.PROCESS_ITEM -= self.on_proccess_item
        self.timer -= self.on_time_complete

    def start(self):
        if self.factory.state == Models.FACTORY_STATE_EMPTY:
            self.state_empty()
        elif self.factory.state == Models.FACTORY_STATE_CURRENT:
            self.state_current()
        elif self.factory.state == Models.FACTORY_STATE_WAIT_COLLECT:
            self.state_collect()

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
        factory.state = Models.FACTORY_STATE_EMPTY
        self.factory = factory
        self.recipe = Store.get_recipe(factory.recipe)

        SignalMng.PROCESS_ITEM += self.on_proccess_item

    def destroy(self):
        SignalMng.PROCESS_ITEM -= self.on_proccess_item
        SignalMng.TICK -= self.on_craft_tick

    def start(self):
        if self.factory.state == Models.FACTORY_STATE_EMPTY:
            self.try_start_craft()
        elif self.factory.state == Models.FACTORY_STATE_CURRENT:
            SignalMng.TICK += self.on_craft_tick
        elif self.factory.state == Models.FACTORY_STATE_WAIT_COLLECT:
            self.try_to_collect()

    def try_start_craft(self):
        if self.factory.enabled and has_recipe_needs(self.recipe):
            self.factory.start_time = AppLoop.cur_time
            self.factory.state = Models.FACTORY_STATE_CURRENT
            self.factory.progress_time = 0
            process_items(self.recipe.input, False)
            SignalMng.FACTORY_CRAFT_STARTED.dispatch(self.factory.id)
            SignalMng.TICK += self.on_craft_tick

    def on_craft_tick(self, delta_time):
        self.factory.progress_time += delta_time
        if self.factory.progress_time >= self.recipe.time:
            self.factory.progress_time = self.recipe.time
            self.stop_craft()
            self.try_to_collect()

    def stop_craft(self):
        self.factory.state = Models.FACTORY_STATE_WAIT_COLLECT
        SignalMng.TICK -= self.on_craft_tick
        SignalMng.FACTORY_CRAFT_COMPLETE.dispatch(self.factory.id)

    def on_proccess_item(self, item: Store.ItemPoint):
        if self.factory.state == Models.FACTORY_STATE_EMPTY:
            self.try_start_craft()
        elif self.factory.state == Models.FACTORY_STATE_WAIT_COLLECT:
            self.try_to_collect()

    def try_to_collect(self):
        if check_storage_for_recipe(self.recipe):
            self.factory.progress_time = 0
            self.factory.state = Models.FACTORY_STATE_EMPTY
            SignalMng.FACTORY_COLLECTED.dispatch(self.factory.id)
            process_items(self.recipe.out)

    def get_progress(self)->tuple:
        if self.factory is None:
            return 0, 0, 0
        else:
            return self.factory.progress_time, 0, self.recipe.time

    def change_enabled(self, value: bool):
        if self.factory.enabled == value:
            return
        else:
            self.factory.enabled = value
            if self.factory.enabled is True:
                self.start()
            else:
                if self.factory.state == Models.FACTORY_STATE_CURRENT:
                    SignalMng.TICK -= self.on_craft_tick


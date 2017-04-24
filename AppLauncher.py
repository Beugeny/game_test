
import ui.MainView

import SignalMng
import Store
from FactoryController import FactoryController


def on_proccess_item(item: Store.ItemPoint):
    pass
    # print(item)
    # print(Store.storages)


def on_factory_complete(id: int):
    # pass
    print("Был скрафчен элемент на фабрике={0}".format(id))


Store.init()

# SignalMng.PROCESS_ITEM += on_proccess_item
# SignalMng.FACTORY_CRAFT_COMPLETE += on_factory_complete

fact_controls = [FactoryController(f) for f in Store.facts.values()]
[f.start() for f in fact_controls]


ui.MainView.show_main()

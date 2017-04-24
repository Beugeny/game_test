import Store
import ui.MainView
from FactoryController import FactoryController

Store.init()

fact_controls = [FactoryController(f) for f in Store.facts.values()]
for f in fact_controls:
    Store.fact_controls[f.factory.id] = f
    f.start()

ui.MainView.show_main()

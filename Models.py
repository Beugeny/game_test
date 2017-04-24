from nltk.sem.logic import typecheck

import SignalMng


class RecipeModel:
    id = 0
    time = 0
    out = []
    input = []

    def __init__(self, id, time, out, input=None):
        super().__init__()
        self.input = input
        self.out = out
        self.time = time
        self.id = id

    def __str__(self, *args, **kwargs):
        return "RecipeModel:: id={0} time={1} in={2} out={3}".format(self.id, self.time, self.input, self.out)

    def __repr__(self, *args, **kwargs):
        return self.__str__(*args, **kwargs)


FACTORY_STATE_EMPTY = "EMPTY"
FACTORY_STATE_CURRENT = "CURRENT"
FACTORY_STATE_WAIT_COLLECT = "WAIT_COLLECT"


class FactoryModel:
    id = 0
    name = ""
    recipe = 0
    start_time = 0  # Время старта крафта
    progress_time = 0  # Сколько крафтилось выражено в пройденном времени
    enabled = True
    state = FACTORY_STATE_EMPTY

    def __init__(self, id, name, recipe):
        super().__init__()
        self.recipe = recipe
        self.name = name
        self.id = id

    def __str__(self, *args, **kwargs):
        return "FactoryModel:: id={0} name={1} recipe={2}".format(self.id, self.name, self.recipe)

    def __repr__(self, *args, **kwargs):
        return self.__str__(*args, **kwargs)


class StorageModel:
    def __init__(self, id, name, max_count, items=None):
        super().__init__()
        if items is not None:
            self.items = items
        self.max_count = max_count
        self.name = name
        self.id = id

    def current_count(self):
        return sum([x for x in self.items.values()]) if self.items is not None else 0

    id = 0
    name = ""
    max_count = 0
    items = dict()

    def __str__(self, *args, **kwargs):
        return "StorageModel:: id={0} name={1} count={2}/{3}".format(self.id, self.name, self.current_count(),
                                                                     self.max_count)

    def __repr__(self, *args, **kwargs):
        return self.__str__(*args, **kwargs)

    def get_item_count(self, id):
        if id in self.items:
            return self.items[id]
        return 0

    def append_item(self, item, positive):
        if item.count == 0:
            return

        if item.id in self.items:
            if positive is True:
                self.items[item.id] += item.count
            else:
                self.items[item.id] -= item.count
        else:
            if positive is True:
                self.items[item.id] = item.count
            else:
                self.items[item.id] = -item.count
        if self.items[item.id] < 0:
            raise Exception("Storage item count<0")
        SignalMng.PROCESS_ITEM.dispatch(item)


class ItemModel:
    def __init__(self, id, name, storage):
        super().__init__()
        self.storage = storage
        self.name = name
        self.id = id

    id = 0
    name = ""
    storage = 0

    def __str__(self, *args, **kwargs):
        return "ItemModel:: id={0} name={1}".format(self.id, self.name)

    def __repr__(self, *args, **kwargs):
        return self.__str__(*args, **kwargs)


class ItemPoint:
    def __init__(self, id, count):
        super().__init__()
        self.count = count
        self.id = id

    id = 0
    count = 0

    def __str__(self, *args, **kwargs):
        return "ItemPoint:: id={0} count={1}".format(self.id, self.count)

    def __repr__(self, *args, **kwargs):
        return self.__str__(*args, **kwargs)

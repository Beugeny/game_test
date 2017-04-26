from typing import List
import SignalMng
import Store


class PlayerResources:
    def __init__(self, start_coins=0):
        super().__init__()
        self._coins = start_coins

    @property
    def coins(self) -> int:
        return self._coins

    @coins.setter
    def coins(self, value: int):
        if self._coins == value:
            return
        self._coins = value
        SignalMng.COINS_CHANGED.dispatch()


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

    def __init__(self, id, name, recipe, upgrades: List['FactoryUpgrade']):
        super().__init__()
        self.recipe = recipe
        self.name = name
        self.id = id
        self.recipe_model = Store.get_recipe(self.recipe)
        self.upgrades = upgrades
        self.current_upgrade_index = 0

    def __str__(self, *args, **kwargs):
        return "FactoryModel:: id={0} name={1} recipe={2}".format(self.id, self.name, self.recipe)

    def __repr__(self, *args, **kwargs):
        return self.__str__(*args, **kwargs)

    def get_recipe_time(self):
        return self.upgrades[self.current_upgrade_index].time_k * self.recipe_model.time

    def get_next_recipe_time(self):
        return self.upgrades[self.current_upgrade_index + 1].time_k * self.recipe_model.time

    def get_next_delta_time(self):
        return self.get_next_recipe_time() - self.get_recipe_time()

    def upg_cost(self):
        return self.upgrades[self.current_upgrade_index].cost


class FactoryUpgrade:
    time_k = 1
    cost = 0

    def __init__(self, k: float, cost: int):
        super().__init__()
        self.time_k = k
        self.cost = cost


class StorageUpgrade:
    counts = 1
    cost = 0

    def __init__(self, counts: int, cost: int):
        super().__init__()
        self.counts = counts
        self.cost = cost


class StorageModel:
    id = 0
    name = ""
    items = dict()

    item_points = None

    def __init__(self, id, name, max_count, upgrades: List['StorageUpgrade'], items=None):
        super().__init__()
        if items is not None:
            self.items = items
        self.name = name
        self.id = id
        self.item_points = [ItemPoint(id, count) for id, count in self.items.items()]
        self.upgrades = upgrades
        self.current_upgrade_index = 0

    def get_item(self, id: int) -> 'ItemPoint':
        for item in self.item_points:
            if item.id == id:
                return item

    def current_count(self):
        return sum([x for x in self.items.values()]) if self.items is not None else 0

    def __str__(self, *args, **kwargs):
        return "StorageModel:: id={0} name={1} count={2}/{3}".format(self.id, self.name, self.current_count(),
                                                                     self.max_count)

    def __repr__(self, *args, **kwargs):
        return self.__str__(*args, **kwargs)

    def get_item_count(self, id):
        if id in self.items:
            return self.items[id]
        return 0

    def get_item_points(self) -> List['ItemPoint']:
        return self.item_points

    def append_item(self, item: 'ItemPoint', positive):
        if item.count == 0:
            return

        if item.id in self.items:
            if positive is True:
                self.items[item.id] += item.count
                self.get_item(item.id).count += item.count
            else:
                self.items[item.id] -= item.count
                self.get_item(item.id).count -= item.count
        else:
            if positive is True:
                self.items[item.id] = item.count
                self.item_points.append(ItemPoint(item.id, item.count))
            else:
                self.items[item.id] = -item.count
                self.item_points.append(ItemPoint(item.id, -item.count))
        if self.items[item.id] < 0:
            raise Exception("Storage item count<0")

        SignalMng.PROCESS_ITEM.dispatch(item)

    def is_storage_item(self, id):
        if id in self.items:
            return True
        return False

    @property
    def max_count(self) -> int:
        return self.upgrades[self.current_upgrade_index].counts

    @property
    def next_max_count(self) -> int:
        return self.upgrades[self.current_upgrade_index + 1].counts

    def upg_cost(self):
        return self.upgrades[self.current_upgrade_index].cost


class ItemModel:
    def __init__(self, id, name, storage, cost):
        super().__init__()
        self.storage = storage
        self.name = name
        self.id = id
        self.cost = cost

    id = 0
    name = ""
    storage = 0
    cost = 0

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

from Models import *

items = dict()
recipes = dict()
storages = dict()
facts = dict()

fact_controls = dict()


def get_fact_control(id):
    return get_by_id(id, fact_controls)


def get_recipe(id):
    """
           :rtype: RecipeModel
           """
    return get_by_id(id, recipes)


def get_item(id):
    """
    :rtype: ItemModel
    """
    return get_by_id(id, items)


def get_storage(id):
    """
        :rtype: StorageModel
        """
    return get_by_id(id, storages)


def get_by_id(id, collection):
    if isinstance(collection, dict):
        return collection.get(id)


def init():
    global items
    global recipes
    global storages
    global facts

    items[1] = ItemModel(1, "Железо", 1)
    items[2] = ItemModel(2, "Уголь", 1)
    items[3] = ItemModel(3, "Сталь", 1)

    recipes[1] = RecipeModel(1, 1000, [ItemPoint(1, 1)])
    recipes[2] = RecipeModel(2, 2000, [ItemPoint(2, 1)])
    recipes[3] = RecipeModel(3, 1500, [ItemPoint(3, 1)], [ItemPoint(1, 1), ItemPoint(2, 1)])

    storages[1] = StorageModel(1, "Склад материалов", 20)

    facts[1] = FactoryModel(1, "Добыча железа", 1)
    facts[2] = FactoryModel(2, "Добыча угля", 2)
    facts[3] = FactoryModel(3, "Плавильня", 3)



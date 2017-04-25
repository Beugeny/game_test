import Store


def has_item(item: Store.ItemPoint):
    model = Store.get_item(item.id)
    storage = Store.get_storage(model.storage)
    return storage.get_item_count(item.id) >= item.count


def has_recipe_needs(recipe):
    if recipe.input is None:
        return True
    return all([has_item(x) for x in recipe.input])


def process_item(item: 'ItemPoint', positive):
    model = Store.get_item(item.id)
    storage = Store.get_storage(model.storage)
    storage.append_item(item, positive)


def process_items(items: list, positive: bool = True):
    if items is not None:
        [process_item(x, positive) for x in items]


def check_item_to_storage(item: Store.ItemPoint):
    model = Store.get_item(item.id)
    storage = Store.get_storage(model.storage)
    return storage.current_count() + item.count <= storage.max_count


def check_storage_for_recipe(recipe: Store.RecipeModel):
    return all([check_item_to_storage(x) for x in recipe.out])

"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):

    for item in items_to_add:
        current_cart.setdefault(item, 0)
        current_cart[item] += 1

    return current_cart


def read_notes(notes):
    return dict.fromkeys(notes, 1)


def update_recipes(ideas, recipe_updates):
    ideas.update(recipe_updates)
    return ideas


def sort_entries(cart):
    return dict(sorted(cart.items()))


def send_to_store(cart, aisle_mapping):
    newDic = {}
    for key, value in cart.items():
        newDic[key] = [cart[key], aisle_mapping[key][0], aisle_mapping[key][1]]

    newDic = dict(reversed(sorted(newDic.items())))

    return newDic


def update_store_inventory(fulfillment_cart, store_inventory):
    for key in fulfillment_cart.keys():
        rest = store_inventory[key][0] - fulfillment_cart[key][0]

        store_inventory[key][0] = rest if rest > 0 else "Out of Stock"

    return store_inventory

def read_cook_book(txt):
    cook_book = {}
    with open(txt) as f:
        file = f.read()
        recipes = file.split(sep="\n\n")

        for recipe in recipes:
            ingredients = []
            recipe = recipe.split(sep="\n")

            for ingredient in recipe[2:]:
                ingredient = ingredient.split(sep=" | ")
                ingredient = {
                    "ingredient_name": ingredient[0],
                    "quantity": int(ingredient[1]),
                    "measure": ingredient[2],
                }
                ingredients.append(ingredient)

            cook_book[recipe[0]] = ingredients
    return cook_book


cook_book = read_cook_book("recipes.txt")


def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    for dish in dishes:
        ingredients = cook_book[dish]
        for ingredient in ingredients:

            if ingredient["ingredient_name"] in result:
                result[ingredient["ingredient_name"]]["quantity"] += ingredient["quantity"] * person_count
            else:
                result[ingredient["ingredient_name"]] = {
                    "quantity": ingredient["quantity"] * person_count,
                    "measure": ingredient["measure"],
                }

    return result

print(get_shop_list_by_dishes(["Омлет", "Фахитос"], 2))

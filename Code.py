
with open("recipes.txt") as f:
    ingredients = []
    cook_book = {}
    while True:
        dish_name = f.readline().strip()
        if not dish_name:
            break
        number_of_entries = f.readline()
        ingredients = []
        for ingredient in range(int(number_of_entries)):
            ingredients_dict = {}
            ingredient = f.readline().strip().split("|")
            ingredient_name, quantity, measure = ingredient
            ingredients_dict["ingredient_name"] = ingredient_name
            ingredients_dict["quantity"] = quantity
            ingredients_dict["measure"] = measure
            ingredients.append(ingredients_dict)
        cook_book[dish_name] = ingredients
        f.readline()
    print(cook_book)
    print()



def get_shop_list_by_dishes(dishes, person_count):
    # print(type(person_count))
    shop_dict = {}
    result_dict = {}
    for dish in dishes:
        # print(dish)
        for (key, value) in cook_book.items():
            if dish == key:
                # print(key, value)
                # print(type(value))
                # print(len(value))
                for entry in value:
                    # print(entry)
                    k = (entry["ingredient_name"]).strip()
                    # print(k)
                    l = (entry["measure"]).strip()
                    m = int((entry["quantity"]).strip())
                    # m = int(m)
                    # print(type(m))
                    if k in result_dict.keys():
                        # print("Такой ингредиент уже есть")
                        # print(result_dict[k]["quantity"])
                        result_dict[k]["quantity"] =  m * person_count + (result_dict[k]['quantity'])
                        # print(result_dict[k]["quantity"])
                    else:
                        result_dict[k] = {"measure": l, "quantity": m * person_count}
    print(result_dict)



get_shop_list_by_dishes(["Омлет", "Фахитос"], 2)
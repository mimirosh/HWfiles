def parse_ingredient(line):
    name, quantity, measure = line.strip().split(' | ')
    return {
        'ingredient_name': name,
        'quantity': int(quantity),
        'measure': measure
    }

def read_cook_book(file_name):
    cook_book = {}
    with open(file_name) as file:
        while True:
            dish_name = file.readline().strip()
            if not dish_name:
                break  # Конец файла
            ingredients_count = int(file.readline().strip())
            ingredients = []
            for _ in range(ingredients_count):
                ingredient_line = file.readline()
                ingredients.append(parse_ingredient(ingredient_line))
            cook_book[dish_name] = ingredients
            file.readline() 
        return cook_book
    
def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                if ingredient['ingredient_name'] not in shop_list:
                    shop_list[ingredient['ingredient_name']] = {'measure': ingredient['measure'], 'quantity': ingredient['quantity'] * person_count}
                else:
                    shop_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
    return shop_list



cook_book = read_cook_book('recipes.txt')
shop_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
print(cook_book)
print()
print(shop_list)

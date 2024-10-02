import os

def read_cookbook(file_path):
    
    cook_book = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        while True:
            dish_name = file.readline().strip()
            if not dish_name:  
                break
            
            ingredient_count = int(file.readline().strip())
            ingredients = []
            
            for _ in range(ingredient_count):
                ingredient_line = file.readline().strip()
                ingredient_name, quantity, measure = ingredient_line.split(' | ')
                ingredients.append({
                    'ingredient_name': ingredient_name,
                    'quantity': int(quantity),
                    'measure': measure
                })
            
            cook_book[dish_name] = ingredients
    
    return cook_book

def get_shop_list_by_dishes(dishes, person_count, cook_book):
    
    shop_list = {}

    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count
                measure = ingredient['measure']

                if name not in shop_list:
                    shop_list[name] = {'measure': measure, 'quantity': quantity}
                else:
                    shop_list[name]['quantity'] += quantity  

    return shop_list


if __name__ == "__main__":
    file_path = os.path.join(os.getcwd(), 'file1.txt')  

    cook_book = read_cookbook(file_path)

    dishes_to_cook = ['Запеченный картофель', 'Омлет']
    person_count = 2

    shopping_list = get_shop_list_by_dishes(dishes_to_cook, person_count, cook_book)
    print(shopping_list)


    
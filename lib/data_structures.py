spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food['name'] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food['heat_level'] > 5]

def print_spicy_foods(spicy_foods):
    pepper = "🌶"
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {pepper * food['heat_level']}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    spicy_foods_by_cuisine = {}
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            spicy_foods_by_cuisine.update(food)

    return(spicy_foods_by_cuisine)

def print_spiciest_foods(spicy_foods):
    spice = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spice)

def get_average_heat_level(spicy_foods):
    if len(spicy_foods) == 0:
        return 0
    total_heat = sum(food['heat_level'] for food in spicy_foods)
    return total_heat / len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

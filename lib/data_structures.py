# This is a list of dictionaries representing different spicy foods
spicy_foods = [
    {
        # The name of the spicy food
        "name": "Green Curry",
        # The cuisine of the spicy food
        "cuisine": "Thai",
        # The heat level of the spicy food (1-10)
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

# This function takes a list of spicy foods and returns a list of their names
def get_names(spicy_foods):
    # Use a list comprehension to extract the name from each food dictionary
    return [food['name'] for food in spicy_foods]

# This function takes a list of spicy foods and returns a list of the spiciest ones (heat level > 5)
def get_spiciest_foods(spicy_foods):
    # Use a list comprehension to filter the list and only include foods with a heat level greater than 5
    return [food for food in spicy_foods if food['heat_level'] > 5]

# This function takes a list of spicy foods and prints them in a formatted way
def print_spicy_foods(spicy_foods):
    # Loop through the list of spicy foods
    for food in spicy_foods:
        # Print the name, cuisine, and heat level of each food in the specified format
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

# This function takes a list of spicy foods and a cuisine, and returns the first matching food
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    # Use a list comprehension to find all foods with the given cuisine
    matching_foods = [food for food in spicy_foods if food['cuisine'] == cuisine]
    # Use the `next()` function to return the first matching food, or `None` if none is found
    return next(iter(matching_foods), None)

# This function takes a list of spicy foods and prints the spiciest ones (heat level > 5)
def print_spiciest_foods(spicy_foods):
    # Use the `get_spiciest_foods()` function to get the list of spiciest foods
    for food in get_spiciest_foods(spicy_foods):
        # Print the name, cuisine, and heat level of each spiciest food in the specified format
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

# This function takes a list of spicy foods and returns the average heat level
def get_average_heat_level(spicy_foods):
    # Calculate the total heat level of all the foods
    total_heat_level = sum(food['heat_level'] for food in spicy_foods)
    # Divide the total heat level by the number of foods to get the average
    return total_heat_level // len(spicy_foods)

# This function takes a list of spicy foods and a new food, and returns the list with the new food added
def create_spicy_food(spicy_foods, new_food):
    # Add the new food to the list and return the updated list
    return spicy_foods + [new_food]

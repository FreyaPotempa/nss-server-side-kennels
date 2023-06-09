from .location_requests import get_single_location
from .customer_requests import get_single_customer

ANIMALS = [
    {
        "id": 1,
        "name": "Snickers",
        "species": "Dog",
        "locationId": 1,
        "customerId": 4,
        "status": "Admitted"
    },
    {
        "id": 2,
        "name": "Roman",
        "species": "Dog",
        "locationId": 1,
        "customerId": 2,
        "status": "Admitted"
    },
    {
        "id": 3,
        "name": "Blue",
        "species": "Cat",
        "locationId": 2,
        "customerId": 1,
        "status": "Admitted"
    }
]


def get_all_animals():
    '''function to get all animals'''
    return ANIMALS
# Function with a single parameter


def get_single_animal(id):
    '''function to get single animal'''
    # Variable to hold the found animal, if it exists
    requested_animal = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for animal in ANIMALS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if animal["id"] == id:
            requested_animal = animal
            matching_location = get_single_location(
                requested_animal["locationId"])
            requested_animal["location"] = matching_location
            matching_customer = get_single_customer(
                requested_animal["customerId"])
            requested_animal["customer"] = matching_customer
            requested_animal.pop("customerId", "locationId")

    return requested_animal


def create_animal(animal):
    '''get the id value of the last animal in list'''
    # Get the id value of the last animal in the list
    max_id = ANIMALS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    animal["id"] = new_id

    # Add the animal dictionary to the list
    ANIMALS.append(animal)

    # Return the dictionary with `id` property added
    return animal


def update_animal(id, new_animal):
    '''PUT function for animals'''
    for index, animal in enumerate(ANIMALS):
        if animal["id"] == id:
            ANIMALS[index] = new_animal
            break


def delete_animal(id):
    '''delete function for animal'''
    # initial value for animal index in case one isn't found
    animal_index = -1

    # iterate the ANIMALS list using enumerate() to access index and value
    for index, animal in enumerate(ANIMALS):
        if animal["id"] == id:
            # found animal, store the index
            animal_index = index

    # if the animal was found, use pop(int) to remove it
    if animal_index >= 0:
        ANIMALS.pop(animal_index)

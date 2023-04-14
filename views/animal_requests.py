import sqlite3
import json
from models import Animal


def get_all_animals():
    '''function to get all animals'''
    # Open a connection to the database
    with sqlite3.connect("./kennel.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id
        FROM animal a
        """)

        # Initialize an empty list to hold all animal representations
        animals = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            animal = Animal(row['id'], row['name'], row['breed'],
                            row['status'], row['location_id'],
                            row['customer_id'])

            animals.append(animal.__dict__)

    return animals
# Function with a single parameter


def get_single_animal(id):
    '''function to get single animal'''
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id
        FROM animal a
        WHERE a.id = ?
        """, (id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        animal = Animal(data['id'], data['name'], data['breed'],
                        data['status'], data['location_id'],
                        data['customer_id'])

        return animal.__dict__
    # requested_animal = None

    # # Iterate the ANIMALS list above. Very similar to the
    # # for..of loops you used in JavaScript.
    # for animal in ANIMALS:
    #     # Dictionaries in Python use [] notation to find a key
    #     # instead of the dot notation that JavaScript used.
    #     if animal["id"] == id:
    #         requested_animal = animal

    # return requested_animal


def get_animals_by_location(location):
    '''get animals at location'''

    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
    SELECT
        a.id,
        a.name,
        a.breed,
        a.status,
        a.location_id,
        a.customer_id
    FROM animal a
    WHERE a.location_id = ?
    """, (location, ))

        animals = []

        dataset = db_cursor.fetchall()

        if dataset:
            for row in dataset:
                animal = Animal(row["id"], row["name"], row["breed"],
                                row["status"], row["location_id"], row["customer_id"])
                animals.append(animal.__dict__)
            return animals
        else:
            return None


def get_animals_by_status(status):
    '''get animals by status'''

    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
    SELECT
        a.id,
        a.name,
        a.breed,
        a.status,
        a.location_id,
        a.customer_id
    FROM animal a
    WHERE a.status = ?
    """, (status, ))

        animals = []

        dataset = db_cursor.fetchall()

        if dataset:
            for row in dataset:
                animal = Animal(row["id"], row["name"], row["breed"],
                                row["status"], row["location_id"], row["customer_id"])
                animals.append(animal.__dict__)
            return animals
        else:
            return None


# def create_animal(animal):
#     '''get the id value of the last animal in list'''
#     # Get the id value of the last animal in the list
#     max_id = ANIMALS[-1]["id"]

#     # Add 1 to whatever that number is
#     new_id = max_id + 1

#     # Add an `id` property to the animal dictionary
#     animal["id"] = new_id

#     # Add the animal dictionary to the list
#     ANIMALS.append(animal)

#     # Return the dictionary with `id` property added
#     return animal


# def update_animal(id, new_animal):
#     '''PUT function for animals'''
#     for index, animal in enumerate(ANIMALS):
#         if animal["id"] == id:
#             ANIMALS[index] = new_animal
#             break

def delete_animal(id):
    '''deletes an animal from the database'''
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM animal
        WHERE id = ?
        """, (id, ))


def update_animal(id, new_animal):
    '''updating an animal'''
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Animal
            SET
                name = ?,
                breed = ?,
                status = ?,
                location_id = ?,
                customer_id = ?
        WHERE id = ?
        """, (new_animal['name'], new_animal['breed'],
              new_animal['status'], new_animal['location_id'],
              new_animal['customer_id'], id, ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True

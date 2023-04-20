import sqlite3
import json
from models import Location


def get_all_locations():
    '''returns all locations'''
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address,
            (SELECT COUNT(*) FROM Animal WHERE location_id = a.id) AS animal_count
        FROM location a
        """)

        locations = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            location = Location(row["id"], row["name"],
                                row["address"], row['animal_count'])

            locations.append(location.__dict__)

    return locations


def get_single_location(id):
    '''returns single location'''
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address
        FROM location a
        WHERE a.id = ?
        """, (id, ))

        data = db_cursor.fetchone()

        location = Location(data["id"], data["name"], data["address"])

        return location.__dict__


def create_location(location):
    '''get the id value of the last location in list'''

    max_id = LOCATIONS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the dictionary
    location["id"] = new_id

    # Add the location dictionary to the list
    LOCATIONS.append(location)

    # Return the dictionary with `id` property added
    return location


def update_location(id, new_location):
    '''PUT function for locations'''
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            LOCATIONS[index] = new_location
            break


def delete_location(id):
    '''delete function for location'''
    location_index = -1

    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            location_index = index

        if location_index >= 0:
            LOCATIONS.pop(location_index)

import json
import sqlite3
from models import Employee, Location


def get_all_employees():
    '''function to get all employees'''
    with sqlite3.connect("./kennel.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.address,
            e.location_id,
            l.name location_name,
            l.address location_address
        FROM employee e
        JOIN location l
            ON l.id = e.location_id
        """)

        # Initialize an empty list to hold all animal representations
        employees = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            employee = Employee(row['id'], row['name'],
                                row['address'], row['location_id'])

            location = Location(
                row["id"], row["location_name"], row["location_address"])

            employee.location = location.__dict__

            employees.append(employee.__dict__)

    return employees


def get_single_employee(id):
    '''function to get single animal'''
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.address,
            e.location_id
        FROM employee e
        WHERE e.id = ?
        """, (id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        employee = Employee(data['id'], data['name'], data['address'],
                            data['location_id'])

        return employee.__dict__


def get_employees_by_location(location):
    '''get employees at location'''
    print("THIS FIRING", location)

    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
    SELECT
        e.id,
        e.name,
        e.address,
        e.location_id
    FROM employee e
    WHERE e.location_id = ?
    """, (location, ))

        employees = []

        dataset = db_cursor.fetchall()

        if dataset:
            for row in dataset:
                employee = Employee(
                    row["id"], row["name"], row["address"], row["location_id"])
                employees.append(employee.__dict__)
            return employees
        else:
            return None


def create_employee(new_employee):
    '''create an animal'''
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Employee
            ( name, address, location_id )
        VALUES
            ( ?, ?, ? );
        """, (new_employee['name'], new_employee['address'], new_employee['location_id']))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the animal dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_employee['id'] = id

    return new_employee


# def update_employee(id, new_employee):
#     '''PUT function for employees'''
#     for index, employee in enumerate(EMPLOYEES):
#         if employee["id"] == id:
#             EMPLOYEES[index] = new_employee
#             break


# def delete_employee(id):
#     '''delete function for employee'''
#     # initial value for animal index in case one isn't found
#     employee_index = -1

#     # iterate the ANIMALS list using enumerate() to access index and value
#     for index, employee in enumerate(EMPLOYEES):
#         if employee["id"] == id:
#             # found animal, store the index
#             employee_index = index

#     # if the animal was found, use pop(int) to remove it
#     if employee_index >= 0:
#         EMPLOYEES.pop(employee_index)

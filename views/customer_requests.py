import json
import sqlite3
from models import Customer


def get_all_customers():
    '''return all customers'''
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
            a.address,
            a.email,
            a.password
        FROM customer a
        """)

        # Initialize an empty list to hold all custy representations
        customers = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            customer = Customer(
                row['id'], row['name'], row['address'], row['email'], row['password'])

            customers.append(customer.__dict__)

    return customers
    # return CUSTOMERS


def get_single_customer(id):
    '''return customer by id'''
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address,
            a.email,
            a.password
        FROM customer a
        WHERE a.id = ?
            """, (id, ))

        data = db_cursor.fetchone()

        customer = Customer(data["id"], data["name"],
                            data["address"], data["email"], data["password"])

        return customer.__dict__


def get_customer_by_email(email):
    '''get customer by email address'''

    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            c.id,
            c.name,
            c.address
        FROM Customer c
        WHERE c.email = ?
        """, (email, ))

        row = db_cursor.fetchone()

        if row:
            customer = Customer(
                row['id'], row['name'], row['address'])

            return customer.__dict__
        else:
            return None


def create_customer(customer):
    '''get the id value of the last item in list'''
    max_id = CUSTOMERS[-1]["id"]

    new_id = max_id + 1

    customer["id"] = new_id

    CUSTOMERS.append(customer)

    return customer


def update_customer(id, new_customer):
    '''PUT function for customers'''
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            CUSTOMERS[index] = new_customer
            break


def delete_customer(id):
    '''delete function for customer'''
    customer_index = -1

    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            customer_index = index

        if customer_index >= 0:
            CUSTOMERS.pop(customer_index)

CUSTOMERS = [
    {
        "id": 1,
        "name": "Hope Kub"
    },
    {
        "id": 2,
        "name": "Leon Sporer"
    },
    {
        "id": 3,
        "name": "Cortez McKenzie"
    }

]


def get_all_customers():
    '''return all customers'''
    return CUSTOMERS


def get_single_customer(id):
    '''return customer by id'''
    requested_customer = None

    for customer in CUSTOMERS:
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer


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

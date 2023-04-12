DATABASE = {
    "animals": [
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
    ],
    "customers": [
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
    ],
    "employees": [
        {
            "id": 1,
            "name": "Jenna Solis"
        },
        {
            "id": 2,
            "name": "Amparo Bauch"
        },
        {
            "id": 3,
            "name": "Teagan Langworth"
        }
    ],
    "locations": [
        {
            "id": 1,
            "name": "Nashville North",
            "address": "8422 Johnson Pike"
        },
        {
            "id": 2,
            "name": "Nashville South",
            "address": "209 Emory Drive"
        }
    ]
}


def all(resource):
    """For GET requests to collection"""
    print(resource)

    if resource in DATABASE.keys():
        return DATABASE[resource]


def retrieve():
    """For GET requests to a single resource"""
    pass


def create():
    """For POST requests to a collection"""
    pass


def update():
    """For PUT requests to a single resource"""
    pass


def delete():
    """For DELETE requests to a single resource"""
    pass

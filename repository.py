DATABASE = {
    "ANIMALS": [
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
    "CUSTOMERS": [
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
    "EMPLOYEES": [
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
    "LOCATIONS": [
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


def all(self, resource):
    """For GET requests to collection"""

    # self._set_headers(200)
    # response = DATABASE[resource]
    pass


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

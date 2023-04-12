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


def retrieve(resource, id):
    """For GET requests to a single resource"""
    requested_resource = None

    if resource in DATABASE.keys():
        asset_list = DATABASE[resource]

        for asset in asset_list:
            if asset["id"] == id:
                requested_resource = asset

    return requested_resource


def create(resource, post_body):
    """For POST requests to a collection"""
    # passing the path with a variable of resource, and passing the new object to append
    if resource in DATABASE.keys():
        max_id = DATABASE[resource][-1]["id"]
        new_id = max_id + 1
        post_body["id"] = new_id

        DATABASE[resource].append(post_body)

        return post_body


def update(resource, id, post_body):
    """For PUT requests to a single resource"""
    if resource in DATABASE.keys():
        asset_list = DATABASE[resource]

        for index, asset in enumerate(asset_list):
            if asset["id"] == id:
                asset_list[index] = post_body
                break


def delete(resource, id):
    """For DELETE requests to a single resource"""
    if resource in DATABASE.keys():
        resource_index = -1

        for index, asset in enumerate(DATABASE[resource]):
            if asset["id"] == id:
                resource_index = index

        if resource_index >= 0:
            DATABASE[resource].pop(resource_index)

    pass

EMPLOYEES = [
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
]


def get_all_employees():
    '''function to get all employees'''
    return EMPLOYEES


def get_single_employee(id):
    '''function to get single employee'''
    requested_employee = None

    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee
    return requested_employee

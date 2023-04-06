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


def create_employee(employee):
    '''gets id value of last item in list to create new item'''
    max_id = EMPLOYEES[-1]["id"]

    new_id = max_id + 1

    employee["id"] = new_id

    EMPLOYEES.append(employee)

    return employee


def update_employee(id, new_employee):
    '''PUT function for employees'''
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            EMPLOYEES[index] = new_employee
            break


def delete_employee(id):
    '''delete function for employee'''
    # initial value for animal index in case one isn't found
    employee_index = -1

    # iterate the ANIMALS list using enumerate() to access index and value
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            # found animal, store the index
            employee_index = index

    # if the animal was found, use pop(int) to remove it
    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)

import metadata


def new_assignment_data(assignment_data: dict):
    for field, value in metadata.ASSIGNMENT.items():
        print(field)
        if metadata.ASSIGNMENT[field]['required'] and field in assignment_data.keys():
            continue

        return False


data = {
    "assignment_id": 2,
    "student_id": 1
}

print(new_assignment_data(data))
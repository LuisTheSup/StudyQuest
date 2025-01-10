import metadata


def new_assignment_data(assignment_data: dict):
    for field, properties in metadata.ASSIGNMENT.items():
        # Checks for required fields in assignment_data
        if properties['required'] and field in assignment_data.keys():
            continue
        return False

    return True


data = {
    "assignment_id": 87,
    "student_id": 1
}

print(new_assignment_data(data))
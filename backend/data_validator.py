from backend import metadata
from backend.exceptions import MissingFieldsError


def new_assignment_data(assignment_data: dict):
    missing_fields = []
    for field, properties in metadata.ASSIGNMENT.items():
        # Checks for missing fields in assignment_data
        if properties['required'] and field not in assignment_data.keys():
            missing_fields.append(field)

    if missing_fields:
        raise MissingFieldsError(missing_fields)
    return True

# TEST DATA
data = {
    "assignment_id": 87,
    "student_id": 1,
    # "name": "study guide",
    "category": "formative",
    # "total_points": 40,
    # "weighting": 1.0,
}

print(new_assignment_data(data))
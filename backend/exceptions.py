class MissingFieldsError(Exception):
    def __init__(self, missing_fields: list[str]):
        super().__init__(f'Missing Required Fields - {', '.join(missing_fields)}')
        self.missing_fields = missing_fields


class InvalidFieldsError(Exception):
    def __init__(self, invalid_fields: list[str]):
        super().__init__(f"Invalid Fields -> {', '.join(invalid_fields)}")
        self.invalid_fields = invalid_fields

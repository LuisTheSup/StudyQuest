class MissingFieldsError(Exception):
    def __init__(self, missing_fields):
        super().__init__(f'Missing Required Fields - {', '.join(missing_fields)}')
        self.missing_fields = missing_fields

ASSIGNMENT = {
    'assignment_id': {
        'datatype': int, # BIGINT
        'required': True,
        'unique': True,
        'nullable': False,
        'edit': False,
        'auto_generated': True,
        'default_value': 'auto_increment',
        'max_length': 19, # Maximum number of digits for BIGINT
        'description': 'Primary key for assignments',
        'format': None,
        'foreign_key': None,
        'constraint': 'PRIMARY KEY'
    },
    'student_id': {
        'datatype': int, # BIGINT
        'required': True,
        'unique': True,
        'nullable': False,
        'edit': False,
        'auto_generated': False,
        'default_value': None,
        'max_length': 19, # Maximum number of digits for BIGINT
        'description': 'Foreign key for student_id',
        'format': None,
        'foreign_key': {
            'table': 'students',
            'column': 'student_id'},
        'constraint': ['FOREIGN KEY', 'ON DELETE CASCADE']
    }
}

STUDENT = {

}

METADATA = {
        'assignment_id': {
        'datatype': int,
        'required': True,
        'unique': True,
        'edit': False,
        'auto_generated': True,
        'default_value': 'auto_increment',
        'max_length': None,
        'description': 'Primary key for assignments'
        },
        'student_id': {
            'datatype': int,
            'required': True,
            'unique': True,
            'edit': False,
        },
        'name': {
            'datatype': int,
            'required': True,
            'unique': True,
            'edit': False,
        },
        'description': {},
        'category': {},
        'points_achieved': {},
        'total_points': {},
        'weighting': {},
        'grade': {},
        'due_date': {},
        'created_at': {},
        'updated_at': {},
        'graded': {}
    }
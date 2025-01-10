ASSIGNMENT = {
    'assignment_id': {
        'datatype': int, # BIGINT
        'required': True,
        'unique': True,
        'edit': False,
        'auto_generated': True,
        'max_length': 19, # Maximum number of digits for BIGINT
        'format': None,
        'key_column': [True, 'PRIMARY'],
    },
    'student_id': {
        'datatype': int, # BIGINT
        'required': True,
        'unique': True,
        'edit': False,
        'auto_generated': False,
        'max_length': 19, # Maximum number of digits for BIGINT
        'format': None,
        'key_column': [True, "FOREIGN"],
    },
    'name': {
        'datatype': str, # VARCHAR(150)
        'required': True,
        'unique': False,
        'edit': True,
        'auto_generated': False,
        'max_length': 150, # Maximum number of characters
        'format': None,
        'key_column': [False],
    },
    'description': {
        'datatype': str, # TEXT
        'required': False,
        'unique': False,
        'edit': True,
        'auto_generated': False,
        'max_length': None,
        'format': None,
        'key_column': [False],
    },
    'category': {
        'datatype': str, # VARCHAR(12)
        'required': True,
        'unique': False,
        'edit': True,
        'auto_generated': False,
        'max_length': 12, # Maximum number of characters
        'format': ['Formative', 'Summative'],
        'key_column': [False],
    },
    'points_achieved': {
        'datatype': float, # NUMERIC TODO Needs to be reviewed further for possible switch to decimal
        'required': False,
        'unique': False,
        'edit': True,
        'auto_generated': False,
        'max_length': None,
        'format': None,
        'key_column': [False],
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
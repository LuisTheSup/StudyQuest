import datetime

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
    },
    'total_points': {
        'datatype': int, # NUMERIC
        'required': True,
        'unique': False,
        'edit': True,
        'auto_generated': False,
        'max_length': None, #TODO To be reviewed
        'format': None,
        'key_column': [False],
    },
    'weighting': {
        'datatype': float, # REAL
        'required': False,
        'unique': False,
        'edit': True,
        'auto_generated': False,
        'max_length': None, #TODO To be reviewed
        'format': None,
        'key_column': [False],
    },
    'grade': {
        'datatype': str, # VARCHAR(3)
        'required': False,
        'unique': False,
        'edit': True,
        'auto_generated': False,
        'max_length': 3, # Maximum number of characters
        'format': ['A', 'B', 'C', 'D', 'F', 'NS', '-', '+'],
        'key_column': [False],
    },
    'percentage': {
        'datatype': str, # VARCHAR(6)
        'required': False,
        'unique': False,
        'edit': True,
        'auto_generated': False,
        'max_length': None, # Maximum number of characters
        'format': None,
        'key_column': [False],
    },
    'due_date': {
        'datatype': str, # TIMESTAMP
        'required': False,
        'unique': False,
        'edit': True,
        'auto_generated': False,
        'max_length': None, #TODO to be reviewed
        'format': None,
        'key_column': [False],
    },
    'created_at': {
        'datatype': str, # TIMESTAMP
        'required': False,
        'unique': False,
        'edit': True,
        'auto_generated': False,
        'max_length': None, #TODO to be reviewed
        'format': None,
        'key_column': [False],
    },
    'updated_at': {
        'datatype': str, # TIMESTAMP
        'required': False,
        'unique': False,
        'edit': True,
        'auto_generated': False,
        'max_length': None, #TODO to be reviewed
        'format': None,
        'key_column': [False],
    },
    'graded': {
        'datatype': bool,
        'required': False,
        'unique': False,
        'edit': True,
        'auto_generated': False,
        'max_length': None, #TODO to be reviewed
        'format': None,
        'key_column': [False],
    }
}

STUDENT = {
    'student_id': {
        'datatype': int, # BIGINT
        'required': True,
        'unique': True,
        'edit': False,
        'auto_generated': True,
        'max_length': 19, # Maximum number of digits for BIGINT
        'format': None,
        'key_column': [True, 'PRIMARY'],
    },
    'firstname': {
        'datatype': str, # VARCHAR(100)
        'required': True,
        'unique': False,
        'edit': True,
        'auto_generated': False,
        'max_length': 100,
        'format': None, #TODO To be reviewed
        'key_column': [False],
    },
    'lastname': {
        'datatype': str, # VARCHAR(100)
        'required': True,
        'unique': False,
        'edit': True,
        'auto_generated': False,
        'max_length': 100,
        'format': None, #TODO to be reviewed
        'key_column': [False],
    },
    'email': {
        'datatype': str, # VARCHAR(255)
        'required': True,
        'unique': True,
        'edit': True,
        'auto_generated': False,
        'max_length': 255,
        'format': None, #TODO to be reviewed
        'key_column': [False],
    },
    'phone_number': {
        'datatype': str, # VARCHAR(30)
        'required': False, #TODO TO be reviewed
        'unique': True,
        'edit': True,
        'auto_generated': False,
        'max_length': 30,
        'format': None, #TODO to be reviewed
        'key_column': [False],
    },
    'gender': {
        'datatype': str, # VARCHAR(10)
        'required': True,
        'unique': False,
        'edit': True,
        'auto_generated': False,
        'max_length': 10,
        'format': ['male', 'female'], #TODO to be reviewed
        'key_column': [False],
    },
    'date_of_birth': {
        'datatype': datetime.date, # DATE TODO To be reviewed
        'required': True, #TODO TO be reviewed
        'unique': False,
        'edit': True,
        'auto_generated': False,
        'max_length': None,
        'format': None,
        'key_column': [False],
    }

}
from sql_connection import SQLConnection

def main():
    with SQLConnection() as postgres:
        postgres.add_assignment(
            2,
            'study guide',
            'Read the chapter slides 1 to 4',
            'Formative',
            18.5,
            20.0,
            0.125,
            'A+',
            '2025-01-08'
        )

if __name__ == '__main__':
    main()
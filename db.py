from sql_connection import SQLConnection

# Assignment related queries
def add_assignment(assignment_data: dict):
    """
    Adds a new assignment record to the table based on the data provided (previously validated)
    :param assignment_data: A dictionary containing the fields and values for the new record
    :return: None
    """
    with SQLConnection() as postgres:
        query = f"""
        INSERT INTO assignments ({', '.join(assignment_data.keys())})
        VALUES ({', '.join(['%s' for _ in range(len(assignment_data))])});
        """

        postgres.cursor.execute(query, tuple(assignment_data.values()))
        postgres.connection.commit()


def update_assignment(assignment_data: dict, assignment_id: int):
    """
    Updates a specific assignment record in the table based on the data provided
    :param assignment_data: A dictionary containing the fields and values to update the record with
    :param assignment_id: The ID of the assignment to update
    :return: None
    """
    with SQLConnection() as postgres:
        subqueries = [f"{field} = %s" for field in assignment_data.keys()]
        query = f"""
        UPDATE assignments
        SET {",\n".join(subqueries)}
        WHERE assignment_id = %s;
        """

        postgres.cursor.execute(query, tuple(assignment_data.values()) + (assignment_id,))
        postgres.connection.commit()


def delete_assignment(assignment_id: int):
    """
    Deletes a specific assignment record from the table
    :param assignment_id: The ID of the assignment to delete
    :return: None
    """
    with SQLConnection() as postgres:
        query = "DELETE FROM assignments WHERE assignment_id = %s"
        postgres.cursor.execute(query, (assignment_id,))
        postgres.connection.commit()


def read_assignment(assignment_id: int):
    """
    Read a single assignment record from the table
    :param assignment_id: The ID of the assignment to read
    :return: list[tuple]
    """
    with SQLConnection() as postgres:
        query = "SELECT * FROM assignments WHERE assignment_id = %s"
        postgres.cursor.execute(query, (assignment_id,))
        return postgres.cursor.fetchone()


def read_assignments():
    """
    Reads all assignment records from the table
    :return: list[tuples]
    """
    with SQLConnection() as postgres:
        query = "SELECT * FROM assignments"
        postgres.cursor.execute(query)
        return postgres.cursor.fetchall()


def read_assignments_column( column: str, *, assignment_id: int = None):
    """
        Reads a specific assignment's column from the table if an assignment id is provided
        otherwise it will read the same column from every assignment in the table
        :param column: Column to read
        :param assignment_id: The ID of the assignment to read - DEFAULTS to None
        :return: list[tuple]
        """
    with SQLConnection() as postgres:
        if assignment_id is None:
            query = f"SELECT {column} FROM assignments"
        else:
            query = f"SELECT {column} FROM assignments WHERE assignment_id = %s"
        postgres.cursor.execute(query, (assignment_id,))
        return postgres.cursor.fetchall()


# Students related queries
def add_student(student_data: dict):
    with SQLConnection as postgres:
        query = f"""
        INSERT INTO students {",\n".join(student_data.keys())}
        VALUES {", ".join(['%s' for _ in range(len(student_data))])};
        """

        postgres.cursor.execute(query, tuple(student_data.values()))
        postgres.connection.commit()


def update_student(student_data: dict, student_id: int):
    """
    Updates a specific user record in the table based on the data provided
    :param student_data: A dictionary containing the fields and values to update the record with
    :param student_id: The ID of the user to update
    :return: None
    """
    with SQLConnection as postgres:
        subqueries = [f"{field} = %s" for field in student_data.keys()]
        query = f"""
        UPDATE students
        SET {", ".join(subqueries)}
        WHERE student_id = %s;
        """

        postgres.cursor.execute(query, tuple(student_data.values()) + (student_id,))
        postgres.connection.commit()


def delete_student(student_id: int):
    """
    Deletes a specific student record from the table
    :param student_id: The ID of the student to delete
    :return: None
    """
    with SQLConnection() as postgres:
        query = f"DELETE FROM students WHERE student_id = %s"
        postgres.cursor.execute(query, (student_id,))
        postgres.connection.commit()


def read_student(student_id: int):
    """
    Read a single student record from the table
    :param student_id: The ID of the student to read
    :return: tuple
    """
    with SQLConnection() as postgres:
        query = f"SELECT * FROM students WHERE student_id = %s"
        postgres.cursor.execute(query, (student_id,))
        return postgres.cursor.fetchone()


def read_students():
    """
    Read all students records from the table
    :return: list[tuples]
    """
    with SQLConnection() as postgres:
        query = f"SELECT * FROM students"
        postgres.cursor.execute(query)
        return postgres.cursor.fetchall()


def student_exists(student_id: int):
    """
    Checks whether a student exists in the table based on the id provided
    :param student_id: The ID of the student to read
    :return: bool
    """
    with SQLConnection() as postgres:
        query = "SELECT EXISTS(SELECT 1 FROM students WHERE student_id = %s);"
        postgres.cursor.execute(query, (student_id,))
        return postgres.cursor.fetchone()[0]


def read_students_column(column: str, *, student_id: int = None):
    """
    Reads a specific student's column from the table if a student id is provided
    otherwise it will read the same column from every student in the table
    :param column: Column to read
    :param student_id: The ID of the student to read - DEFAULTS to None
    :return: list[tuple]
    """
    with SQLConnection() as postgres:
        if student_id is None:
            query = f"SELECT {column} FROM students"
        else:
            query = f"SELECT {column} FROM students WHERE student_id = %s"
        postgres.cursor.execute(query, (student_id,))
        return postgres.cursor.fetchall()

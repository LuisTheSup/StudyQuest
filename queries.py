from sql_connection import SQLConnection


def add_assignment(assignment_data: dict):
    """

    :param assignment_data:
    :return:
    """
    with SQLConnection() as postgres:
        subqueries = [f"{field}" for field in assignment_data.keys()]
        query = f"""
        INSERT INTO assignments ({', '.join(subqueries)})
        VALUES ({', '.join(['%s' for _ in range(len(subqueries))])});
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
    :return: None
    """
    with SQLConnection() as postgres:
        query = "SELECT * FROM assignments WHERE assignment_id = %s"
        postgres.cursor.execute(query, (assignment_id,))
        return postgres.cursor.fetchone()


def read_assignments():
    """
    Reads all assignment records from the table
    :return: None
    """
    with SQLConnection() as postgres:
        query = "SELECT * FROM assignments"
        postgres.cursor.execute(query)
        return postgres.cursor.fetchall()

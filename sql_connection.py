import psycopg2
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Gather and organize environment variables
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")


class SQLConnection:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        self.cursor = self.connection.cursor()

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()
        if self.cursor:
            self.cursor.close()

    def add_assignment(
            self,
            student_id: int,
            name: str,
            description: str,
            category: str,
            points_achieved: float,
            total_points: float,
            weighting: float,
            grade: str,
            due_date: str,
    ):

        query = """
        INSERT INTO assignments (
        student_id,
        name,
        description,
        category,
        points_achieved,
        total_points,
        weighting,
        grade,
        due_date
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, DATE %s)
        """
        values = (
            student_id,
            name,
            description,
            category,
            points_achieved,
            total_points,
            weighting,
            grade,
            due_date
        )
        # SUBMITS and SAVES the changes
        self.cursor.execute(query, values)
        self.connection.commit()
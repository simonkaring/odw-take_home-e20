import mysql.connector


class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            user="root",
            password="root",
            host="db",
            database="people",
        )
        self.cursor = self.connection.cursor(dictionary=True)

    def create_db(self):
        self.cursor.execute("DROP TABLE IF EXISTS people")
        self.cursor.execute(
            """
            CREATE TABLE people
            (
            PersonID SERIAL, Firstname VARCHAR(255), Lastname VARCHAR(255)
            )
            """)
        self.connection.commit()

    def insert(self, firstname, lastname):
        self.cursor.execute(
            """
            INSERT INTO people (Firstname, Lastname)
            VALUES ('{}', '{}')
            """.format(
                firstname,
                lastname
            ))
        self.connection.commit()

    def retrieve(self):
        self.cursor.execute('SELECT * FROM people')
        return(self.cursor.fetchall())
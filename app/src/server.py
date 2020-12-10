from flask import Flask, request, jsonify
import mysql.connector


class DBManager:
    def __init__(self):
        self.connection = mysql.connector.connect(
            user="root",
            password="root",
            host="db",
            database="people",
        )
        self.cursor = self.connection.cursor(dictionary=True)
        # self.cursor.execute(
        #     """
        #     CREATE TABLE people
        #     (
        #     PersonID SERIAL, Firstname VARCHAR(255), Lastname VARCHAR(255)
        #     )
        #     """)
        # self.cursor.execute(
        #     """
        #     INSERT INTO people (Firstname, Lastname)
        #     VALUES ('Donald', 'Trump')
        #     """)
        # self.connection.commit()

    def populate_db(self):
        self.cursor.execute('DROP TABLE IF EXISTS people')
        self.cursor.execute(
            """
            CREATE TABLE people
            (
            PersonID SERIAL, Firstname VARCHAR(255), Lastname VARCHAR(255)
            )
            """)
        self.cursor.execute(
            """
            INSERT INTO people (Firstname, Lastname)
            VALUES ('Mads', 'Jensen')
            """)
        self.connection.commit()

    def query_titles(self):
        self.cursor.execute('SELECT * FROM people')
        return(self.cursor.fetchall())


server = Flask(__name__)
conn = None
conn = DBManager()
conn.populate_db()


@server.route('/persons')
def list_persons():
    global conn
    # if not conn:
    #     conn = DBManager()
    #     conn.populate_db()
    results = conn.query_titles()
    return jsonify(results)


@server.route('/')
def hello():
    return jsonify({"response": "Hello from Docker!"})


if __name__ == '__main__':
    server.run(debug=True, host='0.0.0.0', port=5000)

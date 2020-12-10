from flask import Flask, request, jsonify
from database import Database


app = Flask(__name__)
database = None
database = Database()
database.create_db()
database.populate_db("Mads", "Jensen")
database.populate_db("Mathias", "Neerup")


@app.route('/persons')
def list_persons():
    global database
    # if not database:
    #     database = DBManager()
    #     database.populate_db()
    results = database.retrieve()
    return jsonify(results)


@app.route('/person', methods=['POST'])
def person():
    """Add people to database."""
    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")

    database.insert(firstname, lastname)
    return("POST Success", 200)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

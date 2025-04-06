from flask import Flask

users = {
 1: {"name": "Ala", "age": 22},
 2: {"name": "Bartek", "age": 25},
 3: {"name": "Celina", "age": 30}
}

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/about")
def about():
    return "Nazywam się Michał"

@app.route("/users")
def lista_uzytkownikow():
    return f"{[user['name'] for user in users.values()]}"

@app.route("/users/<id>")
def user_id(id):
    return users[id]

if __name__ == "__main__":
    app.run(debug=True)

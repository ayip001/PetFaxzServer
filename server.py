from flask import Flask, request
import json
import csv

app = Flask(__name__)


@app.route("/generatemsg")
def main():
    breed = str(request.args.get('breed'))
    age = int(request.args.get('age'))
    name = str(request.args.get('name'))
    pronoun = str(request.args.get('pronoun'))
    # dead = str(request.args.get('dead'))
    return json.dumps({"breed": breed, "age": age, "name": name, "pronoun": pronoun})

if __name__ == "__main__":
    app.run()

from flask import Flask, request
import json
import csv
import sys

app = Flask(__name__)

def getLifeSpan( breed ):
    csv_file = csv.reader(open('data.csv', "rb"), delimiter=",")
    for row in csv_file:
        if breed == row[0]:
             return int(row[1])

@app.route("/generatemsg")
def main():
    breed = str(request.args.get('breed'))
    age = int(request.args.get('age'))
    name = str(request.args.get('name'))
    pronoun = str(request.args.get('pronoun'))
    # dead = str(request.args.get('dead'))

    span = getLifeSpan( breed )
    return json.dumps({"breed": breed, "age": age, "name": name, "pronoun": pronoun, "span": span})

if __name__ == "__main__":
    app.run()

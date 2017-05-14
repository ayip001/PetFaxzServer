from flask import Flask, request
import json
import csv
import sys
import datetime
from datetime import timedelta

app = Flask(__name__)

def getLifeSpan( breed ):
    csv_file = csv.reader(open('data.csv', "rb"), delimiter=",")
    for row in csv_file:
        if breed == row[0]:
             return int(row[1])

def getTimeRemaining( age, span_years, timeType ):
    timeRem_sec = span_years * 365 * 24 * 60 * 60 - age
    if timeType == "hours":
        return timeRem_sec / (60 * 60)
    if timeType == "days":
        return timeRem_sec / (60 * 60 * 24)
    if timeType == "years":
        return timeRem_sec / (365 * 24 * 60 * 60)
    if timeType == "date":
        return datetime.date.today() + timedelta(seconds=timeRem_sec)

@app.route("/generatemsg")
def main():
    breed = str(request.args.get('breed'))
    age = int(request.args.get('age'))
    name = str(request.args.get('name'))
    pronoun = str(request.args.get('pronoun'))
    # dead = str(request.args.get('dead'))

    span = str(getTimeRemaining(age, getLifeSpan( breed ), "date"))
    return json.dumps({"breed": breed, "age": age, "name": name, "pronoun": pronoun, "span": span})

if __name__ == "__main__":
    app.run()

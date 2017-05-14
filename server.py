from flask import Flask, request
import random
import json
import csv
import sys
import datetime
from datetime import timedelta

app = Flask(__name__)

messages = [("Princess Di lived to be 36 but {name} probably wont. {name}" +
             " has {time_left} hours left before {pronoun} experiences" +
             " statistical death."),
            ("{name} is going through a mid life crisis. {pronoun} has" +
             " {time_left} left to live")
            ]


def getLifeSpan(breed):
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


    span = getLifeSpan(breed)

    message = random.choice(messages).format(name=name,
                                             time_left=span-age,
                                             pronoun=pronoun)

    return json.dumps({"message": message})


if __name__ == "__main__":
    app.run()

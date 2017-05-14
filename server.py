from flask import Flask, request
import random
import json
import csv

app = Flask(__name__)

messages = [("Princess Di lived to be 36 and so has {name}. {name} has " +
             "{time_left} hours left before {pronoun} experiences" +
             " statistical death."),
            ("{name} is going through a mid life crisis. {pronoun} has" +
             " {time_left} left to live")
            ]


@app.route("/generatemsg")
def main():
    breed = str(request.args.get('breed'))
    age = int(request.args.get('age'))
    name = str(request.args.get('name'))
    pronoun = str(request.args.get('pronoun'))

    # dead = str(request.args.get('dead'))

    time_left = 0

    message = random.choice(messages).format(name=name,
                                             time_left=time_left,
                                             pronoun=pronoun)

    return json.dumps({"message": message})


if __name__ == "__main__":
    app.run()

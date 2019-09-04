from flask import Flask
from random import choice

app = Flask(__name__)

compliments = ["coolio", "smashing", "neato", "fantabulous"]
predictions = ["You will get hit by a car today", "You will get food poisoning from your pizza", "Your dog will eat your pillow"]


@app.route("/compliment")
def get_compliment():
	compliment = choice(compliments)
	return f'Hello there, user! You are so {compliment}'

@app.route("/horoscope")
def get_horoscope():
	prediction = choice(predictions)
	return f'{prediction}'


if __name__ == "__main__":
	app.run(debug = True)
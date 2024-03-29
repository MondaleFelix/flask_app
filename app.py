from flask import Flask, request, render_template
from random import choice

app = Flask(__name__)

compliments = ["coolio", "smashing", "neato", "fantabulous"]
predictions = ["You will get hit by a car today", "You will get food poisoning from your pizza", "Your dog will eat your pillow"]


@app.route("/compliment")
def get_compliment():
	name = request.args.get('name')
	compliment = choice(compliments)
	return f'Hello there, {name}! You are so {compliment}!'

@app.route("/horoscope")
def get_horoscope():
	prediction = choice(predictions)
	return f'{prediction}'

@app.route('/')
def index():
    """Show the homepage and ask the user's name."""
    return render_template('index.html')

if __name__ == "__main__":
	app.run(debug = True)


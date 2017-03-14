from flask import Flask
from flask import url_for
from flask import render_template


app = Flask(__name__)

@app.route("/")
def home():
	return render_template('home.html', title='home')

@app.route("/list")
def list():
	return render_template('list.html',title='list')

@app.route("/settings")
def settings():
	return render_template('settings.html',title='settings')

if __name__ == "__main__":
	app.run()
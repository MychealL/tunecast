from flask import Flask
from flask import url_for
from flask import render_template

app = Flask(__name__)



@app.route("/")
def hello():
   	return render_template('home.html', title='home')

@app.route("/something")
def something():
	return "Something else!"

if __name__ == "__main__":
    app.run()
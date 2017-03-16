from __future__ import print_function
from flask import Flask, request, render_template, url_for
import os

music_dir = 'static/music'
image_dir = 'static/images'
current = 0
key = 'sun'
playlist = {}
playlist[0] = [f for f in os.listdir('static/music/sun') if f.endswith('mp3')]
playlist[1] = [f for f in os.listdir('static/music/rain') if f.endswith('mp3')]
playlist[2] = [f for f in os.listdir('static/music/snow') if f.endswith('mp3')]


app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html',
                           title='Sun',
                           playlist=playlist,
                           current=0,
                           key=key,
                           image_dir='static/images/sun/sun_tunecast.jpg')


@app.route("/home_two")
def home_two():
    return render_template('home_two.html',
                           title='Rain',
                           current=1,
                           playlist=playlist,
                           key='rain',
                           image_dir='static/images/rain/rain_tunecast.jpg')


@app.route("/home_three")
def home_three():
    return render_template('home_three.html',
                           title='Snow',
                           current=2,
                           playlist=playlist,
                           key='snow',
                           image_dir='static/images/snow/snow_tunecast.jpg')


@app.route("/list")
def list():
    return render_template('list.html',
                           title='list',
                           playlist=playlist)


@app.route("/settings")
def settings():
    return render_template('settings.html', title='settings')


if __name__ == "__main__":
    app.run(debug=True, threaded=True)

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
                           title='home',
                           playlist=playlist,
                           current=current,
                           key=key,
                           image_dir=image_dir)


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

from __future__ import print_function
from flask import Flask, request, render_template, url_for
import os

music_dir = 'static/music'
music_files = [f for f in os.listdir(music_dir) if f.endswith('mp3')]
music_files_number = len(music_files)

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html',
                           title='home',
                           music_files=music_files,
                           music_files_number=music_files_number)


@app.route("/list")
def list():
    return render_template('list.html',
                           title='list',
                           music_files_number=music_files_number,
                           music_files=music_files)


@app.route("/settings")
def settings():
    return render_template('settings.html', title='settings')


if __name__ == "__main__":
    app.run(debug=True, threaded=True)

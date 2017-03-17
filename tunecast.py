from __future__ import print_function
from flask import Flask, request, render_template, url_for, redirect
import os

music_dir = 'static/music'
image_dir = 'static/images'
current = 0
key = 'sun'
playlist = {}
playlist[0] = [f for f in os.listdir('static/music/sun') if f.endswith('mp3')]
playlist[1] = [f for f in os.listdir('static/music/rain') if f.endswith('mp3')]
playlist[2] = [f for f in os.listdir('static/music/snow') if f.endswith('mp3')]

global logged_in
logged_in = False

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    print(request.method)
    if request.method == 'POST':
        print("test");
        global logged_in
        logged_in = True
        return redirect("/", code=302)

    return render_template('login.html')

@app.route("/")
def home():
    global logged_in
    if not logged_in: 
       return redirect("/login", code=302)

    return render_template('home.html',
                           title='Sun',
                           playlist=playlist,
                           current=0,
                           key=key,
                           image_dir='https://image.flaticon.com/icons/svg/136/136723.svg')


@app.route("/home_two")
def home_two():
    global logged_in
    if not logged_in: 
       return redirect("/login", code=302)
    return render_template('home_two.html',
                           title='Rain',
                           current=1,
                           playlist=playlist,
                           key='rain',
                           image_dir='https://getreferralmd.com/wp-content/uploads/2015/10/rain.png')


@app.route("/home_three")
def home_three():
    global logged_in
    if not logged_in: 
       return redirect("/login", code=302)
    return render_template('home_three.html',
                           title='Snow',
                           current=2,
                           playlist=playlist,
                           key='snow',
                           image_dir='http://www.myiconfinder.com/uploads/iconsets/256-256-6bda2f56698d9f7d5f0255c12757b2f2-snow.png')


@app.route("/list")
def list():
    global logged_in
    if not logged_in: 
       return redirect("/login", code=302)
    return render_template('list.html',
                           title='list',
                           playlist=playlist)


@app.route("/settings")
def settings():
    global logged_in
    if not logged_in: 
       return redirect("/login", code=302)

    return render_template('settings.html',
                           title='Settings',
                           image_dir='static/images/spotify/spotifylogo.png')



if __name__ == "__main__":
    app.run(debug=True, threaded=True)

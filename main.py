from flask import Flask, render_template
from db import *

# luodaan Flask-applikaatio:
app = Flask("flask-blogit")

@app.route("/")
def home():
    all_blogs = get_all_blogs()
    return render_template("index.html",blogs=all_blogs, title="HOME")
     
app.run() # käynnistää applikaation selaimessa, jää päälle
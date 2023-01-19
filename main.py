from flask import Flask, render_template, request, redirect, flash
from db import *

# luodaan Flask-applikaatio:
app = Flask("flask-blogit")

# flash vaatii secret_key -muuttujan
app.secret_key = b'_5#y'

@app.route("/")
def home():
    all_blogs = get_all_blogs()
    return render_template("index.html",blogs=all_blogs, title="HOME")
     
@app.route("/blogs/create", methods=['POST', 'GET']) 
def create():
    if request.method =='GET':
        return render_template("create.html", title="CREATE BLOG")    
    elif request.method =='POST':
        save_blog(request.form) #lähetetään koko form        
        flash("BLOG CREATED!")
        return redirect("/")

@app.route("/blogs/<id>") #<string:id> <int:id>
def show_blog(id): #näyttää painetun blogin sisällön
    # eli näyttää blog.html -tiedoston.
    blog_by_id = get_blog_by_id(id)
    return render_template('blog.html', blog=blog_by_id, title="Blog Details")

@app.route("/blogs/delete/<id>")
def delete_blog(id):
    delete_blog_by_id(id)
    flash("Blog deleted!")
    #return redirect("/")
    return "JEFDKJDSF"



app.run() # käynnistää applikaation selaimessa, jää päälle
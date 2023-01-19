from flask import Flask, render_template, request, redirect, flash, jsonify
from db import *
import json
from bson import json_util

# luodaan Flask-applikaatio:
app = Flask("flask-blogit")

# flash vaatii secret_key -muuttujan
app.secret_key = b'_5#y'

@app.route("/")
def home():
    all_blogs = get_all_blogs()
    return render_template("index.html",blogs=all_blogs, title="HOME")

@app.route("/about")
def about():
    return "INSERT ABOUT PAGE HERE"

@app.route("/blogs/create", methods=['POST', 'GET']) 
def create():
    if request.method =='GET':
        return render_template("create.html", title="CREATE BLOG")    
    elif request.method =='POST':
        save_blog(request.form) #lähetetään koko form        
        flash("BLOG CREATED!")
        return redirect("/")

@app.route("/blogs/<id>") #<string:id> <int:id>
def show_blog(id): #näyttää painetun blogin sisällön, eli blog.html -tiedoston.
    blog_by_id = get_blog_by_id(id)
    return render_template('blog.html', blog=blog_by_id, title="Blog Details")

@app.route("/blogs/delete/<id>")
def delete_blog(id):
    delete_blog_by_id(id)
    flash("Blog deleted!")
    return redirect("/")
    
@app.route("/blogs/update/<id>", methods=['POST', 'GET'])   
def update_blog(id):    
    if request.method=='GET': # SIVULLE MENNÄÄN        
        blog_by_id = get_blog_by_id(id)     
        return render_template("update.html", form=blog_by_id, id=id)
    elif request.method=='POST': #PAINETTIIN update.html-sivulla Update-nappia
        update_blog_by_id(request.form, id)
        flash("Blog Updated!")
        return redirect("/")

@app.route("/api/<id>")
def get_blog_by_lkjfds(id):    
    blog =get_blog_by_num(id)    
    return json.loads(json_util.dumps(blog))            
    

app.run() # käynnistää applikaation selaimessa, jää päälle
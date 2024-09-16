#minimal FLask app
from flask import Flask, render_template, request, redirect, url_for

#print("Starting flask progmra from ",__names__)
app = Flask(__name__)
#Do any app specific setup here
#for instance, loading a database
app.config["DEBUG"] = True #will run in a debug mod
# TODO: make this a database or something
comments = []

@app.route("/",methods=["GET", "POST"]) #we allow posting

def index():
    if request.method == "GET":
        return render_template("main_page.html", comments=comments)
    #otherwise, its a post

    comments.append(request.form["contents"])
    return redirect(url_for('index'))


#@app.route("/")
#def hello_world():
   # return "<p>Welcome to my shiny new flask app!</p>"



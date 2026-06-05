from flask import Flask, render_template, request, session
from datafile import filename        
import subs.index_subs as indexSubs
from classes.userlogin import Userlogin

app = Flask(__name__)

Userlogin.read(filename + 'DadaBase_Podcast.db')
prev_option=''
app.secret_key = 'BAD_SECRET_KEY'  

path = filename + 'DadaBase_Podcast.db'

@app.route("/", methods=["POST", "GET"])
def index():
    return indexSubs.index(path)
@app.route("/login")
def login():
    return render_template("login.html", id=0, user="", password="", ulogin=session.get("user"), resul="")

@app.route("/logoff")
def logoff():
    session.pop("user", None)
    return render_template("index.html", ulogin=session.get("user"))

@app.route("/chklogin", methods=["post","get"])
def chklogin():
    user = request.form["user"]
    password = request.form["password"]
    resul = Userlogin.chk_password(user, password)
    if resul == "Valid":
        session["user"] = user
        return render_template("index.html", ulogin=session.get("user"))
    return render_template("login.html", user=user, password=password, ulogin=session.get("user"), resul=resul)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)

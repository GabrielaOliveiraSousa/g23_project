
from flask import Flask, render_template, request, session
from classes.guest import Guest
from datafile import filename
from classes.participation import Participation
from classes.podcast import Podcast
from classes.sponsor import Sponsor
from classes.theme import Theme
from classes.userlogin import Userlogin
from subs.apps_podcast import apps_podcast
from subs.apps_gform import apps_gform 
from subs.apps_subform import apps_subform 
from subs.apps_userlogin import apps_userlogin

app = Flask(__name__)

Podcast.read(filename + 'DadaBase_Podcast.db')
Guest.read(filename + 'DadaBase_Podcast.db')
Participation.read(filename + 'DadaBase_Podcast.db')
Sponsor.read(filename + 'DadaBase_Podcast.db')
Theme.read(filename + 'DadaBase_Podcast.db')
Userlogin.read(filename + 'DadaBase_Podcast.db')
app.secret_key = 'BAD_SECRET_KEY'
@app.route("/")
def index():
    return render_template("index.html", ulogin=session.get("user"))
@app.route("/login")
def login():
    return render_template("login.html", user= "", password="", ulogin=session.get("user"),resul = "")
@app.route("/logoff")
def logoff():
    session.pop("user",None)
    return render_template("index.html", ulogin=session.get("user"))
@app.route("/chklogin", methods=["post","get"])
def chklogin():
    user = request.form["user"]
    password = request.form["password"]
    resul = Userlogin.chk_password(user, password)
    if resul == "Valid":
        session["user"] = user
        return render_template("index.html", ulogin=session.get("user"))
    return render_template("login.html", user=user, password = password, ulogin=session.get("user"),resul = resul)
@app.route("/Podcast", methods=["post","get"])
def podcast():
    return apps_podcast()
@app.route("/gform/<cname>", methods=["post","get"])
def gform(cname):
    return apps_gform(cname)
@app.route("/subform/<cname>", methods=["post","get"])
def subform(cname):
    return apps_subform(cname)
@app.route("/plot", methods=["post","get"])
def plot():
    return apps_plot()
@app.route("/plotly", methods=["post", "get"])
def plotly():
    return apps_plotly()          
@app.route("/Userlogin", methods=["post","get"])
def userlogin_route():
    return apps_userlogin()
if __name__ == '__main__':
    app.run()

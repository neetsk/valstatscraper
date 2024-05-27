from flask import Flask, url_for, request, render_template, redirect, abort
from markupsafe import escape
import requests
from secretkey import myToken

app = Flask((__name__))

RIOTAPIAUTHENTICATE = "https://na.api.riotgames.com/val/status/v1/platform-data"

@app.route("/")
def index():
    return redirect(url_for("auth"))

@app.route("/auth")
def mainPage():
    apiAuthHeader = {
        "api_key": myToken
    }
    response = requests.get(RIOTAPIAUTHENTICATE, headers=apiAuthHeader)

    if response.status_code == 200:
        print(response.json())
        return "SUCCESS"
    else:
        return "FAILED"
    '''
    if True:
        return redirect(url_for(addTeam))
    if True:
        abort(404) #runs a 404
    return "hi"
    '''

@app.route("/<match>")
def showMatchStats(myMatch):
    render_template("test.html", match=myMatch)

@app.route("/addteam", methods=['GET', 'POST'])
def addTeam():
    if request.method == "POST":
        request.form['FIELD']
        return "POST ADD TEAM"

    
@app.route("/addplayer", methods=['GET', 'POST'])
def addPlayer():
    if request.method == "POST":
        return "POST ADD PLAYER"

@app.route("/addmatch", methods=['POST'])
def addMatch():
    if request.method == "POST":
        return "SHOW MATCHES"
    
@app.errorhandler(404)
def pageNotFound(error):
    return "NOT FOUND XD"

if __name__ == '__main__':
    app.run(debug=False)
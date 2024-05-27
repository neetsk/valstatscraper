from flask import Flask, url_for, request, render_template, redirect, abort
from markupsafe import escape
import requests
from secretkey import myToken
from endpoints import *

app = Flask((__name__))


@app.route("/")
def index():
    return redirect(url_for("mainPage"))

@app.route("/auth")
def mainPage():
    apiAuthHeader = {
        "Authorization": myToken
    }

    response = requests.get(RIOTAPIAUTHENTICATE, headers=apiAuthHeader)

    if response.status_code == 200:
        return "SUCCESS"
    else:
        return "FAILED with ", response.status_code

'''Get PUUID with Name + Tag'''
@app.route("/puuid/<name>/<tag>")
def getPUUID(name, tag):
    apiParams = {
        "api_key": myToken
    }

    response = requests.get(RIOTAPI_ACCOUNTS_BY_RIOT_ID + name + "/" + tag, params=apiParams)

    if response.status_code == 200:
        return response.json()['puuid']
    else:
        return "FAILED with ", response.status_code


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
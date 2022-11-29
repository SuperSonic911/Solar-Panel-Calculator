from flask import Flask, flash, jsonify, redirect, render_template, request, session
import json
from math import ceil

#auto reload flask #flask --app app.py --debug run
# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

#Solar Cell Specifications EVPV370
ratedPower = 430
maxVoltage = 42
openCircuitVoltage = 49
shortCircuitCurrent = 10.8
noct = 44
#dimension in meter
length = 1.04 
width = 1.865 

#import json file as dictionary
with open("test2.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

#import countries, used in jinja dropdown
with open("countries.txt") as f:
    countries_array = []
    while True:
        line = f.readline()
        if not line:
            break
        countries_array.append(line.strip())


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


#home page
@app.route("/")
def home():
    return render_template("home.html")

#form (build) page
@app.route("/build", methods=["GET", "POST"])
def build():
    if request.method == "POST":
        #form
        E = request.form.get("E", type=float) #Energy per year from user
        if not E or E < 0:
            return "<p>Please enter a positive number for energy consumption</p>"
        E = E * 1000  #in watts
        country = request.form.get("country")  #choose country
        if country == "Select your country":  #just to exclude the empty option
            return "<p> Please select a country from the dropdown menu</p>"
        dni = jsonObject[country]["dni"]
        temp = jsonObject[country]["temp"]
        Pac = E / (dni * 365)
        tcell = temp + (noct - 20)/0.8
        ntemp = 1 - (0.005 * (tcell - 25))
        Pdc = Pac / (0.97 * 0.96 * 0.96 * ntemp)
        noCells = int(ceil(Pdc / ratedPower))
        #either one cell or a double number of solar cells
        if noCells == 1:
            pass
        elif noCells % 2 == 1:
            noCells += 1
        series = noCells
        parallel = 1
        
        #finalization
        Egenerated = noCells * ratedPower * 10**-3 * dni * 365 * 0.97 * 0.96 * 0.96 * ntemp
        #find out space needed at roof
        totalWidth = int(ceil(width * noCells))
        totalLength = int(ceil(length * noCells))

        Egenerated = ceil(Egenerated)

        return render_template("results.html", totalWidth=totalWidth, totalLength=totalLength,
         noCells=noCells, series=series, parallel=parallel, Egenerated=Egenerated)
    else:
        return render_template("build.html", countries_array=countries_array)


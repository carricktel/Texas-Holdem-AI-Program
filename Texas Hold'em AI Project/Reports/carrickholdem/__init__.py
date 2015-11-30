from flask import Flask, render_template, request, url_for, redirect
from THAIP_Class_Card import Card
from THAIP_Class_Table import Table
from THAIP_Class_GamePhase import GamePhase
from THAIP_Class_DetermineHand import DetermineHand
from THAIP_Class_AI import AI
import time
import copy
app = Flask(__name__)
##@app.route("/")
##def init():
##    return render_template('index.html')

#Instantiate a Table object
table = Table(100,100,1)

#Instantiate a GamePhase object
phase = GamePhase()

@app.route("/")
def main():
    return render_template('index.html',outtext = "hello world.")

@app.route("/", methods=['GET','POST'])
def submit():
    if request.method == "POST":
        oldtext = request.form['interface']
        newtext = request.form['userinput']
        outtext = str(oldtext) + "\n" + str(newtext)
        return render_template('index.html', outtext = outtext)


if __name__ == "__main__":
	app.run()

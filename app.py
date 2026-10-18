mport os
import random
import sys

from flask import Flask, render_template
from flask import jsonify, session


def resource_path(relative_path):
    
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


app = Flask(
    __name__,
    template_folder=resource_path("templates"),
    static_folder=resource_path("static"),
)

app.secret_key = "5405897392830934598734593"

#--* Variablen *---


@app.route("/") # <---- Index HTML
def start():
    return render_template("index.html")



@app.route("/highscore")  # <----- Highscore Update durch return von /click
def highscore():
    global Highscore
    return str(Highscore)
    

@app.route("/click")  # <------ click berechnung
def click():
    global Highscore
   
    click_count = session.get("click_count", 0) # | Defintion von click count
    
    
    click_count += 1
    if random.randint(1, 100) <= click_count:
        click_count = 0  
    if click_count > Highscore:
        Highscore = click_count

    session["click_count"] = click_count 
    

    return str(click_count)


if __name__ == "__main__": # <---- Main loop
    app.run(debug=True)

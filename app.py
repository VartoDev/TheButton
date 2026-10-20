import random
from flask import Flask, render_template
from flask import jsonify, session

app = Flask(__name__)

app.secret_key = "5405897392830934598734593"

#--* Variablen *---
Highscore = 0


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
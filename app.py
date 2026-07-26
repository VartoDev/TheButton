import random
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def start():
    return render_template("index.html")
click_count = 0
Verlieren = 0
Highscore = 0
Cat = False
Resetstart = False
Sound_für_Verlieren = False
@app.route("/highscore")
def highscore():
    global Highscore

    if click_count > Highscore:
        Highscore = click_count

    return str(Highscore)
@app.route("/Reset")

def Reset():
    global Resetstart
    global click_count
    global Sound_für_Verlieren
    if Reset == True and click_count == 0:
        Sound_für_Verlieren = True
    else:
        Sound_für_Verlieren = False

        return bool(Sound_für_Verlieren)


@app.route("/Zielerreicht")
def Zielerreicht():
    global click_count
    global Cat

    if click_count == 30:
        Cat = True # wenn man 30 clicks erreicht dann kommt eine KAtze
    return(Cat)

@app.route("/click")

def click():
    global click_count
    global Verlieren
    global Resetstart
   
    
    click_count += 1
    Resetstart = True
    Verlieren +=1
    
    #for i in range (Verlieren):
        #Chance = random.randint(1, 100) 
        #if Chance == 100:
            #click_count = 0
        
    chance = random.randint(1,100)

    if chance <= click_count:
      click_count = 0

    

    
    
    
   

    return str(click_count)


if __name__ == "__main__":
    app.run(debug=True)
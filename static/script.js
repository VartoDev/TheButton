const button = document.getElementById("theButton");
const clickCountElement = document.getElementById("clickCount");
const highscoreElement = document.getElementById("Highscore");
const loginElement = document.getElementById("login");
const sound = new Audio("/static/sounds/dragon-studio-button-press-382713.mp3");
const sound2 = new Audio("/static/sounds/freesound_community-wrong-38598.mp3")

button.addEventListener("click", function() {
    
    sound.currentTime = 0;
    sound.play();
    fetch("/click")
        .then(response => response.text())
        .then(text => {
            console.log(text);
            
            clickCountElement.textContent = text;
            if (clickCountElement.textContent === "0") { 
                 sound2.currentTime = 0;
                 sound2.play();
          }
        });
});

button.addEventListener("click", function() {
    fetch("/highscore")
        .then(response => response.text())
        .then(text => {
            console.log(text);
            highscoreElement.textContent = "Highscore: " + text;
        });
});


function playPress() {
    button.classList.remove("pressing");
    void button.offsetWidth;
    button.classList.add("pressing");
}

button.addEventListener("pointerdown", playPress);
button.addEventListener("animationend", () => button.classList.remove("pressing"));




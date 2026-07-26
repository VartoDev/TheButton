const button = document.getElementById("theButton");
const clickCountElement = document.getElementById("clickCount");
const highscoreElement = document.getElementById("Highscore");
button.addEventListener("click", function() {
    const sound = new Audio("/static/sounds/universfield-mouse-click-351398.mp3");
    const sound2 = new Audio("/static/sounds/freesound_community-wrong-38598.mp3")
    sound.play();
    fetch("/click")
        .then(response => response.text())
        .then(text => {
            console.log(text);
            
            clickCountElement.textContent = text;
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





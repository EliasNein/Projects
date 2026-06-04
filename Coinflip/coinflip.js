function coinFlip(playerMove) {
  let result = document.querySelector(".paragraph");
  let computerMove = Math.random();
  let computerOutput = "";
  if (computerMove < 0.5) {
    computerOutput = "kopf";
  } else {
    computerOutput = "zahl";
  }

  if (playerMove === computerOutput) {
    result.innerHTML = "You win";
  } else {
    result.innerHTML = "You lose";
  }

  JSON.parse(localStorage.getItem('score'));

  updateScore(result.innerHTML);
}

let score = JSON.parse(localStorage.getItem("score")) || {
  wins: 0,
  losses: 0,
};

function updateScore(result) {
  if (result === "You win") {
    score.wins += 1;
  } else if (result === "You lose") {
    score.losses += 1;
  }

  localStorage.setItem("score", JSON.stringify(score));

  document.querySelector(".score").innerHTML =
    `Wins: ${score.wins}, Losses: ${score.losses}`;
}

function resetScore() {
  score = {
    wins: 0,
    losses: 0,
  };

  updateScore();

  document.querySelector(".score").innerHTML =
    `Wins: ${score.wins}, Losses: ${score.losses}`;
}

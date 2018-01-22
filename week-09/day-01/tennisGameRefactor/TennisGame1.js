'use strict'

var TennisGame1 = function () {
  this.firstPlayerScore = 0;
  this.secondPlayerScore = 0;
};

TennisGame1.prototype.wonPoint = function (playerName) {
  playerName === 'player1' ? this.firstPlayerScore++ : this.secondPlayerScore++;
};

function checkEqual(firstPlayerScore) {
  return {0: 'Love-All', 1: 'Fifteen-All', 2: 'Thirty-All'}[firstPlayerScore] || 'Deuce';
}

function checkWinOrAdvantage(difference) {
  if (Math.abs(difference) >= 2) {
    return difference >= 2 ? 'Win for player1' : 'Win for player2';
  }
  return difference === 1 ? 'Advantage player1' : 'Advantage player2';
}

function scoresOut(player) {
  return {0: 'Love', 1: 'Fifteen', 2: 'Thirty'}[player] || 'Forty';
}

TennisGame1.prototype.getScore = function () {
  let score = '';
  let tempScore = 0;
  if (this.firstPlayerScore === this.secondPlayerScore) {
    return checkEqual(this.firstPlayerScore);

  } else if (this.firstPlayerScore >= 4 || this.secondPlayerScore >= 4) {
    return checkWinOrAdvantage(this.firstPlayerScore - this.secondPlayerScore);

  } else {
    for (let i = 1; i < 3; i++) {
      i === 1 ? score += scoresOut(this.firstPlayerScore) : score += '-' + scoresOut(this.secondPlayerScore);
    }
  }
  return score;
};

if (typeof window === 'undefined') module.exports = TennisGame1;

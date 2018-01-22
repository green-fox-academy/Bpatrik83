var TennisGame2 = function(firstPlayerName, secondPlayerName) {
  this.firstPlayerPoint = 0;
  this.secondPlayerPoint = 0;

  this.firstPlayerResult = "";
  this.secondPlayerResult = "";

};

TennisGame2.prototype.getScore = function() {
  let score = "";

  if (this.firstPlayerPoint === this.secondPlayerPoint && this.firstPlayerPoint < 3) {
    if (this.firstPlayerPoint === 0)
      score = "Love";
    if (this.firstPlayerPoint === 1)
      score = "Fifteen";
    if (this.firstPlayerPoint === 2)
      score = "Thirty";
    score += "-All";
  }
  if (this.firstPlayerPoint === this.secondPlayerPoint && this.firstPlayerPoint > 2)
    score = "Deuce";

  if (this.firstPlayerPoint > 0 && this.secondPlayerPoint === 0) {
    if (this.firstPlayerPoint === 1)
      this.firstPlayerResult = "Fifteen";
    if (this.firstPlayerPoint === 2)
      this.firstPlayerResult = "Thirty";
    if (this.firstPlayerPoint === 3)
      this.firstPlayerResult = "Forty";

    this.secondPlayerResult = "Love";
    score = this.firstPlayerResult + "-" + this.secondPlayerResult;
  }
  if (this.secondPlayerPoint > 0 && this.firstPlayerPoint === 0) {
    if (this.secondPlayerPoint === 1)
      this.secondPlayerResult = "Fifteen";
    if (this.secondPlayerPoint === 2)
      this.secondPlayerResult = "Thirty";
    if (this.secondPlayerPoint === 3)
      this.secondPlayerResult = "Forty";

    this.firstPlayerResult = "Love";
    score = this.firstPlayerResult + "-" + this.secondPlayerResult;
  }

  if (this.firstPlayerPoint > this.secondPlayerPoint && this.firstPlayerPoint < 4) {
    if (this.firstPlayerPoint === 2)
      this.firstPlayerResult = "Thirty";
    if (this.firstPlayerPoint === 3)
      this.firstPlayerResult = "Forty";
    if (this.secondPlayerPoint === 1)
      this.secondPlayerResult = "Fifteen";
    if (this.secondPlayerPoint === 2)
      this.secondPlayerResult = "Thirty";
    score = this.firstPlayerResult + "-" + this.secondPlayerResult;
  }
  if (this.secondPlayerPoint > this.firstPlayerPoint && this.secondPlayerPoint < 4) {
    if (this.secondPlayerPoint === 2)
      this.secondPlayerResult = "Thirty";
    if (this.secondPlayerPoint === 3)
      this.secondPlayerResult = "Forty";
    if (this.firstPlayerPoint === 1)
      this.firstPlayerResult = "Fifteen";
    if (this.firstPlayerPoint === 2)
      this.firstPlayerResult = "Thirty";
    score = this.firstPlayerResult + "-" + this.secondPlayerResult;
  }

  if (this.firstPlayerPoint > this.secondPlayerPoint && this.secondPlayerPoint >= 3) {
    score = "Advantage player1";
  }

  if (this.secondPlayerPoint > this.firstPlayerPoint && this.firstPlayerPoint >= 3) {
    score = "Advantage player2";
  }

  if (this.firstPlayerPoint >= 4 && this.secondPlayerPoint >= 0 && (this.firstPlayerPoint - this.secondPlayerPoint) >= 2) {
    score = "Win for player1";
  }
  if (this.secondPlayerPoint >= 4 && this.firstPlayerPoint >= 0 && (this.secondPlayerPoint - this.firstPlayerPoint) >= 2) {
    score = "Win for player2";
  }
  return score;
};

TennisGame2.prototype.SetP1Score = function(number) {
  var i;
  for (i = 0; i < number; i++) {
    this.P1Score();
  }
};

TennisGame2.prototype.SetP2Score = function(number) {
  var i;
  for (i = 0; i < number; i++) {
    this.P2Score();
  }
};

TennisGame2.prototype.P1Score = function() {
  this.firstPlayerPoint++;
};

TennisGame2.prototype.P2Score = function() {
  this.secondPlayerPoint++;
};

TennisGame2.prototype.wonPoint = function(player) {
  if (player === "player1")
    this.P1Score();
  else
    this.P2Score();
};

if (typeof window === "undefined") {
  module.exports = TennisGame2;
}
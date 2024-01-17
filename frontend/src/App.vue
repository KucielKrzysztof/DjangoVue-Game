<template>
	<div id="app">
		<h1>Rock Paper Scissors Game</h1>

		<!-- Show the start button if the game hasn't started -->
		<div v-if="!gameStarted">
			<button @click="startGame">Start</button>
			<button @click="goToScoreboard">Scoreboard</button>
		</div>

		<!-- Show the game interface if the game has started -->
		<div v-else-if="!gameOver">
			<p>Streak: {{ streakPoints }}</p>
			<h2>Choose your move:</h2>
			<button @click="makeMove('rock')">Rock</button>
			<button @click="makeMove('paper')">Paper</button>
			<button @click="makeMove('scissors')">Scissors</button>
			<p v-if="playerMove">Your move: {{ playerMove }}</p>
			<p v-if="opponentMove">Opponent's move: {{ opponentMove }}</p>
			<p v-if="gameResult">{{ gameResult }}</p>
		</div>

		<!-- <div v-else>
			<h2>Game Over</h2>
			<p>Your streak points: {{ streakPoints }}</p>
			<label for="playerName">Enter your name:</label>
			<input v-model="playerName" id="playerName" type="text" />
			<button @click="submitScore">Submit Score</button>
		</div> -->
		<div v-if="gameOver && streakPoints > 0">
			<h2>Game Over</h2>
			<p>Your streak points: {{ streakPoints }}</p>
			<label for="playerName">Enter your name:</label>
			<input v-model="playerName" id="playerName" type="text" />
			<button @click="submitScore">Submit Score</button>
		</div>
		<div v-else-if="gameOver">
			<h2>Game Over</h2>
			<p>Your streak points: {{ streakPoints }}</p>
			<p>
				Sorry, you didn't score any points this time. Better luck next time!
			</p>
			<button @click="reloadPage">Retry</button>
		</div>
	</div>
</template>

<script>
import axios from "axios";
export default {
	data() {
		return {
			moves: ["rock", "paper", "scissors"],
			playerMove: null,
			opponentMove: null,
			gameOver: false,
			streakPoints: 0,
			playerName: "",
			gameStarted: false,
			gameResult: null,
		};
	},
	methods: {
		startGame() {
			// Add this method
			this.gameStarted = true;
		},
		goToScoreboard() {
			window.location.href = "http://localhost:8000/scoreboard";
		},
		makeMove(move) {
			this.playerMove = move;
			this.opponentMove = this.getRandomMove();
			this.determineWinner();
		},
		getRandomMove() {
			const randomIndex = Math.floor(Math.random() * this.moves.length);
			return this.moves[randomIndex];
		},
		determineWinner() {
			if (this.playerMove === this.opponentMove) {
				this.gameResult = "draw";
			} else if (
				(this.playerMove === "rock" && this.opponentMove === "scissors") ||
				(this.playerMove === "paper" && this.opponentMove === "rock") ||
				(this.playerMove === "scissors" && this.opponentMove === "paper")
			) {
				this.gameResult = "win";
				this.streakPoints++;
			} else {
				// Player loses
				this.gameOver = true;
			}
		},
		reloadPage() {
			window.location.reload();
		},
		submitScore() {
			// Implement logic to submit score to scoreboard
			console.log(`Player: ${this.playerName}, Score: ${this.streakPoints}`);
			// Tworzymy obiekt z danymi do wysłania na backend
			const dataToSend = {
				player_name: this.playerName,
				score: this.streakPoints,
			};
			// Wysyłamy dane na backend za pomocą żądania POST
			axios
				.post("http://localhost:8000/api/submit_score/", dataToSend)
				.then((response) => {
					console.log(response.data.message);
					window.location.reload();
				})
				.catch((error) => {
					console.error("Error submitting score:", error);
					// Tutaj możesz obsłużyć błąd, jeśli zachodzi
				});
		},
	},
	watch: {
		streakPoints(newVal) {
			console.log("Streak teraz:", newVal);
		},
	},
};
</script>

<style>
#app {
	text-align: center;
	margin-top: 60px;
}

button {
	margin: 10px;
	padding: 5px 10px;
	font-size: 16px;
}
</style>

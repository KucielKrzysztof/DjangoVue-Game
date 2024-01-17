<template>
	<b-container>
		<b-row align-h="center">
			<b-col xs="12" md="8" lg="6">
				<div id="app">
					<div class="logo">
						Rock Paper Scissors <br />
						Game
					</div>

					<!-- Menu gry/Starting Page coś takiego-->
					<div v-if="!gameStarted">
						<div class="menu-buttons">
							<button @click="startGame" class="aqua menu-button">Start</button>
							<button @click="goToScoreboard" class="aqua menu-button">Scoreboard</button>
						</div>
					</div>

					<!-- Po wystartowaniu gry-->
					<div v-else-if="!gameOver">
						<p style="color: gold">
							Streak: <span style="color: red">{{ streakPoints }}</span>
						</p>
						<h2>Choose your move:</h2>
						<button @click="makeMove('rock')" class="hover_bordered_button">
							<img :src="require('@/assets/rock.png')" alt="Rock" />
						</button>
						<button @click="makeMove('paper')" class="hover_bordered_button">
							<img :src="require('@/assets/paper.png')" alt="Paper" />
						</button>
						<button @click="makeMove('scissors')" class="hover_bordered_button">
							<img :src="require('@/assets/scissors.png')" alt="Scissors" />
						</button>
						<h2>Round result:</h2>
						<div style="display: flex; justify-content: center; align-items: center; gap: 32px">
							<p v-if="playerMove">Your move:</p>
							<p v-if="opponentMove">Enemy Move:</p>
						</div>
						<div style="display: flex; justify-content: center; align-items: center">
							<p v-if="playerMove">
								<img :src="require(`@/assets/${playerMove}.png`)" alt="Player's Move" />
							</p>
							VS
							<p v-if="opponentMove">
								<img :src="require(`@/assets/${opponentMove}.png`)" alt="Oponent's move" />
							</p>
						</div>
						<p v-if="gameResult">
							Game Result: <span style="color: gold">{{ gameResult }}</span>
						</p>
					</div>

					<!-- Zakończenie gry -->
					<div v-if="gameOver && streakPoints > 0">
						<h2>Game Over</h2>
						<p>
							Your streak points:
							<span style="color: red">{{ streakPoints }}</span>
						</p>
						<label for="playerName">Enter your name:</label>
						<input v-model="playerName" id="playerName" type="text" maxlength="6" />
						<br />
						<button @click="submitScore" class="bordered_button" style="margin-top: 10px; margin-bottom: 10px">Submit Score</button>
						<br /><button @click="reloadPage" class="btn btn-primary">Retry</button>
					</div>

					<div v-else-if="gameOver">
						<h2><span style="color: red">Game Over</span></h2>
						<p>
							Your streak points:<span style="color: red">{{ streakPoints }}</span>
						</p>
						<p>Sorry, you didn't score any points this time. Better luck next time!</p>
						<button @click="reloadPage" class="btn btn-primary">Retry</button>
					</div>
				</div>
			</b-col>
		</b-row>
	</b-container>
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
				this.gameOver = true;
			}
		},
		reloadPage() {
			window.location.reload();
		},
		submitScore() {
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
					console.error("NIE DZIAŁA XD", error);
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
@import "./styles/main.min.css";
@import url("https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap");
#app {
	text-align: center;
	margin-top: 60px;
}
</style>

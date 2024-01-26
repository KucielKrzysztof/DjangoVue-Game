<template>
	<div id="game">
		<div class="logo">
			Rock Paper Scissors <br />
			Game
		</div>

		<!-- Menu gry/Starting Page coś takiego-->
		<div v-if="!gameStarted">
			<div class="menu-buttons">
				<button @click="startGame" class="aqua menu-button">Start</button>
				<router-link to="/scoreboard" class="aqua menu-button">Scoreboard</router-link>
				<router-link v-if="!isUserLoggedIn" to="/login" class="aqua menu-button">Login</router-link>
				<router-link v-if="!isUserLoggedIn" to="/register" class="aqua menu-button">Register</router-link>
				<router-link to="/reportbug" class="aqua menu-button">Report Bug</router-link>
				<button v-if="isUserLoggedIn" @click="logout" class="aqua menu-button" style="color: red !important">Logout</button>
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
			<label v-if="!isUserLoggedIn">Enter your name:</label>
			<input v-if="!isUserLoggedIn" v-model="playerName" id="playerName" type="text" maxlength="6" />
			<p v-else style="color: gold">Your name: {{ playerName }}</p>
			<br />
			<button @click="submitScore" class="btn" style="margin-top: 10px; margin-bottom: 10px; background-color: orange !important">
				Submit Score
			</button>
			<br /><button @click="reloadPage" class="btn btn-primary">Retry</button>
		</div>

		<div v-else-if="gameOver">
			<h2><span style="color: red">Game Over</span></h2>
			<h2>Round result:</h2>
			<div style="display: flex; justify-content: center; align-items: center; gap: 32px">
				<p v-if="playerMove">Your move:</p>
				<p v-if="opponentMove">Enemy Move:</p>
			</div>
			<img :src="require(`@/assets/${playerMove}.png`)" alt="Player's Move" />
			VS
			<img :src="require(`@/assets/${opponentMove}.png`)" alt="Oponent's move" />
			<p>
				Your streak points:<span style="color: red">{{ streakPoints }}</span>
			</p>
			<p>Sorry, you didn't score any points this time. Better luck next time!</p>
			<button @click="reloadPage" class="btn btn-primary">Retry</button>
		</div>
	</div>
</template>
<script>
import axios from "axios";
//import { watchEffect, ref } from "vue";
export default {
	//do testu ten setup tylko potem usune
	/* setup() {
		const user = ref(JSON.parse(localStorage.getItem("user")) || null);
		const accessToken = ref(localStorage.getItem("accessToken") || null);
		const refreshToken = ref(localStorage.getItem("refreshToken") || null);

		setInterval(() => {
			user.value = JSON.parse(localStorage.getItem("user")) || null;
			accessToken.value = localStorage.getItem("accessToken") || null;
			refreshToken.value = localStorage.getItem("refreshToken") || null;
		}, 1000);

		watchEffect(() => {
			console.log("User data:", user.value);
			console.log("Access Token:", accessToken.value);
			console.log("Refresh Token:", refreshToken.value);
		});
	}, */
	//dotąd usuwaj
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
			isUserLoggedIn: false,
		};
	},
	created() {
		this.isUserLoggedIn = !!localStorage.getItem("user");
		const user = localStorage.getItem("user") ? JSON.parse(localStorage.getItem("user")) : null;

		if (user && user.username) {
			this.playerName = user.username;
		}
	},
	components: {},
	methods: {
		startGame() {
			this.gameStarted = true;
		},
		logout() {
			// Usuń dane użytkownika z localStorage
			localStorage.removeItem("user");
			localStorage.removeItem("accessToken");
			localStorage.removeItem("refreshToken");
			// Ustaw dane na null to też do testów mam
			this.user = null;
			this.accessToken = null;
			this.refreshToken = null;

			// Ustaw flagę isUserLoggedIn na false
			this.isUserLoggedIn = false;

			// Przekieruj użytkownika do strony logowania
			this.$router.push("/");
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
			const user = localStorage.getItem("user") ? JSON.parse(localStorage.getItem("user")) : null;
			console.log(user);
			if (localStorage.getItem("user")) {
				this.playerName = user.username;
			}

			if (!this.playerName) {
				console.error("Player name is undefined.error");
				return;
			}
			console.log(`Player: ${this.playerName}, Score:
${this.streakPoints}`);
			const dataToSend = { player_name: this.playerName, score: this.streakPoints };
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
<style></style>

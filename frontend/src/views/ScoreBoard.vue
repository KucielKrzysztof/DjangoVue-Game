<template>
	<div class="container">
		<h1 class="scoreboard-title text-center my-4">Scoreboard</h1>

		<div class="box-element col-12 col-sm-10 col-md-8 col-lg-7 mx-auto">
			<div class="row">
				<div class="col-3 col-lg-2">Rank:</div>
				<div class="col-6 col-lg-7">Player Name:</div>
				<div class="col-3 col-lg-3">Score:</div>
			</div>
			<div v-for="(score, index) in scores" :key="index" class="row border-top row1">
				<div class="col-3 col-lg-2" :class="{ 'gold-text': index < 1 }">{{ index + 1 }}</div>
				<div class="col-6 col-lg-7" :class="{ 'gold-text': index < 1 }">{{ score.player_name }}</div>
				<div class="col-3 col-lg-3" :class="{ 'gold-text': index < 1 }">{{ score.max_score }}</div>
			</div>
			<div class="box-element back">
				<button @click="goBack" class="btn btn-primary">Go Back</button>
			</div>
		</div>
	</div>
</template>

<script>
import axios from "axios";

export default {
	data() {
		return {
			scores: [],
		};
	},
	methods: {
		goBack() {
			this.$router.go(-1);
		},
	},
	created() {
		axios
			.get("http://localhost:8000/api/scoreboard/")
			.then((response) => {
				this.scores = response.data;
			})
			.catch((error) => {
				console.error(error);
			});
	},
};
</script>

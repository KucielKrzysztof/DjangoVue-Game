<template>
	<b-container>
		<b-row align-h="center">
			<b-col xs="12" md="8" lg="6">
				<div id="app">
					<router-view />
				</div>
			</b-col>
		</b-row>
	</b-container>
</template>

<script></script>

<style>
@import "./styles/main.min.css";
@import url("https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap");
#app {
	text-align: center;
	margin-top: 60px;
}
</style>

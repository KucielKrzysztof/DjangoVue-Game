<template>
	<div>
		<div class="container">
			<h1 class="scoreboard-title text-center my-4">Login</h1>
			<p v-if="errorMessage" class="error">{{ errorMessage }}</p>
			<div class="form-container transparent-bg">
				<form @submit.prevent="submitLogin">
					<div>
						<label for="loginUsername">Username:</label>
						<input id="loginUsername" v-model="loginForm.username" type="text" required />
					</div>
					<div>
						<label for="loginPassword">Password:</label>
						<input id="loginPassword" v-model="loginForm.password" type="password" required />
					</div>
					<button type="submit">Login</button>
				</form>
			</div>
			<div class="login-button">
				<span>Don't have an account?</span>
				<button class="btn" @click="goToRegister" style="margin-left: 10px; background-color: orange">Register</button>
			</div>
		</div>
	</div>
</template>

<script>
import { reactive, toRaw, onMounted, ref } from "vue";
import axios from "axios";
import { useRouter, useRoute } from "vue-router";

export default {
	setup() {
		const loginForm = reactive({
			username: "",
			password: "",
		});
		const errorMessage = ref(null);
		const route = useRoute();
		const router = useRouter();

		function goToRegister() {
			router.push("/register");
		}
		//jesli przechodzimy z udanego rejestrowania to przekazuje nam username do forma
		onMounted(() => {
			if (route.query.username) {
				loginForm.username = route.query.username;
			}
		});

		async function submitLogin() {
			const formData = toRaw(loginForm);

			try {
				const response = await axios.post("http://localhost:8000/api/login/", formData);

				if (response.data.success) {
					console.log("Logowanie udane");
					// Zapisz dane użytkownika w localStorage
					const accessToken = response.data.access_token;
					const refreshToken = response.data.refresh_token;
					localStorage.setItem("user", JSON.stringify(response.data));
					localStorage.setItem("accessToken", accessToken);
					localStorage.setItem("refreshToken", refreshToken);
					router.push("/");
				} else {
					console.error("Błąd logowania:", response.data.message, response.data.errors);
					errorMessage.value = response.data.message;
				}
			} catch (error) {
				console.error("Błąd wysyłania danych:", error);
				if (error.response) {
					// Serwer zwrócił błąd, odczytaj komunikat o błędzie z odpowiedzi
					errorMessage.value = error.response.data.message;
				} else {
					// Inny błąd, np. problem z siecią
					errorMessage.value = "Failed to send data to server";
				}
			}
		}

		return { loginForm, submitLogin, errorMessage, goToRegister };
	},
};
</script>

<style scoped>
.container {
	box-sizing: border-box;
	max-width: 100%;
	overflow-x: hidden;
}
.transparent-bg {
	background-color: transparent !important;
	color: white !important;
	border: none !important;
}
.form-container {
	width: 100%;
	max-width: 600px;
	margin: 0 auto;
	padding: 20px;
	background-color: #f8f9fa;
	border: 1px solid #dee2e6;
	border-radius: 5px;
}

form div {
	margin-bottom: 10px;
}

form label {
	display: block;
	margin-bottom: 5px;
}

form input {
	width: 100%;
	padding: 5px;
	border: 1px solid #ced4da;
	border-radius: 3px;
	background-color: transparent !important;
	color: white !important;
}

form button {
	margin-top: 20px;
	padding: 10px 20px;
	background-color: #007bff;
	color: #fff;
	border: none;
	border-radius: 3px;
	cursor: pointer;
}
form button:hover {
	background-color: #0056b3;
}
.login-button {
	margin-top: 20px;
	margin-bottom: 20px;
}
</style>

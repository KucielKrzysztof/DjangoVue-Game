<template>
	<div class="container">
		<h1 class="scoreboard-title text-center my-4">Register</h1>
		<p v-if="errorMessage" class="error">{{ errorMessage }}</p>
		<div class="form-container transparent-bg">
			<form @submit.prevent="submitForm">
				<div>
					<label for="username">Username:</label>
					<input id="username" v-model="form.username" type="text" :readonly="submittedData" required />
					<p v-if="v$.username.$error" class="error">Username is invalid</p>
				</div>
				<div>
					<label for="email">Email:</label>
					<input id="email" v-model="form.email" type="email" :readonly="submittedData" required />
					<p v-if="v$.email.$error" class="error">Email is invalid</p>
				</div>
				<div>
					<label for="password">Password:</label>
					<input id="password" v-model="form.password" type="password" :readonly="submittedData" required />
					<p v-if="v$.password.$error" class="error">Password is invalid</p>
				</div>
				<div>
					<label for="confirmPassword">Confirm Password:</label>
					<input id="confirmPassword" v-model="form.confirmPassword" type="password" :readonly="submittedData" required />
					<p v-if="v$.confirmPassword.$error" class="error">Must be the same as password</p>
				</div>
				<div class="checkbox-container">
					<label for="terms">Accept Terms and Conditions:</label>
					<input id="terms" v-model="form.terms" type="checkbox" :readonly="submittedData" required />
					<p v-if="v$.terms.$error" class="error">You must accept the terms and conditions</p>
				</div>
				<div>
					<label for="location">Location:</label>
					<select id="location" v-model="form.location" :readonly="submittedData" required>
						<option value="">Where are you from</option>
						<option value="eu">Europe</option>
						<option value="na">North-America</option>
						<option value="sa">South-America</option>
						<option value="as">Asia</option>
						<option value="af">Africa</option>
						<option value="au">Australia</option>
						<option value="other">Other</option>
					</select>
				</div>
				<button type="submit">Register</button>
			</form>
		</div>
		<div v-if="submittedData" class="box-element col-12 col-sm-10 col-md-8 col-lg-7 mx-auto transparent-bg">
			<div class="card-header" style="color: green !important">Successfully registered</div>
			<div class="card-header">Your data:</div>
			<ul class="list-group list-group-flush">
				<li class="list-group-item transparent-bg" v-for="(value, key) in submittedData" :key="key">
					<strong>{{ key }}:</strong> {{ value }}
				</li>
			</ul>
		</div>
	</div>
</template>
<script>
import { reactive, nextTick, toRaw, ref } from "vue";
import { required, email } from "@vuelidate/validators";
import { useVuelidate } from "@vuelidate/core";
import axios from "axios";

export default {
	setup() {
		const form = reactive({
			username: "",
			email: "",
			password: "",
			confirmPassword: "",
			terms: false,
			location: "",
		});

		const passwordMatch = () => {
			return form.password === form.confirmPassword;
		};
		const notAdmin = (value) => value !== "admin";

		const rules = {
			username: { required, notAdmin },
			email: { required, email },
			password: { required },
			confirmPassword: { required, sameAs: passwordMatch },
			terms: { required },
			location: { required },
		};

		const v$ = useVuelidate(rules, form);

		const submittedData = ref(null);
		const errorMessage = ref(null);

		async function submitForm() {
			console.log("submitForm is called");
			console.log("v$ before $touch:", v$);
			await nextTick();
			v$.value.$touch();
			console.log("v$ after $touch:", v$);
			if (v$.value.$error) {
				console.log("Form is invalid");
				console.log("Validation state:", v$.value);
				console.log("username error:", v$.value.username.$error);
				console.log("email error:", v$.value.email.$error);
				console.log("password error:", v$.value.password.$error);
				console.log("confirmPassword error:", v$.value.confirmPassword.$error);
				console.log("terms error:", v$.value.terms.$error);
				console.log("location error:", v$.value.location.$error);
				return;
			}

			console.log("Form is valid", form);
			/* const formData = toRaw(form); */
			//const { confirmPassword, ...formData } = toRaw(form);
			let formData = toRaw(form);
			delete formData.confirmPassword;

			try {
				const response = await axios.post("http://localhost:8000/api/register/", formData);

				if (response.data.success) {
					submittedData.value = toRaw(form);
					console.log("Rejestracja udana");
					errorMessage.value = null;
				} else {
					console.error("Błąd rejestracji:", response.data.message);
					errorMessage.value = response.data.message;
				}
			} catch (error) {
				console.error("Błąd wysyłania danych:", error);
				if (error.response && error.response.data) {
					// Jeśli serwer zwróci konkretną wiadomośc to pokaże ją NIE ZAPOMNIJ ŻE TO TUTAJ
					errorMessage.value = error.response.data.message;
				} else {
					errorMessage.value = "Registration failed, try again later";
				}
			}
		}

		return { form, v$, submitForm, submittedData, errorMessage };
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

form input,
form select {
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
form select option {
	color: rgb(0, 0, 0);
}

form button:hover {
	background-color: #0056b3;
}
.checkbox-container {
	display: flex;
	align-items: center;
	justify-content: flex-start;
	white-space: nowrap;
}

.checkbox-container input[type="checkbox"] {
	transform: scale(1.5);
}
@media (max-width: 700px) {
	.checkbox-container {
		flex-direction: column;
	}

	.checkbox-container input[type="checkbox"] {
		margin-right: 0;
		margin-bottom: 10px;
	}
}
</style>

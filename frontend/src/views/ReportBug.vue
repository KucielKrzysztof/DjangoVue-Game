<template>
	<div class="container">
		<h1 class="scoreboard-title text-center my-4">Report Bug</h1>
		<p v-if="errorMessage" class="error">{{ errorMessage }}</p>
		<div class="form-container transparent-bg">
			<form @submit.prevent="submitBug">
				<div>
					<label for="bugTitle">Bug Title:</label>
					<input id="bugTitle" v-model="form.bugTitle" type="text" required />
					<p v-if="v$.bugTitle.$error" class="error">Bug title is required</p>
				</div>
				<div>
					<label for="bugDescription">Bug Description:</label>
					<textarea id="bugDescription" v-model="form.bugDescription" required></textarea>
					<p v-if="v$.bugDescription.$error" class="error">Bug description is required</p>
				</div>
				<div>
					<label for="bugSteps">Steps to Reproduce:</label>
					<textarea id="bugSteps" v-model="form.bugSteps" required></textarea>
					<p v-if="v$.bugSteps.$error" class="error">Steps to reproduce the bug are required</p>
				</div>
				<div>
					<label for="yourEmail">Your Email:</label>
					<input id="yourEmail" v-model="form.yourEmail" type="email" required />
					<p v-if="v$.yourEmail.$error" class="error">Email is required</p>
				</div>
				<button type="submit">Submit Bug Report</button>
			</form>
		</div>
	</div>
</template>

<script>
import { reactive, ref } from "vue";
import { required } from "@vuelidate/validators";
import { useVuelidate } from "@vuelidate/core";

export default {
	setup() {
		const form = reactive({
			bugTitle: "",
			bugDescription: "",
			bugSteps: "",
			yourEmail: "",
		});

		const rules = {
			bugTitle: { required },
			bugDescription: { required },
			bugSteps: { required },
			yourEmail: { required },
		};

		const v$ = useVuelidate(rules, form);
		const errorMessage = ref(null);

		async function submitBug() {
			v$.value.$touch();
			if (v$.value.$error) {
				errorMessage.value = "Please fill out all fields";
				return;
			}

			// Here, you would typically send the form data to your server
			console.log("Form is valid", form);
		}

		return { form, v$, submitBug, errorMessage };
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
form select,
textarea {
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
@keyframes flames {
	0% {
		color: #ff0000;
	}
	50% {
		color: #ff8000;
	}
	100% {
		color: #ff0000;
	}
}

.flames {
	animation: flames 1s infinite;
}
.login-button {
	margin-top: 20px;
	margin-bottom: 20px;
}
</style>

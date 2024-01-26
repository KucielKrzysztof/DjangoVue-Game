<template>
	<div class="container">
		<h1 class="scoreboard-title text-center my-4">Report Bug</h1>
		<p v-if="errorMessage" class="error">{{ errorMessage }}</p>
		<div class="form-container transparent-bg">
			<div v-if="submittedData" class="card-header" style="color: yellow !important">&#128274; Form now in readonyl mode &#128274;</div>
			<form @submit.prevent="submitBug">
				<div>
					<label for="yourEmail">Your Email:</label>
					<input id="yourEmail" v-model="form.yourEmail" type="email" required :readonly="submittedData" maxlength="100" />
					<p v-if="v$.yourEmail.$error" class="error">Email is required</p>
				</div>
				<div>
					<label for="bugTitle">Title:</label>
					<input id="bugTitle" v-model="form.bugTitle" type="text" required :readonly="submittedData" maxlength="200" />
					<p v-if="v$.bugTitle.$error" class="error">Bug title is required</p>
				</div>
				<div>
					<label for="bugDescription">Bug Description:</label>
					<textarea id="bugDescription" v-model="form.bugDescription" required :readonly="submittedData" maxlength="1000" rows="5"></textarea>
					<p v-if="v$.bugDescription.$error" class="error">Bug description is required</p>
				</div>
				<div>
					<label for="bugSteps">Steps to Reproduce:</label>
					<textarea id="bugSteps" v-model="form.bugSteps" required :readonly="submittedData" maxlength="1000" rows="4"></textarea>
					<p v-if="v$.bugSteps.$error" class="error">Steps to reproduce the bug are required</p>
				</div>
				<div>
					<label for="bugType">Bug Type:</label>
					<select id="bugType" v-model="form.bugType" :disabled="submittedData" required>
						<option disabled value="">Please select a bug type</option>
						<option>UI</option>
						<option>Functionality</option>
						<option>Performance</option>
						<option>Security</option>
						<option>Other</option>
					</select>
					<p v-if="v$.bugType.$error" class="error">Bug type is required</p>
				</div>
				<div class="bug-priority">
					<label>Bug Priority:</label>
					<div class="radio-group">
						<div>
							<input id="low" type="radio" value="Low" v-model="form.bugPriority" :disabled="submittedData" />
							<label for="low" style="color: green">Low</label>
						</div>
						<div>
							<input id="medium" type="radio" value="Medium" v-model="form.bugPriority" :disabled="submittedData" />
							<label for="medium" style="color: yellow">Medium</label>
						</div>
						<div>
							<input id="high" type="radio" value="High" v-model="form.bugPriority" :disabled="submittedData" />
							<label for="high" style="color: red">High</label>
						</div>
					</div>
					<p v-if="v$.bugPriority.$error" class="error">Bug priority is required</p>
				</div>
				<button type="submit" :disabled="submittedData">Submit Bug Report</button>
			</form>
		</div>
		<div v-if="submittedData" class="box-element col-12 col-sm-10 col-md-8 col-lg-7 mx-auto transparent-bg">
			<div class="card-header" style="color: green !important">Bug report successfully submitted</div>
			<div class="card-header">Your submitted data:</div>
			<ul class="list-group list-group-flush">
				<li class="list-group-item transparent-bg" v-for="(value, key) in submittedData" :key="key">
					<strong style="color: gold !important">{{ key }}:</strong>
					<span>{{ value }}</span>
				</li>
			</ul>
			<div class="login-button">
				<button class="btn btn-primary" @click="goToMain">Okay</button>
			</div>
		</div>
	</div>
</template>

<script>
import { reactive, ref, nextTick } from "vue";
import { required } from "@vuelidate/validators";
import { useVuelidate } from "@vuelidate/core";
import { useRouter } from "vue-router";
import axios from "axios";

export default {
	setup() {
		const submittedData = ref(null);
		const form = reactive({
			bugTitle: "",
			bugDescription: "",
			bugSteps: "",
			yourEmail: "",
			bugType: "",
			bugPriority: "",
		});

		const rules = {
			bugTitle: { required },
			bugDescription: { required },
			bugSteps: { required },
			yourEmail: { required },
			bugType: { required },
			bugPriority: { required },
		};

		const v$ = useVuelidate(rules, form);
		const errorMessage = ref(null);

		const router = useRouter();
		function goToMain() {
			router.push({
				path: "/",
			});
		}

		async function submitBug() {
			v$.value.$touch();
			if (v$.value.$error) {
				errorMessage.value = "Please fill out all fields";
				return;
			}

			console.log("Form is valid", form);
			try {
				const dataToSend = {
					email: form.yourEmail,
					bug_title: form.bugTitle,
					bug_description: form.bugDescription,
					bug_steps: form.bugSteps,
					bug_type: form.bugType,
					bug_priority: form.bugPriority,
				};

				const response = await axios.post("http://localhost:8000/api/report_bug/", dataToSend);

				if (response.status === 200 && response.data) {
					console.log("Bug report sent successfully");
					errorMessage.value = null;
					submittedData.value = dataToSend;
					nextTick(() => {
						window.scrollTo(0, document.body.scrollHeight);
					});
				} else {
					throw new Error("Unexpected response from the server");
				}
			} catch (error) {
				console.log(error);
				errorMessage.value = `Error sending bug report: ${error.message}`;
			}
		}

		return { form, v$, submitBug, errorMessage, submittedData, goToMain };
	},
};
</script>

<style scoped>
.container {
	box-sizing: border-box;
	max-width: 100%;
	overflow-x: hidden !important;
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
.radio-group {
	display: flex;
	gap: 10px;
	align-items: center;
	justify-content: center;
}
.list-group-item {
	word-wrap: break-word;
}
</style>

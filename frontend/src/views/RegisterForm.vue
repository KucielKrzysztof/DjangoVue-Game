<template>
	<div class="container">
		<h1 class="scoreboard-title text-center my-4">Register</h1>
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
			<div>
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
<style scoped>
.transparent-bg {
	background-color: transparent !important;
	color: white !important;
	border: none !important;
}
</style>
<script>
import { reactive, nextTick, toRaw, ref } from "vue";
import { required, email } from "@vuelidate/validators";
import { useVuelidate } from "@vuelidate/core";

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
			submittedData.value = toRaw(form);
			// Here you would send the form data to your backend
		}

		return { form, v$, submitForm, submittedData };
	},
};
</script>

import { createRouter, createWebHistory } from "vue-router";
import RegisterForm from "@/views/RegisterForm.vue";
import LoginForm from "@/views/LoginForm.vue";
import ReportBug from "@/views/ReportBug.vue";

const routes = [
	{
		path: "/",
		name: "GameVue",
		component: () => import("@/views/GameVue.vue"),
	},
	{
		path: "/register",
		name: "RegisterForm",
		component: RegisterForm,
	},
	{
		path: "/scoreboard",
		name: "ScoreBoard",
		component: () => import("@/views/ScoreBoard.vue"),
	},
	{
		path: "/login",
		name: "LoginForm",
		component: LoginForm,
	},
	{
		path: "/reportbug",
		name: "ReportBug",
		component: ReportBug,
	},
	//ściezka wildcard, przekierowuje na stronę główną
	{ path: "/:pathMatch(.*)*", redirect: "/" },
];

const router = createRouter({
	history: createWebHistory(process.env.BASE_URL),
	routes,
});
router.beforeEach((to, from, next) => {
	// Sprawdź, czy użytkownik jest zalogowany
	const loggedIn = localStorage.getItem("user");

	// Jeśli użytkownik próbuje uzyskać dostęp do strony logowania lub rejestracji, a jest już zalogowany,
	// przekieruj go na stronę główną
	if ((to.path === "/login" || to.path === "/register") && loggedIn) {
		next("/");
	} else {
		next();
	}
});

export default router;

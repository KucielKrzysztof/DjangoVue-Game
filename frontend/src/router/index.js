import { createRouter, createWebHistory } from "vue-router";
import RegisterForm from "@/views/RegisterForm.vue";

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
];

const router = createRouter({
	history: createWebHistory(process.env.BASE_URL),
	routes,
});

export default router;

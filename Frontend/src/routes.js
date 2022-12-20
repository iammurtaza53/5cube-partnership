import { createWebHistory, createRouter } from "vue-router";

import DashboardComponent from "./components/DashboardComponent.vue";
import CategoryComponent from "./components/CategoryComponent.vue";
import ExpenseComponent from "./components/ExpenseComponent.vue";
import IncomeComponent from "./components/IncomeComponent.vue";
import LogIn from "./components/LogIn.vue";
const routes = [
    {
        name: "dashboard",
        path: "/",
        component:DashboardComponent,
    },
    {
        name: "login",
        path: "/login",
        component:LogIn,
    },
    {
        name: "category",
        path: "/category",
        component:CategoryComponent,
    },
    {
        name: "expense",
        path: "/expense",
        component:ExpenseComponent,
    },
    {
        name: "income",
        path: "/income",
        component:IncomeComponent,
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})
export default router
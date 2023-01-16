import { createWebHistory, createRouter } from "vue-router";

// import DashboardComponent from "./components/DashboardComponent.vue";
import CategoryComponent from "./components/CategoryComponent.vue";
import ExpenseComponent from "./components/ExpenseComponent.vue";
import IncomeComponent from "./components/IncomeComponent.vue";
import LogIn from "./components/LogIn.vue";
import ShareComponent from "./components/ShareComponent.vue";
import ReportComponent from "./components/ReportComponent.vue";
import GroupComponent from "./components/GroupComponent.vue";
import SignUp from "./components/SignUp";
import StatisticsComponent from "./components/StatisticsComponent.vue";

const routes = [
    // {
    //     name: "dashboard",
    //     path: "/dashboard",
    //     component:DashboardComponent,
    // },
    {
        name: "login",
        path: "/signin",
        component: LogIn,
        meta: {
            isRequired: false
        }
    },
    {
        name: "category",
        path: "/category",
        component: CategoryComponent,
        meta: {
            isRequired: true
        }
    },  
    {
        name: "expense",
        path: "/expense",
        component: ExpenseComponent,
        meta: {
            isRequired: true
        }
    },
    {
        name: "income",
        path: "/income",
        component: IncomeComponent,
        meta: {
            isRequired: true
        }
    },
    {
        name: "share",
        path: "/share",
        component: ShareComponent,
        meta: {
            isRequired: true
        }
    },
    {
        name: "report",
        path: "/report",
        component: ReportComponent,
        meta: {
            isRequired: true
        }
    },
    {
        name: "group",
        path: "/group",
        component: GroupComponent,
        meta: {
            isRequired: true
        }
    },
    {
        name:"signup",
        path:"/signup",
        component: SignUp,
        meta: {
            isRequired: false
        }
    },
    {
        name:"statistic",
        path:"/statistic",
        component: StatisticsComponent,
        meta: {
            isRequired: false
        }
    },
    {
        path: '',
        redirect: '/signin'
    }
   
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})
router.beforeEach((to, from, next) => {
    if (to.meta.isRequired) {
        if (localStorage.getItem('token')) {
            next()
        } else {
            next('/')
        }
    } else {
        next()
    }
})
export default router
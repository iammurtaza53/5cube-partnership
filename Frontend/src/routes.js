import { createWebHistory, createRouter } from "vue-router";

import DashboardComponent from "./components/DashboardComponent.vue";
import CategoryComponent from "./components/CategoryComponent.vue";
import ExpenseComponent from "./components/ExpenseComponent.vue";
import IncomeComponent from "./components/IncomeComponent.vue";
import LogIn from "./components/LogIn.vue";
import ShareComponent from "./components/ShareComponent.vue";
import ReportComponent from "./components/ReportComponent.vue";
import GroupComponent from "./components/GroupComponent.vue";
import SignUp from "./components/SignUp";

const routes = [
    {
        name: "dashboard",
        path: "/dashboard",
        component:DashboardComponent,
    },
    {
        name: "Signin",
        path: "/",
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
    },
    {
        name: "share",
        path: "/share",
        component:ShareComponent,
    },
    {
        name: "report",
        path: "/report",
        component:ReportComponent,
    },
    {
        name: "group",
        path: "/group",
        component:GroupComponent,
    },
    {
        name:"SignUp",
        path:"/signup",
        component:SignUp,
    }
   
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})
router.beforeEach((to, from, next) => {

    let isLoggedIn = localStorage.getItem('isLoggedIn')
    if(!isLoggedIn){
        next({path:'/'})
    }
    else{
        next()
    }
     

    // if ( from.matched.some(record => record.meta.requiresAuth) ) {
    
    //   next('/');
    // } else {
    //   next();
    // }
  });
export default router
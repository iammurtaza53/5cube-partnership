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


const routes = [
    {
        name: "dashboard",
        path: "/dashboard",
        // component: DashboardComponent,
        meta: {
            isRequired: true
        }
    },
    {
        name: "Signin",
        path: "/",
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
        name: "SignUp",
        path: "/signup",
        component: SignUp,
        meta: {
            isRequired: false
        }
    }

]

const router = createRouter({
    history: createWebHistory(),
    routes,
})




router.beforeEach((to, from, next) => {
    let isLoggedIn = localStorage.getItem('isLoggedIn')
    let isAuthenticationRequired = to.meta['isRequired']

    if(isAuthenticationRequired)
      if(isLoggedIn){
        next();
      }else {
        next("/");
      }
    
     else{
        next();

     }

    // if (isLoggedIn && isAuthenticationRequired) 
    // {
    //     return next({path:'/dashboard'})
    // } else if (!isLoggedIn && isAuthenticationRequired) {
    //     return next({path:'/'})
    // } else {
    //     next()
    // }

}
);

export default router
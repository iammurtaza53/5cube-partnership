import { createApp } from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import { loadFonts } from './plugins/webfontloader'
import router from './routes'
import VueApexCharts from "vue3-apexcharts";
loadFonts()

createApp(App)
  .use(vuetify).use(router).use(VueApexCharts)
  .mount('#app')

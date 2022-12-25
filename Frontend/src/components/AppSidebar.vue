<template>
  <v-navigation-drawer
    v-model="drawers"
    :rail="rail"
    permanent
    @click="rail = false"
    app
    color="#510f13"
    elevation="4"
  >
    <v-list-item nav class="mt-2">
      <div class="ma-4">
        <v-img aspect-ratio="2.2" src="https://www.5cube.io/wp-content/uploads/2018/10/5CUBE-logo-150x.png"></v-img>
      </div>
      <template v-slot:append>
        <v-btn
          color="white"
          variant="text"
          icon="mdi-chevron-left"
          @click.stop="rail = !rail"
        ></v-btn>
      </template>
    </v-list-item>

    <v-divider color="white" class="divider"></v-divider>
    <div class="routes-list">
      <v-list class="pa-0" v-for="(item, i) in routes" :key="i">
        <v-list-item
          :to="item.path"
          class="routes-list-item"
          :prepend-icon="item.icon"
          :title="item.name"
          :value="item.name"
        ></v-list-item>
      </v-list>
    </div>
  </v-navigation-drawer>
  
</template>

<script>
export default {
  name: "AppSidebar",
  data() {
    
    return {
      drawers: true,

      routes: [
        { path: "/", name: "Expense Management", icon: "mdi-view-dashboard" },
        {
          path: "/category",
          name: "Category",
          icon: "mdi-format-list-bulleted-square",
        },
        { path: "/expense", name: "Expense", icon: "mdi-arrow-left-circle" },
        { path: "/income", name: "Income", icon: "mdi-arrow-right-circle" },
        { path: "/share", name: "Share", icon: "mdi-currency-usd"},
        { path:"/report", name: "Report", icon: "mdi-chart-line-variant"},
      ],
      rail: false,
    };
  },
};
</script>

<style scoped>

.routes-list-item {
  color: #dc8c8c;
  /* #aa1a21rgb(250, 224, 228) */
  /* font-size: 0.6rem; */
  font-weight: 100;
  letter-spacing: 1px;
  text-decoration: none;
  text-underline-offset: none;
}
/* .mycol {
  border: 1px solid red;
  align-items: center;
} */
.routes-list {
  margin-top: 40px;
}
/* .theme--light.v-list-item--active:before,
.theme--light.v-list-item--active:hover:before{
  color:#510f13
} */
.v-list-item--active {
     color: white;
  }
  
</style>
<style>
.divider{
    border-top-width: 2px;
  }
</style>

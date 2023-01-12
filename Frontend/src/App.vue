<template>
  <v-app>
    <v-main>
      <v-container class="main-container">
        <router-view></router-view>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>

export default {
  name: "App",
  components: {
    
  },
  data: () => ({
  }),
  
};
</script>
<style scoped>
.main-container{
  min-width: 100%;
  padding: 0px;
}

</style>

<template>
  
  <v-app-bar app  color="#f7f7f7" elevation-on-scroll elevation="4">
    <v-toolbar-title class="text-uppercase">
      <span class="font-weight-bold text-color">5Cube Expense Management</span>
    </v-toolbar-title>
    <v-spacer></v-spacer>
    <v-btn to="/" class="text-color">
      <span>Exit</span>
      <v-icon>mdi-exit-to-app</v-icon>
    </v-btn>
  </v-app-bar>
</template>
<script>

export default {
  components: {
    },
    data() {
        return {
        }
    },
    methods: {
       
    },
    props: {
    },
}
</script>

<style scoped>
.text-color{
  color: #727272;
  font-size: 18px;
}
</style>

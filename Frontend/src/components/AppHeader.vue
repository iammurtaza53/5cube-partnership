<template>
  
  <v-app-bar app  color="#f7f7f7" elevation-on-scroll elevation="4">
    <v-toolbar-title class="text-uppercase">
      <span class="font-weight-bold text-color">5Cube Expense Management</span>
    </v-toolbar-title>
    <v-spacer></v-spacer>
  <div>
    <v-btn class="text-color" @click="logout()">
      <span>Exit</span>
      <v-icon>mdi-exit-to-app</v-icon>
    </v-btn>
  </div>
  </v-app-bar>
</template>
<script>
export default{
  name:'AppHeader',
  data(){
    return{

    }
  },
  methods:{
    logout()
    
    
    {
      console.log('isLoggedout')
      localStorage.clear();
      this.$router.push({path:'/'})
    }

  }


  

  

}
</script>

<style scoped>
.text-color{
  color: #727272;
  font-size: 18px;
}
</style>

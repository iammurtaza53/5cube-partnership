<template>
  <v-container class="container mt-12">
    <v-sheet class="pb-12 login-sheet" elevation="4" shaped>
      <v-row align="center" justify="center">
        <v-col cols="12" sm="4" class="loginfield ma-12 pa-5">
          <v-img src="../assets/5CUBE-logo.png" ></v-img>
        </v-col>
      </v-row>
      <v-form>
      <v-row align="center" justify="center">
        <v-col cols="12" sm="10">
          <v-text-field
            prepend-inner-icon="mdi-email"
            label="Email"
            hint="Enter your Email to access this website"
          ></v-text-field>
        </v-col>
      </v-row>
      <v-row align="center" justify="center">
        <v-col cols="12" sm="10">
          <v-text-field
            prepend-inner-icon="mdi-lock"
            label="Password"
            hint="Enter your password to access this website"
          ></v-text-field>
        </v-col>
      </v-row>
      <v-row align="center" justify="center">
        <v-col justify="center" cols="12" sm="10">
          <v-btn class="Loginbtn" prepend-icon="mdi-vuetify" color="error"
            >Login</v-btn
          >
        </v-col>
      </v-row>
    </v-form>
    </v-sheet>
  </v-container>
</template>
<script></script>


<style scoped>

.container {
    width: 38%;
  /* border : 1px solid green; */
}
.login-sheet{
    border:1px solid #afafaf
}
.loginfield {
  border: 1px solid #c62d2d;
  border-top-left-radius: 20px; 
  border-bottom-right-radius: 20px; 
}
.Loginbtn {
  width: 345px !important;
}
</style>

<template>
  <v-container class="container mt-12">
    <v-sheet class="pb-12 login-sheet" elevation="4">
      <v-row align="center" justify="center">
        <v-col cols="12" sm="4" class="loginfield ma-12 pa-5">
          <v-img src="../assets/5CUBE-logo.png" ></v-img>
        </v-col>
      </v-row>
      <v-form>
      <v-row align="center" justify="center">
        <v-col cols="12" sm="10">
          <v-text-field
            v-model="email"
            :rule="emailRule"
            label="Email"
            required
            prepend-inner-icon="mdi-email"
            hint="Enter your Email to access this website"
          ></v-text-field>
        </v-col>
      </v-row>
      <v-row align="center" justify="center">
        <v-col cols="12" sm="10">
          <v-text-field
            v-model= "password"
            :rules="passwordRule"
            label="Password"
            required
            prepend-inner-icon="mdi-lock"
            hint="Enter your password to access this website"
          ></v-text-field>
        </v-col>
      </v-row>
      <v-row align="center" justify="center">
        <v-col justify="center" cols="12" sm="10">
          <v-btn class="Loginbtn" prepend-icon="mdi-vuetify" color="error" @click="submit()"
            >Login</v-btn
          >
        </v-col>
      </v-row>
    </v-form>
    </v-sheet>
  </v-container>
</template>
<script>
export default{
  name:"LoginComponent",
  data(){
    return{
     email:"",
     emailRule:[
     (v) => !!v || "email is required",
     (v) => /.+@.+/.test(v) || "e-mail must be valid",
     ],
     password:"",
     passworRule:[
       (v) => !!v || "password is required",
     ],
    };
  },
  methods:{
    submit(){
      if(this.email !=="" && this.password !==""){
      this.$router.push({path:"/"})
    }

  }

},
}
</script>


<style scoped>

.container {
    width: 34%;
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

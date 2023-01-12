<template>
  <v-container class="container mt-12">
    <v-sheet class="pb-12 login-sheet" elevation="4">
      <v-row align="center" justify="center">
        <v-col cols="12" sm="4" class="loginfield ma-12 pa-5">
          <v-img src="../assets/5CUBE-logo.png" ></v-img>
        </v-col>
      </v-row>
      <v-form v-model="isvalid">
      <v-row align="center" justify="center">
        <v-col cols="12" sm="10">
          <v-text-field
            v-model="email"
            :rules="emailRules"
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
            :rules="passwordRules"
            label="Password"
            type="password"
            prepend-inner-icon="mdi-lock"
            required
            hint="Enter your password to access this website"
          ></v-text-field>
        </v-col>
      </v-row>
      <v-row align="center" justify="center">
        <v-col justify="center" cols="12" sm="10">
          <v-btn class="Loginbtn" prepend-icon="mdi-vuetify" color="error"
          :disabled="!isvalid"
           @click="submit()"
            >Sign in</v-btn
          >
          <div class="signup mt-2" align="center" justify="center">
            <h6>if you are not a memeber? sign up</h6>
          <v-btn to="/signup"
          color="white"
          flat>
          <span>sign up</span>

          </v-btn>
          </div>
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
      isvalid:false,
     email:"",
     emailRules:[
     (v) => !!v || "email is required",
     (v) => /.+@.+/.test(v) || "e-mail must be valid",
     ],
     password:"",
     passwordRules:[
       (v) => !!v || "password is required",
       v=> v.length <=10 || "password is required 10 length"

     ],
    };
  },
  methods:{
    submit(){
      if(this.email == "fariha@gmail.com" && this.password == "test123"){
           
      this.$router.push({path:"/dashboard"})
      }
     
    

    }

  }

};

</script>


<style>

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

<template>
  <v-container class="container mt-6">
    <v-sheet class="pb-12 signupsheet" elevation="4">
      <v-row align="center" justify="center">
        <v-col sm="4" class="signupfield ma-10 pa-4">
          <v-img src="../assets/5CUBE-logo.png"></v-img>
        </v-col>
      </v-row>

      <v-form v-model="isformvalid">
        <v-row class="mx-4" align="center" justify="center">
          <v-col cols="12" sm="10">
            <v-text-field
              v-model="fullname"
              :rules="nameRules"
              label="FullName"
              prepend-inner-icon="mdi-account"
              required
            ></v-text-field>

            <v-text-field
              v-model="email"
              :rules="emailRules"
              label="Email"
              prepend-inner-icon="mdi-email"
              required
            >
            </v-text-field>
            <v-text-field
              v-model="password"
              :rules="passwordRules"
              label="Password"
              type="password"
              prepend-inner-icon="mdi-key"
              required
            >
            </v-text-field>

            <v-btn
              class="signupbtn mt-4"
              prepend-icon="mdi-vuetify"
              color="error"
              :disabled="!isformvalid"
              @click="signup()"
              >Sign up</v-btn
            >

            <div class="singinbtn mt-3" align="center" justify="center">
              <h6>if you are already member?</h6>
              <v-btn to="/" color="white" flat>
                <span>sign in</span>
              </v-btn>
            </div>
          </v-col>
        </v-row>
      </v-form>
    </v-sheet>
  </v-container>
</template>
<script>
export default {
  // mounted() {
  //   if (localStorage.fullname) {
  //     this.name=localStorage.name;
  //   }
  //   if (localStorage.email) {
  //     this.email=localStorage.email;
  //   }
  //   if (localStorage.password) {
  //     this.password = localStorage.password;
  //   }
  // },
  data() {
    return {
      isformvalid: false,
      fullname: "",
      nameRules: [
        (v) => !!v || "Name is required",
        (v) => v.length <= 15 || "Name must be less than 15 characters",
      ],
      email: "",
      emailRules: [
        (v) => !!v || "E-mail is required",
        (v) => /.+@.+/.test(v) || "E-mail must be valid",
      ],
      password: "",
      passwordRules: [
        (v) => !!v || "password is required",
        (v) => v.length <= 10 || "password length must be less than 10",
      ],
    };
  },
  methods: {
    signup() {
      {
       localStorage.setItem("token", localStorage.name=this.fullname, localStorage.email=this.email, localStorage.password=this.password);
        this.$router.push("/signin");
      }
    },
  },
};
</script>
<style>
.container {
  width: 34%;
}
.signupbtn {
  width: 400px;
}
.signupfield {
  border: 1px solid rgb(199, 47, 47);
  border-top-left-radius: 20px;
  border-bottom-right-radius: 20px;
}
.sidecont {
  background-color: brown;
}

.signupsheet {
  border: 1px solid rgb(201, 197, 197);
}
</style>
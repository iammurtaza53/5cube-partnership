<template>
 <v-container class="container mt-12">
    <v-sheet class="pb-12 signupsheet" elevation="4">
        <v-row align="center" justify="center">
            <v-col cols="12" sm="4" class="signupfield ma-12 pa-5">
                <v-img src= "../assets/5CUBE-logo.png" ></v-img>

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
        </v-form>
     
    </v-sheet>
 </v-container>
</template>
<script>
export default {
    
}
</script>
<style>
.container{
    width:40%
}
</style>
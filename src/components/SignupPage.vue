<template>
  <v-img
  src="../assets/signup.jpg"
  height="100vh"
  gradient="to bottom right, rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)"
>
      <v-container fluid fill-height>
        <v-layout align-center justify-center>
          <v-flex xs12 sm8 md4>
            <v-card class="elevation-24">
              <v-toolbar color="warning lighten-1">
                <v-toolbar-title>Sign Up </v-toolbar-title>
                <v-spacer></v-spacer>                
              </v-toolbar>
              <v-card-text>
                <v-form>
                  <v-text-field v-model="email" id="email" prepend-icon="mdi-email" name="email" label="Email" type="text"></v-text-field>
                  <v-text-field v-model="username" prepend-icon="mdi-account" name="username" label="Username" type="text"></v-text-field>
                  <v-text-field v-model="password" id="password" prepend-icon="mdi-lock" name="password" label="Password" type="password"></v-text-field>
                </v-form>
                <span class="text-center">Already have an account</span>
                <v-btn text color="warning lighten-1" @click="$router.push('/login')">Sign In</v-btn>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="warning lighten-1" @click="submit" >Sign Up</v-btn>
              </v-card-actions>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </v-img>

</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      username: "",
      email: "",
      password: "",
      emailRules: [
        (v) => !!v || "Email is required",
        (v) => /.+@.+\..+/.test(v) || "Email must be valid",
      ],
      passwordRules: [
        (v) => !!v || "Password is required",
        (v) => (v && v.length >= 8) || "Password must be at least 8 characters",
      ],
    };
  },
  methods: {
    async submit(){
      let result= axios.post("https://642d575cbf8cbecdb40381dc.mockapi.io/Users",{
        Name: this.username,
        Email: this.email,
        Password: this.password
      })
      // console.log(result);
      if(result){
        console.log("Sign up successful")
        this.$router.push('/login')
      }
      else{
        alert("Signup Failed")
      }
    }
  },
};
</script>

<style></style>

<template>
  <!-- <v-img
    src="../assets/login.jpg"
    height="100vh"
    gradient="to bottom right, rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)"
  > -->
    <v-container fluid fill-height>
      <v-layout align-center justify-center>
        <v-flex xs12 sm8 md4>
          <v-card class="elevation-24">
            <v-toolbar color="warning lighten-1">
              <v-toolbar-title>Login</v-toolbar-title>
              <v-spacer></v-spacer>
            </v-toolbar>
            <v-card-text>
              <v-form>
                <v-text-field
                  v-model="username"
                  id="username"
                  prepend-icon="mdi-account"
                  name="username"
                  label="Username"
                  type="text"
                  class="zoomable-text-field"

                ></v-text-field>
                <v-text-field
                  v-model="password"
                  id="password"
                  prepend-icon="mdi-lock"
                  name="password"
                  label="Password"
                  type="password"
                  class="zoomable-text-field"

                ></v-text-field>
              </v-form>
              <span class="text-center">Don't have an account</span>
              <v-btn
                text
                color="warning lighten-1"
                @click="$router.push('/signup')"
                >Sign Up</v-btn
              >
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="warning lighten-1" @click="login">Login</v-btn>
            </v-card-actions>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  <!-- </v-img> -->

  <!-- <v-app >
    <v-main  >
      <v-container fluid fill-height >
        <v-layout align-center justify-center>
          <v-flex xs12 sm8 md4>
            <v-card class="elevation-24" >
              <v-toolbar color="primary">
                <v-toolbar-title>Login</v-toolbar-title>
                <v-spacer></v-spacer>                
              </v-toolbar>
              <v-card-text>
                <v-form>
                  <v-text-field v-model="username" id="username" prepend-icon="mdi-account" name="username" label="Username" type="text"></v-text-field>
                  <v-text-field v-model="password" id="password" prepend-icon="mdi-lock" name="password" label="Password" type="password"></v-text-field>
                </v-form>
                <span class="text-center">Don't have an account</span>
                <v-btn text color="primary" @click="$router.push('/signup')">Sign Up</v-btn>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="primary" @click="login">Login</v-btn>
              </v-card-actions>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </v-main>
  </v-app> -->
</template>

<script>
import axios from "axios";

export default {
  data: () => ({
    username: "",
    password: "",
    valid: false,
  }),
  methods: {
    // login(){
    //   console.log(this.username)
    //   console.log(this.password)
    // },
    async login() {
      let result = await axios.get(
        `https://649488730da866a95367ef70.mockapi.io/Users?Name=${this.username}&Password=${this.password}`
      );

      // console.log(this.username, this.password)
      if (result.data.length < 1) alert("Invalid username or password");
      else {
        if (
          result.data[0].Name == this.username &&
          result.data[0].Password == this.password
        ) {
          localStorage.setItem("user", JSON.stringify(result.data[0]));
          this.$router.push("/IndexPage");
        } else {
          alert("Invalid username or password");
        }
      }
    },
  },
};
</script>
<style>
img {
  background-image: url("../assets/login.jpg");
  background-repeat: no-repeat;
  background-size: cover;
}
.zoomable-text-field {
  transition: transform 0.3s ease;
}

.zoomable-text-field:hover {
  transform: scale(1.05); /* Adjust the zoom level as desired */
}
</style>

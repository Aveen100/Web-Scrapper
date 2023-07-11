<template>
  <nav>
    <!-- **************ToolBar Start ***************** -->

    <v-app-bar flat app fixed class="grey darken-4">
      <v-app-bar-nav-icon v-on:click="drawer = !drawer" color="yellow"></v-app-bar-nav-icon>
      <v-toolbar-title>
        <span class="yellow--text">Web</span>
        <span class="font-weight-light white--text"  >Scrapper</span>
        <!-- <span>{{pic}}</span> -->
      </v-toolbar-title>
      <v-spacer></v-spacer>

      <v-btn icon class="hidden-sm-and-down">
        <v-icon color="red">mdi-heart</v-icon>
      </v-btn>

      <v-btn icon @click="logout">
        <v-icon color="white">mdi-logout</v-icon>
      </v-btn>
    </v-app-bar>
    <!-- **************ToolBar Ends ***************** -->

    <!-- **************Navigation drawer Start ***************** -->

    <v-navigation-drawer class="warning lighten-1" app v-model="drawer">
      <p class="text-center mt-4 headline">Side Bar</p>

      <v-divider></v-divider>
      <v-list dense>
        <v-list-item-group>
          <v-list-item to="/IndexPage">
            <v-list-item-icon>
              <v-icon>mdi-home</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title>Home</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
          <v-list-item to="/home">
            <v-list-item-icon>
              <v-icon>mdi-target</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title>Scrapper's Page</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
          <v-list-item to="/about">
            <v-list-item-icon>
              <v-icon>mdi-help</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title>About</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
        <!-- <v-divider></v-divider> -->
      </v-list>

      <template v-slot:append>
        <div class="pa-2">
          <v-btn block class="grey lighten-2" @click="logout"> Logout </v-btn>
        </div>
      </template>
    </v-navigation-drawer>

    <!-- **************Navigation drawer End ***************** -->
  </nav>
</template>

<script>
export default {
  components: {},
  data() {
    return {
      drawer: false,
    };
  },
  methods: {
    logout() {
      localStorage.removeItem("user");
      this.$router.push("/");
    },
  },
};
</script>

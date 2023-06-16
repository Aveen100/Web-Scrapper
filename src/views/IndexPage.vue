<template>
    <div>
      <div>
      <Navbar />
  
      <!-- ***********  Hero Image Start **********  -->
  
      <v-parallax src="../assets/hero.jpg" max-height="auto">
        <v-row align="center" justify="center">
          <v-col class="text-left" cols="8">
            <h1 class="text-h4 font-weight-thin mb-4 my-12">Web Scrapper</h1>
            <h4 class="title my-12">Scrapper the Website Today today!</h4>
            <v-chip large class="subtitle-1 warning" to="/home">
              Scrap Now</v-chip
            >
          </v-col>
        </v-row>
      </v-parallax>
  
      <!-- ***********  Hero Image End **********  -->
  
      <!-- ***********  Services Start **********  -->
  
      <v-container fluid class="grey lighten-2 pa-16">
        <v-row align="center" justify="center">
          <h1 class="warning--text">Why Us?</h1>
        </v-row>
        <v-layout row>
          <v-hover v-slot="{ hover }" open-delay="50">
            <v-card
              :elevation="hover ? 16 : 2"
              :class="{ 'on-hover': hover }"
              class="elevation-15 mx-auto my-12"
            >
              <v-layout>
                <v-icon right size="100px" color="warning lighten-1"
                  >mdi-dump-truck</v-icon
                >
                <v-layout column class="pa-10">
                  <h3 class="warning--text">Free Shipping</h3>
                  <p class="grey--text">When Order over $100</p>
                </v-layout>
              </v-layout>
            </v-card>
          </v-hover>
          <v-hover v-slot="{ hover }" open-delay="50">
            <v-card
              :elevation="hover ? 16 : 2"
              :class="{ 'on-hover': hover }"
              class="elevation-15 mx-auto my-12"
            >
              <v-layout>
                <v-icon right size="100px" color="warning lighten-1"
                  >mdi-phone</v-icon
                >
                <v-layout column class="pa-10">
                  <h3 class="warning--text">24/7 Support</h3>
                  <p class="grey--text">Get support all day</p>
                </v-layout>
              </v-layout>
            </v-card>
          </v-hover>
          <v-hover v-slot="{ hover }" open-delay="50">
            <v-card
              :elevation="hover ? 16 : 2"
              :class="{ 'on-hover': hover }"
              class="elevation-15 mx-auto my-12"
            >
              <v-layout>
                <v-icon right size="100px" color="warning lighten-1"
                  >mdi-cash-refund</v-icon
                >
                <v-layout column class="pa-10">
                  <h3 class="warning--text">Refund</h3>
                  <p class="grey--text">Get refund within 3 days!</p>
                </v-layout>
              </v-layout>
            </v-card>
          </v-hover>
        </v-layout>
      </v-container>
  
      <!-- ***********  Services End **********  -->
  
      <!-- ***********  Our Story **********  -->
      <v-container fluid class="hidden-md-and-down">
        <v-layout>
          <v-row align="center" justify="center">
            <v-col class="text-center" cols="8">
              <h1 class="warning--text mb-4 my-12">Our Story</h1>
            </v-col>
          </v-row>
        </v-layout>
        <v-row >
          <v-col class="col-3"></v-col>
          <v-col class="col-3">
            <p class="subtitle-1 grey--text">
              Lorem Ipsum is simply dummy text of the printing and typesetting
              industry. Lorem Ipsum has been the industry's standard dummy text
              ever since the 1500s, when an unknown printer took a galley of type
              and scrambled it to make a type specimen book. It has survived not
              only five centuries, but also the leap into electronic typesetting,
              remaining essentially unchanged. It was popularised in the 1960s
              with the release of Letraset sheets containing Lorem Ipsum passages,
              and more recently with desktop publishing software like Aldus
              PageMaker including versions of Lorem Ipsum
            </p>
          </v-col>
          <v-divider vertical ></v-divider>
          <v-col class="col-3">
            <p class="subtitle-1 grey--text text-justify">
              Lorem Ipsum is simply dummy text of the printing and typesetting
              industry. Lorem Ipsum has been the industry's standard dummy text
              ever since the 1500s, when an unknown printer took a galley of type
              and scrambled it to make a type specimen book. It has survived not
              only five centuries, but also the leap into electronic typesetting,
              remaining essentially unchanged. It was popularised in the 1960s
              with the release of Letraset sheets containing Lorem Ipsum passages,
              and more recently with desktop publishing software like Aldus
              PageMaker including versions of Lorem Ipsum
            </p>
          </v-col>
        </v-row>
      </v-container>
  
      <!-- ***********  Categories End  /// Our Products **********  -->
  
      <Footer />
    </div>
    <Loader />
  </div>
  </template>
  
  <script>
  import Navbar from "../components/NavBar.vue";
  import Footer from "../components/TheFooter.vue";
  import Loader from "../components/PageLoader.vue";
  export default {
    name: "IndexPage",
    data() {
      return {};
    },
    components: {
      Navbar,
      Footer,
      Loader
    },
    computed: {
    },
    methods: {
    },
    beforeCreate(){
      const value = localStorage.getItem('user');

if (!value) {
  this.$router.push('/login'); // Redirect to login view page
}   
   }
   
  };
  </script>
  
  <style></style>
  
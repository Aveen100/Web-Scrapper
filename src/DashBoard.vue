<template>
  <div>
    <v-container my-5>
      <v-row>
          
          <v-card max-width="200" class="mx-5">
            <v-avatar class="mx-auto" size="80" color="grey">
              <img src="../assets/twitter.png">
            </v-avatar>
            <v-card-title>Twitter </v-card-title>
            <v-text-field label="Enter URL" variant="outlined" max-width="10"></v-text-field>
           
            <v-btn text class="warning elevation-10 mx-auto">Scrap</v-btn>
        </v-card>
          <v-card max-width="200" class="mx-5" >
            <v-avatar class="mx-auto" size="80" color="grey">
              <img src="../assets/wallmart.png">
            </v-avatar>
            <v-card-title>WallMart </v-card-title>
            <v-text-field label="Enter URL" variant="outlined" max-width="10"></v-text-field>
           
            <v-btn class="warning elevation-10 mx-auto" >Scrap</v-btn>
          </v-card>
          <v-card max-width="200" class="mx-5" >
            <v-avatar class="mx-auto" size="80" color="grey">
              <img src="../assets/amazon.png">
            </v-avatar>
            <v-card-title>Amazon </v-card-title>
          <v-text-field label="Enter URL" variant="outlined" max-width="10"></v-text-field>
           
            <v-btn class="warning elevation-10 mx-auto" >Scrap</v-btn>
          </v-card>
          <v-card max-width="200" class="mx-4">
            <v-avatar class="mx-auto" size="80" >
              <img src="../assets/yelp.png" >
            </v-avatar>
            <v-card-title>Yelp </v-card-title>
            <v-text-field label="Enter URL" variant="outlined" max-width="10"></v-text-field>
           
            <v-btn class="warning elevation-10 mx-auto" >Scrap</v-btn>
          </v-card>
        

          
          
        </v-row>
        <v-divider
  :thickness="6"
  class="border-opacity-75 ma-15"
  color="warning"
  inset
></v-divider>
<v-row justify="center">
    <v-col cols="12" md="4">
        <v-card max-width="200" class="mx-4 justify-center align-center">
          
            <v-card-title>Other Links </v-card-title>
            <v-text-field label="Enter URL" variant="outlined" max-width="10"></v-text-field>
           
            <v-btn class="warning elevation-10 mx-auto" >Scrap</v-btn>
          </v-card>
    </v-col>
  </v-row>
        
    </v-container>
  </div>
</template>

<script>
export default {};
//how to scrap data of website using python in vue 2 front end?
</script>

<style>
.mx-auto {
    margin-left: auto;
    margin-right: auto;
    display: flex;
    align-items: center;
  }
 
</style>

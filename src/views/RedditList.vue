<template>
    <div>
      <v-parallax
        src="../assets/amzback.jpeg"
        height="110vh"
        gradient="to bottom right, rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)"
      >
        <NavBar />
        <v-card
          v-if="showcard == true"
          class="mx-auto ma-auto my-5 elevation-20"
          width="400"
        >
          <v-avatar size="50">
            <img src="../assets/reddit.png" />
          </v-avatar>
          <v-card-title>Reddit</v-card-title>
          <v-card-text>
            <v-text-field
            label="Enter URL"
            variant="outlined"
            max-width="10"
            v-model="url"
            :rules="[
              rules1.required,
              (v) =>
                /^https:\/\/www\.reddit\.com\//.test(v) ||
                'Enter Valid Reddit URL',
            ]"
            class="zoomable-text-field"
            ></v-text-field>
  
            <v-text-field
              type="number"
              label="Number of Pages that you want to scrap?"
              variant="outlined"
              max-width="10"
              v-model="pageurl"
              required
              :rules="[rules.required]"
              class="zoomable-text-field"
            ></v-text-field>
          </v-card-text>
          <v-card-actions>
            <v-btn class="warning mx-5 my-5" @click="getProducts(), loadPage()"
              >Scrap List</v-btn
            >
          </v-card-actions>
        </v-card>
        <v-card class="mx-auto ma-auto my-5 elevation-20" style="width: 80%">
          <v-data-table
            v-if="showcard == false"
            :headers="headers"
            :items="laptops"
            class="custom-table"
          >
            <template #item="{ item }">
              <v-list-item two-line>
               
                <v-list-item-content class="mx-3">
                  <v-list-item-title class="mx-3">
                    <span style="font-weight:bold">Post Title : </span>
                    {{ item }}
                  </v-list-item-title>

                </v-list-item-content>
              </v-list-item>
            </template>
          </v-data-table>
        </v-card>
  
        <!-- ****** Download Button *****  -->
        <!-- <v-container class="text-center">
          <v-chip
            v-if="laptops.length != 0"
            @click="downloadCSV()"
            class="warning"
            >Download CSV</v-chip
          >
        </v-container> -->
      </v-parallax>
      <TheFooter />
      <PageLoader v-if="showPageLoader" />
    </div>
  </template>
  
  <script>
  import NavBar from "../components/NavBar";
  import TheFooter from "../components/TheFooter";
  import axios from "axios";
  import cheerio from "cheerio";
//   import XLSX from "xlsx";
  import PageLoader from "../components/PageLoader.vue";
  // import PageLoader from "../components/PageLoader.vue"
  
  export default {
    components: {
      NavBar,
      TheFooter,
      PageLoader,
    },
    computed: {},
    beforeCreate() {
      const value = localStorage.getItem("user");
  
      if (!value) {
        this.$router.push("/"); // Redirect to login view page
      }
    },
  
    data() {
      return {
        headers: [{ text: "Products", value: "image" }],
        showPageLoader: false,
        laptops: [],
        url: "",
        pageurl: "",
        stopload: false,
        rules: {
          required: (value) => !!value || "Page Number is required",
        },
        rules1: {
          required: (value) => !!value || "URL is required",
        },
        showcard: true,
      };
    },
    methods: {
      async getProducts() {
        try {
            const response = await axios.get(this.url);
    const $ = cheerio.load(response.data);
    
    const postTitles = [];
    
    $('h3._eYtD2XCVieq6emjKBH3m').each((index, element) => {
      const postTitle = $(element).text().trim();
      postTitles.push(postTitle);
    });
    
    console.log('Post Titles:');
    this.showcard=false;
    this.laptops= postTitles;

    console.log(this.laptops , "sss");
  } catch (error) {
    console.error(error);
  }
      },


      loadPage() {
        if(this.url && this.pageurl){

        
        this.showPageLoader = true; // Show the PageLoader component
        // Perform any other necessary operations or async requests
  
        const checkStopLoad = () => {
          if (!this.stopload) {
            setTimeout(checkStopLoad, 100); // Check again after 100 milliseconds
          } else {
            this.showPageLoader = false; // Hide the PageLoader component
          }
        };
        checkStopLoad();
    }
        // Start checking the condition
      },
    },
  };
  </script>
  
  <style>
  .custom-table .v-data-table-header th {
    background-color: #ffc107;
    color: black;
  }
  .zoomable-text-field {
    transition: transform 0.3s ease;
  }
  
  .zoomable-text-field:hover {
    transform: scale(1.05); /* Adjust the zoom level as desired */
  }
  </style>
  
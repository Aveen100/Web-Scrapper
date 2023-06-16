<template>
  <div>
    <v-parallax
    src="../assets/yelpback.jpg"
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
        <img src="../assets/yelp.png" />
      </v-avatar>
      <v-card-title>Yelp</v-card-title>
      <v-card-text>
        <v-text-field
          label="Enter URL"
          variant="outlined"
          max-width="10"
          v-model="YelpURL"
          :rules="[
            rules1.required,
            (v) =>
              /^https:\/\/www\.yelp\.com\//.test(v) || 'Enter Valid Yelp URL',
          ]"
        ></v-text-field>
        <v-text-field
          type="number"
          label="Number of Pages that you want to scrap?"
          variant="outlined"
          max-width="10"
          v-model="pageurl"
          required
          :rules="[rules.required]"
        ></v-text-field>
      </v-card-text>
      <v-card-actions>
        <v-btn class="warning mx-5 my-5" @click="YelpData(),loadPage()"
          >Scrap List</v-btn
        >
      </v-card-actions>
    </v-card>

    <!-- ********Data Table Starts********** -->
    <v-card class="mx-auto ma-auto my-5 elevation-20" style="width: 75%">
      <v-data-table
        v-if="showcard == false"
        :headers="headers"
        :items="yelp"
        class="custom-table"
      >
        <template #item="{ item }">
          <v-list-item two-line>
            <v-avatar size="130">
              <img :src="item.image" alt="" />
            </v-avatar>
            <v-list-item-content class="mx-3">
              <v-list-item-title class="mx-3">{{
                item.businessName
              }}</v-list-item-title>
              <v-list-item-subtitle class="mx-3">{{
                item.ratings
              }}</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
        </template>
      </v-data-table>
    </v-card>
    <!-- **************Data Table Ends***********   -->

    <v-container class="text-center">
      <v-chip v-if="yelp.length != 0" @click="downloadCSV" class="warning"
        >Download CSV</v-chip
      >
    </v-container>
</v-parallax>
    <TheFooter />
    <ScrapperLoader v-if="showPageLoader" />
  </div>
</template>

<script>
import NavBar from "../components/NavBar";
import TheFooter from "../components/TheFooter";
import axios from "axios";
import cheerio from "cheerio";
import XLSX from "xlsx";
import ScrapperLoader from "../components/ScrapperLoader.vue";

export default {
  components: {
    NavBar,
    TheFooter,
    ScrapperLoader,
  },
  beforeCreate(){
      const value = localStorage.getItem('user');

if (!value) {
  this.$router.push('/login'); // Redirect to login view page
}   
   },
  data() {
    return {
      showPageLoader: false,
      stopload: false,
      headers: [{ text: "Services", value: "image" }],
      yelp: [],
      YelpURL: "",
      pageurl: "",
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
    async scrapePage(url) {
      const response = await axios.get(url);
      const $ = cheerio.load(response.data);
      const scrapedItems = [];

      $("div").each((index, element) => {
        const businessName = $(element).find("h3.css-1agk4wl").text().trim();
        const ratings = $(element).find("span.css-gutk1c").text().trim();
        const image = $(element).find("img.css-xlzvdl").attr("src");

        if (
          businessName !== "" &&
          ratings.length < 5 &&
          ratings !== "" &&
          !scrapedItems.some((item) => item.businessName === businessName)
        ) {
          scrapedItems.push({
            businessName,
            ratings,
            image,
          });
        }
      });

      return scrapedItems;
    },

    async scrapePaginatedPages(url, maxPages) {
      const scrapedItems = [];

      for (let page = 0; page < maxPages; page++) {
        const pageUrl = `${url}&start=${page * 10}`;
        const items = await this.scrapePage(pageUrl);
        scrapedItems.push(...items);
      }

      return scrapedItems;
    },
  
    async YelpData() {
      try {
        const url = `${this.YelpURL}&start=0`;
        const maxPages = this.pageurl; // Maximum number of pages to scrape
        this.yelp = await this.scrapePaginatedPages(url, maxPages);
        this.showcard = false;

      } catch (error) {
        console.error("Error:", error);
      }
      this.stopload = true;
    },
    convertToCSV(data, filename) {
      const worksheet = XLSX.utils.json_to_sheet(data);
      const workbook = XLSX.utils.book_new();
      XLSX.utils.book_append_sheet(workbook, worksheet, "Sheet1");
      XLSX.writeFile(workbook, `${filename}.xlsx`);
    },

    downloadCSV() {
      const worksheet = XLSX.utils.json_to_sheet(this.yelp, {
        header: [],
        width: [300, 200, 500],
      });
      const filename = "YelpServices.xlsx";
      XLSX.writeFile(
        { SheetNames: ["Products"], Sheets: { Products: worksheet } },
        filename
      );
    },
    loadPage() {
  this.showPageLoader = true; // Show the PageLoader component
  // Perform any other necessary operations or async requests

  const checkStopLoad = () => {
    if (this.showcard) {
      setTimeout(checkStopLoad, 100); // Check again after 100 milliseconds
    } else {
      this.showPageLoader = false; // Hide the PageLoader component
    }
  };

  // Start checking the condition
  checkStopLoad();
}
  },
};
</script>

<style>
.custom-table .v-data-table-header th {
  background-color: #ffc107;
  color: black;
}
</style>

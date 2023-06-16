<template>
  <div>
    <v-parallax
      src="../assets/ebayback.jpg"
      height="110vh"
      gradient="to bottom right, rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)"
    >
      <NavBar />
      <!-- ******************* CARD STARTS ********************** -->

      <v-card
        v-if="showcard == true"
        class="mx-auto ma-auto my-5 elevation-20"
        width="400"
      >
        <v-avatar size="50">
          <img src="../assets/ebay.png" />
        </v-avatar>
        <v-card-title>Ebay</v-card-title>
        <v-card-text>
          <v-text-field
            label="Enter URL"
            variant="outlined"
            max-width="10"
            v-model="url"
            :rules="[
              rules1.required,
              (v) =>
                /^https:\/\/www\.ebay\.com\//.test(v) || 'Enter Valid Ebay URL',
            ]"
          ></v-text-field>
          <v-text-field
            type="number"
            label="Number of Pages that you want to scrap?"
            variant="outlined"
            max-width="10"
            v-model="pageurl"
            required
            :rules="[(v) => !!v || 'This field is required']"
          ></v-text-field>
        </v-card-text>
        <v-card-actions>
          <v-btn class="warning mx-5 my-5" @click="getProducts(), loadPage()"
            >Scrap List</v-btn
          >
        </v-card-actions>
      </v-card>
      <!-- ******************* CARD ENDS ********************** -->
      <!-- ******************* DATA TABLE STARTS ********************** -->
      <v-card class="mx-auto ma-auto my-5 elevation-20" style="width: 75%">
        <v-data-table
          v-if="showcard == false"
          :headers="headers"
          :items="products"
          class="custom-table"
        >
          <template #item="{ item }">
            <v-list-item two-line>
              <v-avatar size="130">
                <img :src="item.image" alt="" />
              </v-avatar>
              <v-list-item-content class="mx-3">
                <v-list-item-title class="mx-3">{{
                  item.title
                }}</v-list-item-title>
                <v-list-item-subtitle class="mx-3">{{
                  item.price
                }}</v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>
          </template>
        </v-data-table>
      </v-card>

      <!-- ******************* DATA TABLE ENDS ********************** -->
      <v-container class="text-center">
        <v-chip v-if="products.length != 0" @click="downloadCSV" class="warning"
          >Download CSV</v-chip
        >
      </v-container>
      </v-parallax>
      
      <TheFooter></TheFooter>
      <PageLoader v-if="showPageLoader" />
  </div>
</template>

<script>
import NavBar from "../components/NavBar";
import TheFooter from "../components/TheFooter";
import axios from "axios";
import cheerio from "cheerio";
import XLSX from "xlsx";
import PageLoader from "../components/PageLoader.vue";

export default {
  data() {
    return {
      headers: [{ text: "Products", value: "image" }],
      showPageLoader: false,
      stopload: false,
      products: [],
      showcard: true,
      rules: {
        required: (value) => !!value || "Page Number is required",
      },
      rules1: {
        required: (value) => !!value || "URL is required",
      },
      url: "",
      pageurl: "",
    };
  },
  components: {
    NavBar,
    TheFooter,
    PageLoader,
  },
  beforeCreate(){
      const value = localStorage.getItem('user');

if (!value) {
  this.$router.push('/login'); // Redirect to login view page
}   
   },
  methods: {
    async getProducts() {
      const baseUrl = this.url;
      const data = [];

      for (let page = 1; page <= this.pageurl; page++) {
        const url = baseUrl + page;

        try {
          const response = await axios.get(url);
          const html = response.data;
          const $ = cheerio.load(html);
          $("div.s-item__wrapper").each((i, element) => {
            const title = $(element).find(".s-item__title").text().trim();
            const price = $(element).find("span.s-item__price").text().trim();
            const image = $(element).find("img").attr("src");
            if (
              title != "" &&
              price != "" &&
              image != null &&
              title != "Shop on eBay"
            )
              this.products.push({ title, price, image });
            this.showcard = false;
          });
          console.log(this.products);
        } catch (error) {
          console.log("Error:", error);
        }
      }

      this.stopload = true;
      return data;
    },

    convertToCSV(data, filename) {
      const worksheet = XLSX.utils.json_to_sheet(data);
      const workbook = XLSX.utils.book_new();
      XLSX.utils.book_append_sheet(workbook, worksheet, "Sheet1");
      XLSX.writeFile(workbook, `${filename}.xlsx`);
    },

    downloadCSV() {
      const worksheet = XLSX.utils.json_to_sheet(this.products, {
        header: [],
        width: [300, 200, 500],
      });
      const filename = "EbayProducts.xlsx";
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
    },
  },
};
</script>
<style>
.custom-table .v-data-table-header th {
  background-color: #ffc107;
  color: black;
}
</style>

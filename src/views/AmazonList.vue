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
          <img src="../assets/amazon.png" />
        </v-avatar>
        <v-card-title>Amazon</v-card-title>
        <v-card-text>
          <v-text-field
          label="Enter URL"
          variant="outlined"
          max-width="10"
          v-model="url"
          :rules="[
            rules1.required,
            (v) =>
              /^https:\/\/www\.amazon\.com\//.test(v) ||
              'Enter Valid Amazon URL',
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
              <v-avatar size="130">
                <img :src="item.image" alt="" />
              </v-avatar>
              <v-list-item-content class="mx-3">
                <v-list-item-title class="mx-3">{{
                  item.title
                }}</v-list-item-title>
                <v-list-item-subtitle class="mx-3">
                  <template>
                    <div class="text-center">
                      <v-rating
                        small
                        readonly
                        color="warning"
                        v-model="item.rating"
                        hover
                        half-increments
                      ></v-rating>
                      <pre>{{ item.rating }}</pre>
                    </div>
                  </template>
                </v-list-item-subtitle>
                <v-list-item-subtitle class="mx-3">
                  <span style="font-weight:bold">Price :</span>
                  {{
                  item.price
                }}</v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>
          </template>
        </v-data-table>
      </v-card>

      <!-- ****** Download Button *****  -->
      <v-container class="text-center">
        <v-chip
          v-if="laptops.length != 0"
          @click="downloadCSV()"
          class="warning"
          >Download CSV</v-chip
        >
      </v-container>
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
import XLSX from "xlsx";
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
      for (let page = 1; page <= this.pageurl; page++) {
        // change the number to the desired number of pages
        const response = await axios.get(this.url + page);
        const html = response.data;
        const $ = cheerio.load(html);
        $("div.s-result-item").each((i, element) => {
          const title = $(element).find("h2").text().trim();
          const pricetovalidate = $(element).find("span.a-price").first().text().trim();
          const match = pricetovalidate.match(/\$([\d,]+\.\d+)/);
          const price = match ? match[1] : null;
          const image = $(element).find("img.s-image").attr("src");
          const ratings = $(element)
            .find("span.a-icon-alt")
            .first()
            .text()
            .trim();
          const ratingMatch = ratings.match(/^[0-9.]+/);
          const rating = ratingMatch ? parseFloat(ratingMatch[0]) : null;
          // const ratingstwo = $(element).find("span.a-size-base s-underline-text").first().text().trim();
          // console.log(checktwo , "reviews")
          const laptop = {
            title,
            price,
            image,
            rating,
          };
          if (title != "" && price != "" && image != null)
            this.laptops.push(laptop);
          console.log(this.laptops);
          this.showcard = false;
        });
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
      const worksheet = XLSX.utils.json_to_sheet(this.laptops, {
        header: [],
        width: [300, 200, 500],
      });
      const filename = "AmazonProducts.xlsx";
      XLSX.writeFile(
        { SheetNames: ["Products"], Sheets: { Products: worksheet } },
        filename
      );
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

<template>
  <div>
    <!-- <v-parallax 
      src="../assets/home.jpg"
      style="height: fit-content;"
    >
    <div class="parallax-image"></div> -->
    <v-img
    src="../assets/login.jpg"
    height="110vh"
    gradient="to bottom right, rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)"
  >
  
      <v-container my-5>
        <v-layout row class="xs12 sm6">
          <!-- *************** AMAZON CARD STARTS ******************* -->
          <v-card class="mx-auto ma-auto my-5 elevation-20">
            <v-avatar size="80">
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
                  (v) => !!v || 'URL is required',
                  (v) =>
                    /^https:\/\/www\.amazon\.com\//.test(v) ||
                    'Enter Valid Amazon URL',
                ]"
              ></v-text-field>
            </v-card-text>
            <v-card-actions>
              <!-- *************** AMAZON DIALOG START ******************* -->
              <v-dialog transition="dialog-bottom-transition" max-width="600">
                <template v-slot:activator="{ on, attrs }">
                  <v-btn
                    color="warning"
                    variant="text"
                    @click="scrapeAmazon"
                    v-bind="attrs"
                    v-on="on"
                    :disabled="!isValidAmazonURL"
                  >
                    Scrap
                  </v-btn>
                  <br />
                  <v-btn class="warning mx-5" to="/AmazonList"
                    >Scrap List</v-btn
                  >
                </template>
                <template v-slot:default="Amazondialog">
                  <PageLoader />

                  <v-card>
                    <v-toolbar color="warning" dark
                      >Amazon Scrapped Data</v-toolbar
                    >
                    <v-card-text>
                      <h2>Product Image:</h2>
                      <v-img :src="Amazonimage" :width="300"></v-img>
                      <h2>Product Title:</h2>
                      <p>{{ AmazonName }}</p>
                      <h2>Product Price:</h2>
                      <div class="text-h5">{{ Amazonprice }}</div>
                    </v-card-text>

                    <v-card-actions class="justify-end">
                      <v-btn text @click="Amazondialog.value = false"
                        >Close</v-btn
                      >
                    </v-card-actions>
                  </v-card>
                </template>
                <!-- *************** AMAZON DIALOG END ******************* -->
              </v-dialog>
            </v-card-actions>
          </v-card>
          <!-- *************** AMAZON CARD ENDS ******************* -->

          <!-- *************** REDDIT CARD STARTS ******************* -->
          <v-card class="mx-auto ma-auto my-5 elevation-20">
            <v-avatar size="80">
              <img src="../assets/reddit.png" />
            </v-avatar>
            <v-card-title>Reddit</v-card-title>
            <v-card-text>
              <v-text-field
                label="Enter URL"
                variant="outlined"
                max-width="10"
                v-model="RedditURL"
                :rules="[
                  (v) => !!v || 'URL is required',
                  (v) =>
                    /^https:\/\/www\.reddit\.com\//.test(v) ||
                    'Enter Valid Reddit URL',
                ]"
              ></v-text-field>
            </v-card-text>
            <v-card-actions>
              <!-- *************** REDDIT DIALOG START ******************* -->
              <v-dialog transition="dialog-bottom-transition" max-width="600">
                <template v-slot:activator="{ on, attrs }">
                  <v-btn
                    color="warning"
                    variant="text"
                    @click="RedditScrape"
                    v-bind="attrs"
                    v-on="on"
                    :disabled="!isValidRedditURL"
                  >
                    Scrap
                  </v-btn>
                </template>
                <template v-slot:default="Redditdialog">
                  <PageLoader />

                  <v-card>
                    <v-toolbar color="warning" dark
                      >Reddit Scrapped Data</v-toolbar
                    >
                    <v-card-text>
                      <h2>Username :</h2>
                      <p>{{ RedditUsername }}</p>
                      <h2>Post Title:</h2>
                      <p>{{ RedditPost }}</p>
                      <h2>Post Image:</h2>
                      <v-img :src="RedditImage" class="my-2"></v-img>
                    </v-card-text>
                    <v-card-actions class="justify-end">
                      <v-btn text @click="Redditdialog.value = false"
                        >Close</v-btn
                      >
                    </v-card-actions>
                  </v-card>
                </template>
                <!-- *************** REDDIT DIALOG END ******************* -->
              </v-dialog>
            </v-card-actions>
          </v-card>
          <!-- *************** REDDIT CARD ENDS ******************* -->
          <PageLoader />

          <!-- *************** EBAY CARD STARTS ******************* -->
          <v-card class="mx-auto ma-auto my-5 elevation-20">
            <v-avatar size="80">
              <img src="../assets/ebay.png" />
            </v-avatar>
            <v-card-title>E-Bay </v-card-title>
            <v-card-text>
              <v-text-field
                label="Enter URL"
                variant="outlined"
                max-width="10"
                v-model="EbayURL"
                :rules="[
                  (v) => !!v || 'URL is required',
                  (v) =>
                    /^https:\/\/www\.ebay\.com\//.test(v) ||
                    'Enter Valid Ebay URL',
                ]"
              ></v-text-field>
            </v-card-text>
            <v-card-actions>
              <!-- *************** REDDIT DIALOG START ******************* -->
              <v-dialog transition="dialog-bottom-transition" max-width="600">
                <template v-slot:activator="{ on, attrs }">
                  <v-btn
                    color="warning"
                    variant="text"
                    @click="EbayScrape"
                    v-bind="attrs"
                    v-on="on"
                    :disabled="!isValidEbayURL"
                  >
                    Scrap
                  </v-btn>
                  <v-btn class="warning mx-5" to="/EbayList">Scrap List</v-btn>
                </template>
                <template v-slot:default="Ebaydialog">
                  <PageLoader />

                  <v-card>
                    <v-toolbar color="warning" dark
                      >EBay Scrapped Data</v-toolbar
                    >
                    <v-card-text>
                      <h2>Product Image:</h2>
                      <v-img :src="EbayImage" :width="300"></v-img>
                      <h2>Product Title:</h2>
                      <p>{{ EbayName }}</p>
                      <h2>Product Price:</h2>
                      <div class="text-h5">{{ EbayPrice }}</div>
                    </v-card-text>
                    <v-card-actions class="justify-end">
                      <v-btn text @click="Ebaydialog.value = false"
                        >Close</v-btn
                      >
                    </v-card-actions>
                  </v-card>
                </template>
                <!-- *************** EBAY DIALOG END ******************* -->
              </v-dialog>
            </v-card-actions>
          </v-card>
          <!-- *************** EBAY CARD ENDS ******************* -->
          <!-- *************** YELP CARD STARTS ******************* -->
          <v-card class="mx-auto ma-auto my-5 elevation-20" width="200">
            <v-avatar size="80" class="mx-auto justify-center">
              <!-- Add 'mx-auto' class to center the image -->
              <img src="../assets/yelp.png" />
            </v-avatar>
            <v-card-title class="text-center" align="center">
              <!-- Add 'text-center' class to center the title -->
              Yelp
            </v-card-title>
            <v-card-actions class="justify-center my-4">
              <!-- Add 'justify-center' class to center the actions -->
              <v-btn color="warning" variant="text" @click="navigateToYelp">
                Scrap List
              </v-btn>
            </v-card-actions>
          </v-card>

          <!-- *************** YELP CARD ENDS ******************* -->
        </v-layout>
        <!-- *************** DIVIDER STARTS ******************* -->
        <v-divider
          :thickness="6"
          class="border-opacity-75 ma-15"
          color="warning"
          inset
        ></v-divider>
        <!-- *************** DIVIDER ENDS ******************* -->
        <!-- *************** OTHER LINKS SECTION STARTS ******************* -->

        <v-card class="mx-auto ma-auto my-5 elevation-20">
          <v-card-title>Other Website's Links</v-card-title>
          <v-card-text>
            <v-text-field
              label="Enter URL"
              variant="outlined"
              max-width="10"
              :rules="[
                (v) => !!v || 'URL is required',
                (v) => /^https:\/\/www\./.test(v) || 'Enter Valid  URL',
              ]"
              v-model="OtherURL"
            ></v-text-field>
          </v-card-text>
          <v-card-actions>
            <!-- *************** OTHER LINKS DIALOG START ******************* -->
            <v-dialog transition="dialog-bottom-transition" max-width="600">
              <template v-slot:activator="{ on, attrs }">
                <v-btn
                  color="warning"
                  variant="text"
                  @click="check"
                  v-bind="attrs"
                  v-on="on"
                  :disabled="!isValidOtherURL"
                >
                  Scrap
                </v-btn>
              </template>
              <template v-slot:default="OtherDialog">
                
                <v-card v-if="!snackbar">
                  <PageLoader />
                  <v-toolbar color="warning" dark
                    >Other Scrapped Data</v-toolbar
                  >
                  <v-card-text>
                    <h2>Title:</h2>
                    <P>{{ scrapedData.OtherTitle }}</P>
                    <h2>Description:</h2>
                    <p>{{ scrapedData.OtherDescription }}</p>
                    <h2>Details:</h2>
                    <p>{{ scrapedData.detail }}</p>
                  </v-card-text>
                  <v-card-actions class="justify-end">
                    <v-btn text @click="OtherDialog.value = false">Close</v-btn>
                  </v-card-actions>
                </v-card>
              </template>
            </v-dialog>
          </v-card-actions>
          <!-- *****list**** -->
          <!-- *************** OTHER LINKS DIALOG END ******************* -->
          <!-- ****** SNAKBAR STARTS ***** -->
          <v-snackbar v-model="snackbar">
            Website does not allow scrapping

            <template v-slot:actions>
              <v-btn color="pink" variant="text" @click="snackbar = false">
                Close
              </v-btn>
            </template>
          </v-snackbar>
          <!-- ****** SNAKBAR ENDS ***** -->
        </v-card>
        <!-- *************** OTHER LINKS SECTION ENDS ******************* -->
      </v-container>
    <!-- </v-parallax> -->
    </v-img>
  </div>
</template>

<script>
import axios from "axios";
import cheerio from "cheerio";
import DOMPurify from "dompurify";
import PageLoader from "../components/PageLoader.vue";

export default {
  components: { PageLoader },
  data() {
    return {
      AmazonName: "",
      Amazonprice: "",
      Amazonimage: "",
      RedditUsername: "",
      RedditPost: "",
      RedditImage: "",
      RedditURL: "",
      EbayName: "",
      EbayPrice: "",
      EbayImage: "",
      EbayURL: "",
      OtherURL: "",
      snackbar: null,
      desc: "",
      data: [],
      url: "",
      YelpURL: "",
      Yelp: [],
      scrapedData: [],
      products: [],
      posts: [],

    };
  },
  computed: {
    sanitizedDescription() {
      return DOMPurify.sanitize(this.description);
    },
    isValidAmazonURL() {
      // Check if all rules are satisfied
      return this.url.startsWith("https://www.amazon.com/");
    },
    isValidRedditURL() {
      // Check if all rules are satisfied
      return this.RedditURL.startsWith("https://www.reddit.com/");
    },
    isValidEbayURL() {
      // Check if all rules are satisfied
      return this.EbayURL.startsWith("https://www.ebay.com/");
    },
    isValidOtherURL() {
      // Check if all rules are satisfied
      return this.OtherURL.startsWith("https://www.");
    },
  },
  mounted(){
    this.fetchPosts();

  },
  methods: {
    // ***** AMAZON SCRAPPER Starts *****
    scrapeAmazon() {
      axios
        .get(this.url)
        .then((response) => {
          const html = response.data;
          const $ = cheerio.load(html);
          this.AmazonName = $("h1").text();
          this.Amazonprice = $("span.a-price").text().substring(0, 6);

          this.Amazonimage = $("img.imageLeft0").attr("src");
          console.log("Price :", this.Amazonprice);
        })
        .catch((error) => console.log("Error:", error));
    },
    // ***** AMAZON SCRAPPER Starts *****

    // ****** REDDIT SCRAPPER *******
    RedditScrape() {
      axios
        .get(this.RedditURL)
        .then((response) => {
          const $ = cheerio.load(response.data);
          // const divId = "post-title-t3_13or2nb";
          this.RedditPost = $('div[slot="title"]').text();

          console.log("title is :", this.RedditPost);

          // this.RedditUsername = $("div.post-title-t3_13rpepm").text();
          this.RedditUsername = $("a.text-neutral-content").text();
          console.log("username is:", this.RedditUsername);

          const imgElement = $("#post-image");
          this.RedditImage = imgElement.attr("src");
          console.log("Image is is:", this.RedditImage);
        })
        .catch((error) => {
          console.error("sadasd", error);
        });
    },


    // ******** EBAY SCRAPPER ******
    EbayScrape() {
      axios
        .get(this.EbayURL)
        .then((response) => {
          const $ = cheerio.load(response.data);
          this.EbayName = $("h1").text().trim();
          this.EbayPrice = $("div.x-price-primary").text();
          console.log(`Title of Ebay : ${this.EbayName}`);
          console.log(`Price of EBay : ${this.EbayPrice}`);
          this.EbayImage = $('meta[property="og:image"]').attr("content");
          console.log(`Image URL: ${this.EbayImage}`);
        })
        .catch((error) => {
          console.error(error);
        });
    },

    // ***********************others ***********
    check() {
      axios
        .get(this.OtherURL)
        .then((response) => {
          const html = response.data;
          const $ = cheerio.load(html);
          const OtherTitle = $("title").text();
          const detail = $("h1,h2, h3").text();
          const OtherDescription = $('meta[name="description"]').attr(
            "content"
          );
          this.scrapedData = { OtherTitle, OtherDescription, detail };
          if (
            this.scrapedData.OtherDescription == "" ||
            this.scrapedData.OtherDescription == undefined ||
            this.scrapedData.detail === "" ||
            this.scrapedData.detail == undefined
          ) {
            console.log("Empty");
            this.OtherDialog = false;
            this.snackbar = true;
          } else {
            console.log("sadasd", this.scrapedData);
            this.snackbar = false;
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },

    navigateToYelp() {
      this.$router.push({ name: "YelpList" });
    },
    async fetchPosts() {
      try {
    const response = await axios.get('https://www.reddit.com/?sr_id=4594335&sr_name=entertainment&domain=www.reddit.com&geoip_country=PK&user_agent=Mozilla%2F5.0%20(iPhone%3B%20CPU%20iPhone%20OS%2013_2_3%20like%20Mac%20OS%20X)%20AppleWebKit%2F605.1.15%20(KHTML%2C%20like%20Gecko)%20Version%2F13.0.3%20Mobile%2F15E148%20Safari%2F604.1&base_url=%2Fr%2Fentertainment%2F&referrer_domain=www.reddit.com&referrer_url=%2F&language=&dnt=false&compact_view=true&adblock=false&session_id=qjaaapljnbmnkmjeji&loid=000000000a1z1yjmsv&loid_created=1682533314000&reddaid=&utm_term=rpl_migration_only&utm_medium=mweb&utm_source=xpromo&utm_name=shredditmweb_xpromo_consolidation_rpl&campaign=shredditmweb_xpromo_consolidation_rpl&channel=xpromo&feature=mweb&keyword=rpl_migration_only&mweb_subreddit_ids=t5_2qh0f&%24og_redirect=https%3A%2F%2Fwww.reddit.com%2Fr%2Fentertainment%2F&%24deeplink_path=%2Fr%2Fentertainment%2F&%24android_deeplink_path=reddit%2Fr%2Fentertainment%2F&mweb_loid=t2_a1z1yjmsv&mweb_loid_created=1682533314000&mweb_user_id36=&mweb_user_name=&utm_content=geo_blocking_popup_xpromo_listing&tags=geo_blocking_popup_xpromo_listing&_branch_match_id=1197584673280091004&utm_campaign=shredditmweb_xpromo_consolidation_rpl&_branch_referrer=H4sIAAAAAAAAA41T24rbMBD9GuvF4MS3JVsQZbv0AmloYHt7E7I9sRXrtpK8afbrO7aTLYFNWyOD5szM0cwcqQvB%2BjeLhYOmESHh1iZS6H7x1jsmGlqUt0WelwQtzRVQ0AFc4EIr3JHGKNzSw%2BGQnPJro0gLRlhWm0EHd6TbNRk8OMZbzKAb8yyk5FH2oUyWcZStxLYzGqL8XXy%2F%2FRbPVvzlIU5zlrE8lqKHeMPrEfoZZbfxnbUSfkC1FgFJbpZlkiZpOTKtP33dfI6y%2BznnI9S9GRO%2Bg%2FPCaAxO82SZ5PHGVELCaJfv02IVP%2FAdd2IiK5KUVNwDG5ykiDj8LzpGmzjYgXPY0evdv7hPHKTBtndceiDotrwO7EnAgQY3AOFNJU3dn%2Fwe%2FFjqOPfHPefcyr2ulO7VHvaCSIP48vzx9Dk97pV%2FmnBWO%2BABGprerLIyz%2FO0wBgyBMWwekWdlUyJ1vEw8hstj5NPQSMGRdUBqsn2ZnA10F%2FWGWUmZBLdd3N%2FYxybnSiv9kaKZmZEflJz7E60%2Bn%2FDO641yPNhO6x%2FcDDX0sPxYFzzWtkTqR%2Bq%2BQgclaehZNljt9yRKCtMy9AjHNSBduPVjvI7FAHXpUzXxEWKBsCOT4BZHrqrtwADuW7cOPvLhPmMa2lT%2BZOSIWN%2FNHyB%2FyIkjjCMTwifF5tujdAts8YO9jxkKXxAkATe%2Bn%2BH%2FQYoaB87%2BgMAAA%3D%3D');
    const $ = cheerio.load(response.data);
    
    const postTitles = [];
    
    $('h3._eYtD2XCVieq6emjKBH3m').each((index, element) => {
      const postTitle = $(element).text().trim();
      postTitles.push(postTitle);
    });
    
    console.log('Post Titles:');
    console.log(postTitles);
  } catch (error) {
    console.error(error);
  }
  
    }
    
  },
};
</script>

<style>
@media (max-width: 500px) {
  .parallax-image {
    display: none;
  }
}
</style>

<template>
  <div>
    <NavBar />
    <NewDashBoard />
    <TheFooter></TheFooter>
    <PageLoader />
  </div>
</template>
<!--  -->
<script>
import NavBar from "../components/NavBar";
import TheFooter from "../components/TheFooter";
import NewDashBoard from "../components/NewDashboard.vue";
import PageLoader from "../components/PageLoader.vue"
export default {
  name: "MainPage",

  components: {
    NavBar,
    TheFooter,
    NewDashBoard,
    PageLoader,
  },
  beforeCreate(){
      const value = localStorage.getItem('user');

if (!value) {
  this.$router.push('/'); // Redirect to login view page
}   
   },
 

};
</script>


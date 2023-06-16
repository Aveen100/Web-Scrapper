<template>
  <div class="text-center">
      <v-overlay
    :opacity="1"
    :value="overlay"
  >

<v-progress-circular
    :rotate="180"
    :size="250"
    :width="10"
    color="warning"
    indeterminate
  >
    Loading ...
  </v-progress-circular>
  </v-overlay>
</div>
</template>

<script>
export default {
name: 'PageLoader',
data(){
  return{
      overlay:true 
  }
},  

methods: {
load(){
setTimeout(() => {
              this.overlay = false;
          }, 13500);
        }
},
mounted(){
this.load();
        },
}
</script>

<style>

</style>

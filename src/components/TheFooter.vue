<template>
  <v-footer class="d-flex flex-column warning" id="footer">
    <div class="bg-teal d-flex w-100 align-center px-4">
      <strong>Get connected with us on social networks!</strong>

      <v-spacer></v-spacer>
    </div>
    <v-btn icon>
      <v-icon>mdi-facebook</v-icon>
      <v-icon>mdi-instagram</v-icon>
      <v-icon>mdi-linkedin</v-icon>
    </v-btn>

    <div class="px-4 py-2 bg-black text-center w-100">
      {{ new Date().getFullYear() }} — <strong>Vuetify</strong>
    </div>
  </v-footer>
</template>
<script>
export default {};
</script>

<style scopped>

</style>

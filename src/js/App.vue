<template>
  <div id="app">

    <ul>
      <li v-for="contact in contacts">
        {{contact.name}}
      </li>
    </ul>

  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "app",
  data() {
    return {
      msg: "Initial vue setup",
      contacts: [],
      errors: []
    };
  },
  created() {
    axios
      .get(this.vue_data.contact_list_url)
      .then(response => {
        console.log("response", response);
        this.contacts = response.data;
      })
      .catch(e => {
        console.log("errors", e);
        this.errors.push(e);
      });
  }
};
</script>

<style lang="scss">
h1,
h2 {
  font-weight: normal;
  color: purple;
}
</style>

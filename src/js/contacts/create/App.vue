<template>
  <div>
    <h1>Add New Contact</h1>
    <div>{{msg}}</div>
    <form v-on:submit.prevent="addContact">
      <div class="form-group">
        <label for="name">Name</label>
        <input type="text" class="form-control" v-model="contact.name" id="name">
      </div>
      <div class="form-group">
        <label for="address">Address</label>
        <input type="text" class="form-control" id="address" placeholder="1234 Main St">
      </div>
      <div class="form-row">
        <div class="form-group col-md-6">
          <label for="city">City</label>
          <input type="text" class="form-control" id="city">
        </div>
        <div class="form-group col-md-4">
          <label for="state">State</label>
          <input type="text" class="form-control" id="state">
        </div>
        <div class="form-group col-md-2">
          <label for="zip_code">Zip</label>
          <input type="text" class="form-control" id="zip_code">
        </div>
      </div>
    </form>
  </div>
</template>

<script>
import axios from "axios";

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";

export default {
  data() {
    return {
      msg: "Initial create setup",
      contact: {},
      errors: []
    };
  },
  methods: {
    addContact() {
      axios
        .post(this.initial_data.contact_list_url, this.contact)
        .then(response => {
          console.log("response", response);
          console.log("data", response.data);
          console.log("url", response.data.url);
        })
        .catch(e => {
          console.log("errors", e);
          this.errors.push(e);
        });
    }
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

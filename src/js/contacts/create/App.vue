<template>
  <div>
    <h1>Add New Contact</h1>
    <h2>Available Tags</h2>
    <ul>
      <li v-for="(tagOption, index) in tagOptions" :key="index">{{ tagOption.name }}</li>
    </ul>
    <form v-on:submit.prevent="addContact">
      <div class="form-group">
        <label for="name">Name</label>
        <input type="text" class="form-control" v-model="contact.name" id="name">
      </div>
      <div class="form-group">
        <label for="address">Address</label>
        <input type="text" class="form-control" v-model="address.address" id="address" placeholder="1234 Main St">
      </div>
      <div class="form-row">
        <div class="form-group col-md-6">
          <label for="city">City</label>
          <input type="text" class="form-control" v-model="address.city" id="city">
        </div>
        <div class="form-group col-md-4">
          <label for="state">State</label>
          <input type="text" class="form-control" v-model="address.state" id="state">
        </div>
        <div class="form-group col-md-2">
          <label for="zip_code">Zip</label>
          <input type="text" class="form-control" v-model="address.zip_code" id="zip_code">
        </div>
      </div>
      <div class="form-group">
        <label for="name">Email</label>
        <input type="text" class="form-control" v-model="email.email" id="name">
      </div>
      <div class="form-row">
        <div class="form-group col-md-6">
          <label for="city">Phone</label>
          <input type="text" class="form-control" v-model="phone.number" id="city">
        </div>
        <div class="form-group col-md-4">
          <label for="state">Type</label>
          <input type="text" class="form-control" v-model="phone.type" id="state">
        </div>
      </div>
      <div class="form-group">
        <div v-for="(tagOption, index) in tagOptions" :key="index">
          <input type="checkbox" :id="tagOption.name" :value="tagOption.name" v-model="tags">
          <label :for="tagOption.name">{{ tagOption.name }}</label>
        </div>
        
        <br>
        <span>Tags: {{ tags }}</span>
      </div>
      <button
            class="btn btn-primary"
            @click.prevent="addContact">Add Contact
        </button>
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
      address: {},
      phone: {},
      email: {},
      tagOptions: [],
      tags: [],
      errors: []
    };
  },
  created() {
    this.getTags();
  },
  methods: {
    addContact() {
      this.contact.addresses = [this.address];
      this.contact.emails = [this.email];
      this.contact.phones = [this.phone];
      this.contact.tags = this.tags;
      console.log("contact: ", this.contact);
      axios
        .post(this.initialData.contactListUrl, this.contact)
        .then(response => {
          console.log("response", response);
          console.log("data", response.data);
          console.log("url", response.data.url);
        })
        .catch(e => {
          console.log("errors", e);
          this.errors.push(e);
        });
    },
    getTags() {
      axios
        .get(this.initialData.tagListUrl)
        .then(response => {
          console.log("response", response);
          this.tagOptions = response.data;
        })
        .catch(e => {
          console.log("errors", e);
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

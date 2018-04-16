<template>
    <div>
      <h2>Available Tags</h2>
        <ul>
          <li v-for="(tagOption, index) in tagOptions" :key="index">{{ tagOption.name }}</li>
        </ul>
        <form v-on:submit.prevent="updateContact">
          <p v-if="errors.length">
            <b>Please correct the following error(s):</b>
            <ul>
              <li v-for="(error, index) in errors" :key="index">{{ error }}</li>
            </ul>
          </p>
          <div class="form-group">
            <label for="name">Name</label>
            <input type="text" class="form-control" v-model="contact.name" id="name">
          </div>
          <div class="form-group">
            <label for="address">Address</label>
            <input type="text" class="form-control" v-model="address.address" id="address">
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
          </div>
          <button class="btn btn-primary" @click="updateContact">Update</button>
          <button class="btn btn-danger" @click="cancelUpdate">Cancel</button>
        </form>
    </div>
</template>
<script>
import axios from "axios";
import _ from "lodash";

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";

export default {
  data() {
    return {
      id: this.$route.params.id,
      contact: {},
      errors: [],
      tagOptions: [],
      address: {},
      phone: {},
      email: {},
      tags: []
    };
  },
  watch: {
    '$route'(to, from) {
      this.id = this.$route.params.id;
      this.getContactDetails();
    }
  },
  methods: {
    getContactDetails() {
      axios
        .get("/contacts/contacts/" + this.id)
        .then(response => {
          this.contact = response.data;
          this.address = _.isEmpty(this.contact.addresses) ? {} : this.contact.addresses[0];
          this.email = _.isEmpty(this.contact.emails) ? {} : this.contact.emails[0];
          this.phone = _.isEmpty(this.contact.phones) ? {} : this.contact.phones[0];
          this.tags = this.contact.tags;
        })
        .catch(e => {
          console.log("errors", e);
          this.errors.push(e);
        });
    },
    validateForm() {
      this.errors = [];
      if (!this.contact.name) this.errors.push("Name required.");
    },
    getTags() {
      axios
        .get('/contacts/tags')
        .then(response => {
          console.log("response", response);
          this.tagOptions = response.data;
        })
        .catch(e => {
          console.log("errors", e);
        });
    },
    navegateToDetail() {
      this.$router.push({ name: 'detail', params: { id: this.id }});
    },
    updateContact() {
      this.contact.addresses = _.isEmpty(this.address) ? [] : [this.address];
      this.contact.emails = _.isEmpty(this.email) ? [] : [this.email];
      this.contact.phones = _.isEmpty(this.phone) ? [] : [this.phone];
      this.contact.tags = this.tags;
      this.validateForm();
      if (this.errors.length) {
        return;
      }
      axios
        .put('/contacts/contacts/' + this.contact.id + '/', this.contact)
        .then(response => {
          console.log("response", response);
          console.log("data", response.data);
          console.log("url", response.data.url);
          console.log("id", response.data.id);
          this.navegateToDetail(response.data.id);
        })
        .catch(e => {
          console.log("errors", e);
          this.errors.push(e);
        });
    },
    cancelUpdate() {
      this.navegateToDetail();
    }
  },
  created() {
    this.getContactDetails();
    this.getTags();
  },
};
</script>
<style>

</style>

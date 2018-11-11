<template>
    <div>
        <h1>Edit Contact</h1>
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
          <!-- <div class="form-row">
            <div class="form-group col-md-6">
              <label for="city">Phone</label>
              <input type="text" class="form-control" v-model="phone.number" id="city">
            </div>
            <div class="form-group col-md-4">
              <label for="state">Type</label>
              <input type="text" class="form-control" v-model="phone.type" id="state">
            </div>
          </div> -->
          <teq-phone 
            v-for="(phone, index) in phones" 
            :key="index" 
            v-bind:phone="phone" 
            v-on:remove="removePhone(index)" >
          </teq-phone>
          <button @click.prevent="addPhone" class="btn__add-element">Add phone</button>
          <div class="form-group">
            <label class="typo__label">Choose tags</label>
              <multiselect
                v-model="tags"
                :options="tagOptions"
                :multiple="true"
                :close-on-select="false"
                :searchable="true"
                placeholder="Choose zero or more"
              ></multiselect>
            </div>
            <br>
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

import Multiselect from 'vue-multiselect'
import teqPhone from './form/Phone.vue'

export default {
  components: {
    Multiselect,
    teqPhone
  },
  data() {
    return {
      id: this.$route.params.id,
      contact: {},
      errors: [],
      tagOptions: [],
      address: {},
      phones: [{}],
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
        .get(this.initialData.Urls.contact_detail(this.id))
        .then(response => {
          this.contact = response.data;
          this.address = _.isEmpty(this.contact.addresses) ? {} : this.contact.addresses[0];
          this.email = _.isEmpty(this.contact.emails) ? {} : this.contact.emails[0];
          this.phones = _.isEmpty(this.contact.phones) ? [{}] : this.contact.phones;
          this.tags = this.contact.tags;
        })
        .catch(e => {
          this.errors.push(e);
        });
    },
    validateForm() {
      this.errors = [];
      if (!this.contact.name) this.errors.push("Name required.");
    },
    getTags() {
      axios
        .get(this.initialData.Urls.tag_list())
        .then(response => {
          this.tagOptions = _.map(response.data, 'name')
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
      this.contact.phones = this.phones;
      this.contact.tags = this.tags;
      this.validateForm();
      if (this.errors.length) {
        return;
      }
      axios
        .put(this.initialData.Urls.contact_detail(this.id), this.contact)
        .then(response => {
          this.navegateToDetail(response.data.id);
        })
        .catch(e => {
          this.errors.push(e);
        });
    },
    cancelUpdate() {
      this.navegateToDetail();
    },
    addPhone() {
      this.phones.push({});
    },
    removePhone(index) {
      this.phones.splice(index, 1);
    }
  },
  created() {
    this.getContactDetails();
    this.getTags();
  },
};
</script>
<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>
<style>

</style>

<template>
  <div>
    <h1>Add New Contact</h1>
    
    <form v-on:submit.prevent="addContact">
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
      <button
            class="btn btn-primary"
            @click.prevent="addContact">Add Contact
      </button>
    </form>
  </div>
</template>

<script>
import axios from "axios";
import _ from "lodash";
import Multiselect from 'vue-multiselect'
import teqPhone from './form/Phone.vue'

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";

export default {
  components: {
    Multiselect,
    teqPhone
  },
  data() {
    return {
      msg: "Initial create setup",
      contact: {},
      address: {},
      phones: [{}],
      email: {},
      tagOptions: [],
      tags: [],
      errors: [],
    };
  },
  created() {
    this.getTags();
  },
  methods: {
    validateForm() {
      this.errors = [];
      if (!this.contact.name) this.errors.push("Name required.");
    },
    addContact() {
      this.contact.addresses = _.isEmpty(this.address) ? [] : [this.address];
      this.contact.emails = _.isEmpty(this.email) ? [] : [this.email];
      this.contact.phones = this.phones;
      this.contact.tags = this.tags;
      this.validateForm();
      if (this.errors.length) {
        return;
      }
      axios
        .post(this.initialData.Urls.contact_list(), this.contact)
        .then(response => {
          this.navegateToDetail(response.data.id);
        })
        .catch(e => {
          console.log("errors", e);
          this.errors.push(e);
        });
    },
    navegateToDetail(id) {
      this.$router.push({ name: 'detail', params: { id: id }});
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
    addPhone() {
      this.phones.push({});
    },
    removePhone(index) {
      this.phones.splice(index, 1);
    }
  }
};
</script>
<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>
<style lang="scss">
  h1,
  h2 {
    font-weight: normal;
    color: purple;
  }

  .btn__add-element {
    color:white;
    background: green;
  }

  .btn__add-element:hover {
    color:green;
    background: white;
    border: solid green 2px;
  }
</style>

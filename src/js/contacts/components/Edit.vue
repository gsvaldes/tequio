<template>
    <div>
        <form action="">
            <div class="form-group">
                <label for="name">Name</label>
                <input id="name" type="text" v-model="contact.name" class="form-control">
            </div>
        </form>
        {{contact.name}}
        <button class="btn btn-danger" @click="updateContact">Update</button>
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
      errors: []
    };
  },
  methods: {
    getContactDetails() {
      axios
        .get("/contacts/contacts/" + this.id)
        .then(response => {
          this.contact = response.data;
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
    navegateToDetail(id) {
      this.$router.push({ name: 'detail', params: { id: id }});
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
        .post('/contacts/contacts/' + this.contact.id + '/', this.contact)
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
  },
  created() {
    this.getContactDetails();
  },
};
</script>
<style>

</style>

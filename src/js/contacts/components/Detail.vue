<template>
    <div>       
        <div class="card bg-transparent contact-details" >
            <div class="card-header bg-transparent">
              <h3 class="card-title">{{contact.name}}</h3>
            </div>
            <div class="card-body">
                <h5 class="card-title">Address</h5>
                <address 
                    v-for="address in contact.addresses" 
                    :key="address.id + '-address'">
                    <div>{{ address.address }}</div>
                    <div>{{ address.city }} {{address.state}} {{address.zip_code}} {{address.country}}</div>      
                </address>
                <hr>
                <h5 class="card-title">Emails</h5>
                <div 
                    v-for="email in contact.emails" 
                    :key="email.id + '-email'">
                    {{ email.email }}
                </div>
                <hr>
                <h5 class="card-title">Phones</h5>
                <div 
                    v-for="phone in contact.phones" 
                    :key="phone.id + '-phone'">
                    {{ phone.number | phone }}
                </div>
                <hr>
                <h5 class="card-title">Tags</h5>
                <span 
                    class="badge badge-info tag" 
                    v-for="tag in contact.tags" 
                    :key="tag.id + '-tag'">
                    {{tag}}
                </span>
            </div>
            <div class="card-footer bg-transparent">
                <router-link
                    :to="{name: 'edit', params: {id: id}}"
                    tag="button"
                    class="btn btn-primary"
                >Edit Contact</router-link>
            </div>
        </div>   
        <div v-for="note in contact.notes" :key="note.id + '-note'">{{ note.note }}</div>     
    </div>
</template>
<script>
import axios from "axios";

export default {
  data() {
    return {
      id: this.$route.params.id,
      contact: {},
      errors: []
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
          console.log('data: ', response.data);
          this.contact = response.data;
        })
        .catch(e => {
          console.log("errors", e);
          this.errors.push(e);
        });
    },
    getNotes() {
      axios
        .get(this.initialData.Urls.contact_notes(this.id))
        .then(response => {
          this.contact = response.data;
        })
        .catch(e => {
          console.log("errors", e);
          this.errors.push(e);
        });
    }
  },
  created() {
    this.getContactDetails();
    this.getNotes();
  }
};
</script>
<style scoped>
.contact-details {
  /* width: 400px; */
  margin: 30px auto;
  border: 1px solid #eee;
  padding: 20px;
  box-shadow: 0 2px 3px #ccc;
}
.tag {
  margin-right: 0.2em;
}
</style>

<template>
    <div>
        
        
        <div class="card bg-transparent contact-details" >
            <div class="card-header bg-transparent">{{contactData.name}}</div>
            <div class="card-body">
                <h5 class="card-title">Address</h5>
                <address v-for="address in contactData.addresses" :key=address.id>
                    <div>{{address.address}} {{address.street}}</div>
                    <div>{{address.city}} {{address.state}} {{address.zip_code}} {{address.country}}</div>      
                </address>
                <hr>
                <h5 class="card-title">Emails</h5>
                <div v-for="email in contactData.emails" :key=email.id>
                    {{email.email}}
                </div>
                <hr>
                <h5 class="card-title">Phones</h5>
                <div v-for="phone in contactData.phones" :key=phone.id>
                    {{phone.number|phone}}
                </div>
                <hr>
                <h5 class="card-title">Tags</h5>
                <span class="badge badge-info tag" v-for="tag in contactData.tags" :key=tag.id>
                    {{tag}}
                </span>
            </div>
            <div class="card-footer bg-transparent">
                <button class="btn btn-primary" @click="updateContact">Edit Contact</button>
            </div>
        </div>
        
    </div>


    
  
</template>
<script>
export default {
  props: ["contactData"],
  methods: {
    updateContact() {
      this.$emit("editContact", true);
    }
  },
  filters: {
    phone: function(value) {
      return value
        .replace(/\D+/g, "")
        .replace(/(\d{3})(\d{3})(\d{4})/, "($1) $2-$3");
    }
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


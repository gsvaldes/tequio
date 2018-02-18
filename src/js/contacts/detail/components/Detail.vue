<template>
    <div>
        
        
        <div class="card bg-light mb-3" style="max-width: 18rem;">
            <div class="card-header">{{contactData.name}}</div>
            <div class="card-body">
                <h5 class="card-title">Addresses</h5>
                <address v-for="(address, i) in contactData.addresses" :key=i>
                    <div>{{address.address}} {{address.street}}</div>
                    <div>{{address.city}} {{address.state}} {{address.zip_code}} {{address.country}}</div>      
                </address>
                <hr>
                <h5 class="card-title">Emails</h5>
                <div v-for="(email, i) in contactData.emails" :key=i>
                    {{email.email}}
                </div>
                <hr>
                <h5 class="card-title">Phones</h5>
                <div v-for="(phone, i) in contactData.phones" :key=i>
                    {{phone.number|phone}}
                </div>
                <hr>
                <h5 class="card-title">Tags</h5>
                <div v-for="(tag, i) in contactData.tags" :key=i>
                    {{tag}}
                </div>
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
<style>

</style>


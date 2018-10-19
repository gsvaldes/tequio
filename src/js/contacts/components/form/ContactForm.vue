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
export default {
    
}
</script>

<style>

</style>


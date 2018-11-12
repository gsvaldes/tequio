<template>
  <div>
    <teq-contact-form :isUpdate="true">
      <h1 slot="form-title">Edit Contact</h1>
    </teq-contact-form>
  </div>
</template>
<script>
import ContactForm from './form/ContactForm.vue'

export default {
  components: {
    teqContactForm: ContactForm
  },
};
</script>
<style>

</style>

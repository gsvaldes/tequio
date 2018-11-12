<template>
  <div>
    <teq-contact-form :isUpdate="false">
      <h1 slot="form-title">Add New Contact</h1>
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

<style lang="scss">

</style>

<template>
    <div>
        <form action="">
            <div class="form-group">
                <label for="name">Name</label>
                <input id="name" type="text" v-model="contactData.name" class="form-control">
            </div>
        </form>
        {{contactData.name}}
        <button class="btn btn-danger" @click="submit">Submit</button>
    </div>
  
</template>
<script>
export default {
  props: ["contactData"],
  data() {
    return {
      done: false
    };
  },
  methods: {
    submit() {
      this.done = true;
      this.$emit("formUpdated", this.done);
    }
  }
};
</script>
<style>

</style>

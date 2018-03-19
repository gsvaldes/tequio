<template>
  <div class="row">
    <div class="col-xs-12 col-md-6 offset-md-3">
      <!-- <button class="btn btn-primary" @click="edit=true" v-show="!edit">Edit Contact</button> -->
      <app-detail 
        :contactData="contactData" 
        v-if="!edit"
        @editContact="edit = $event"
      ></app-detail>
      <app-update 
        :contactData="contactData" 
        v-else
        @formUpdated="edit = !$event"
      ></app-update>
    </div>  
  </div>
</template>
<script>
import Detail from "./components/Detail.vue";
import Update from "./components/Update.vue";

export default {
  components: {
    appDetail: Detail,
    appUpdate: Update
  },
  data() {
    return {
      msg: "Initial detail setup",
      contactData: this.initial_data,
      edit: false
    };
  }
};
</script>
<style>

</style>



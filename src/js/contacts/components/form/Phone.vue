<template>
    <div class="form-row">
        <div class="form-group col-md-6">
          <label for="number">Phone</label>
          <input type="text" class="form-control" v-model="phone.number">
        </div>
        <div class="form-group col-md-4">
          <label for="type">Type</label>
          <input type="text" class="form-control" v-model="phone.type">
        </div>
    </div>
</template>
<script>
export default {
    props: ['phone'] 
}
</script>
<style>

</style>



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
        <div class="form-group col-md-2">
            <button @click.prevent="remove" class="btn__remove">Remove</button>
        </div>
    </div>
</template>
<script>
export default {
    props: ['phone'],
    methods: {
        remove(index){
            this.$emit('remove');
        }
    }
}
</script>
<style scoped>
    .btn__remove {
        color: white;
        background: red;
        height: 2rem;
        margin-top: 2rem;
    }
    .btn__remove:hover {
        color: red;
        background: white;
        border: solid red 2px;
        height: 2rem;
        margin-top: 2rem;
    }
</style>



</style>



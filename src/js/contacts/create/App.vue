<template>
  <div>
    <h1>Add New Contact</h1>
    <div>{{msg}}</div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      msg: "Initial create setup"
    };
  }
};
</script>

<style lang="scss">
h1,
h2 {
  font-weight: normal;
  color: purple;
}
</style>

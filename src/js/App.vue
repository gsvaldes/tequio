<template>
  <div id="app">

    <h1>{{ msg }}</h1>


  </div>
</template>

<script>
export default {
  name: "app",
  data() {
    return {
      msg: "Initial vue setup"
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

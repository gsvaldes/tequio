import Vue from 'vue';

Vue.filter('phone', value => {
    return value
      .replace(/\D+/g, "")
      .replace(/(\d{3})(\d{3})(\d{4})/, "($1) $2-$3");
});

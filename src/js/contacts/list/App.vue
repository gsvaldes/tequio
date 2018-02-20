<template>
  <div>
    <h1>Contact List</h1>
    <v-client-table :columns="columns" :data="contacts" :options="options">
      <div slot="name" slot-scope="props">
        <a :href="'/' + props.row.id">{{props.row.name}}</a>
      </div>
      <div slot="phones" slot-scope="props">
        <div v-for="(phone, index) in props.row.phones" :key="index">
          {{phone.number | phone}}<span class="oi oi-eye"></span>
        </div>
      </div>
      <div slot="tags" slot-scope="props">
        <span v-for="(tag, index) in props.row.tags" :key="index" class="badge badge-secondary">
          {{tag}}
        </span>
      </div>
    </v-client-table>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      msg: "Initial vue setup",
      contacts: [],
      errors: [],
      columns: ["name", "phones", "tags"],
      options: {
        headings: {
          name: "Name",
          phones: "Phone Number(s)",
          tags: "Tags"
        },
        sortable: ["name"],
        filterable: ["name", "tags"]
      }
    };
  },
  created() {
    axios
      .get(this.initial_data.contact_list_url)
      .then(response => {
        console.log("response", response);
        this.contacts = response.data;
      })
      .catch(e => {
        console.log("errors", e);
        this.errors.push(e);
      });
  },
  filters: {
    phone: function(value) {
      return value
        .replace(/\D+/g, "")
        .replace(/(\d{3})(\d{3})(\d{4})/, "($1) $2-$3");
    }
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

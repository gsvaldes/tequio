<template>
  <div>
    <h1>Contact List</h1>
    <v-client-table :columns="columns" :data="contacts" :options="options" id="client-table">
      <div slot="name" slot-scope="props">
        <router-link 
          :to="{ name: 'detail', params: { id: props.row.id}}" 
          class="nav-item"><a>{{props.row.name}}</a>
        </router-link>
      </div>
      <div slot="phones" slot-scope="props">
        <div v-for="(phone, index) in props.row.phones" :key="index">
          {{ phone.number | phone }}<span class="oi oi-eye"></span>
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
      .get(this.initialData.Urls.contact_list())
      .then(response => {
        console.log("response", response);
        this.contacts = response.data;
      })
      .catch(e => {
        console.log("errors", e);
        this.errors.push(e);
      });
  }
};
</script>

<style lang="scss">
h1,
h2 {
  font-weight: normal;
  color: purple;
}
#client-table {
  width: 95%;
  margin: 0 auto;
}
.VueTables__search-field {
  padding-right: 20px;
}
#create-button {
  margin-top: 1.5rem;
}
</style>

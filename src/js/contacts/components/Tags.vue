<template>
    <div>
        <div v-for="(tag, index) in tags" :key="index">{{ tag }}</div>
    </div>
  
</template>
<script>
import axios from "axios";
import _ from "lodash";

export default {
    data() {
        return {
            tags: []
        };
    },
    methods: {
        getTags() {
            axios
                .get(this.initialData.tagListUrl)
                .then(response => {
                console.log("response", response);
                this.tags = _.map(response.data, 'name');
                })
                .catch(e => {
                console.log("errors", e);
                });
            }

    },
    created() {
        this.getTags();
    }

  
}
</script>
<style>

</style>


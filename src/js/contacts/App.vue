<template>
    <div class="container">

        <ul class="nav nav-pills">
            <router-link to="/" tag="li" active-class="active" class="nav-item"><a>Home</a></router-link>
            <router-link to="/create" tag="li" active-class="active" class="nav-item"><a>Add Contact</a></router-link>
        </ul>

        <hr>
        <router-view></router-view>
    </div>
  
</template>
<script>
export default {};
</script>
<style>
.nav-item {
  padding-right: 15px;
}
</style>


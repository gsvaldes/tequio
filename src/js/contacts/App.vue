<template>
    <div class="container">
        <h1>Contact Nav to go here</h1>
        <ul class="nav nav-pills">
            <router-link to="/" tag="li" active-class="active" class="nav-item"><a>Home</a></router-link>
            <router-link to="/create" tag="li" active-class="active" class="nav-item"><a>Add Contact</a></router-link>
            <router-link to="/detail/3" tag="li" active-class="active" class="nav-item"><a>Detail</a></router-link>
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


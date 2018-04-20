<template>
    <div class="container">

        <ul class="nav nav-pills">
            <router-link to="/" tag="li" active-class="active" class="nav-item"><a>Home</a></router-link>
            <router-link to="/create" tag="li" active-class="active" class="nav-item"><a>Add Contact</a></router-link>
            <router-link to="/tags" tag="li" active-class="active" class="nav-item"><a>Tags</a></router-link>
        </ul>

        <hr>
        <transition name="fade" mode="out-in">
            <router-view></router-view>
        </transition>
    </div>
  
</template>
<script>
export default {};
</script>
<style>
.nav-item {
  padding-right: 15px;
}

.fade-enter-active, .fade-leave-active {
  transition: opacity 0.25s ease-in-out;
}

.fade-enter, .fade-leave-to {
  opacity: 0;
}

</style>


<template>
  <div id="app">
    <div class="wrapper">
      <sidebar></sidebar>
      <div class="content">
        <router-view></router-view>
      </div>  
    </div>
  </div>
</template>

<script>
import './sass/main.scss'
import Sidebar from './components/app/Sidebar.vue'

export default {
  name: 'app',
  components: {
    'sidebar': Sidebar,
  }
}
</script>

<style lang="scss">

</style>

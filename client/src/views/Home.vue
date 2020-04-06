<template>
  <div class="home">
    <HelloWorld msg="Em construção"/>
    <img src="../assets/images/medium-logo.svg" style="opacity:0.5">
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Home',
  components: {
    HelloWorld
  }
}
</script>

<style lang="scss">
.home {
  padding-top: 30px;
}
</style>


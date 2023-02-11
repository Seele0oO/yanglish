<template>
  <img alt="Vue logo" src="./assets/logo.png">
  <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
  <mainBox/>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'

// eslint-disable-next-line no-alert, quotes, semi 
import mainBox from './components/mainBox.vue'

export default {
  name: 'App',
  components: {
    // HelloWorld
    mainBox
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

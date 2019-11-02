<template>
  <div id="app">
    <navbar></navbar>
    <router-view/>
    <flash></flash>
  </div>
</template>

<script>
import Navbar from '@/components/Navbar';
import FlashNotification from '@/common/Flash';

export default {
  name: 'app',
  components: {
    "navbar": Navbar,
    "flash": FlashNotification,
  }
};
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>

<template>
  <div id="app">
      <AppHeader />
      <main>
        <router-view />
      </main>
      <AppFooter />
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import AppHeader from './components/AppHeader.vue';
import AppFooter from './components/AppFooter.vue';

@Component({
  components: {
    AppHeader,
    AppFooter,
  },
})

export default class App extends Vue {}

</script>

<style lang="scss">
  html, body {
    width: 100%;
    height: 100%;
  }

  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    min-height: 100%;
    display: flex;
    flex-direction: column;
    align-items: stretch;
  }

  main {
    flex-grow: 1;
  }

  header, main, footer {
    flex-shrink: 0;
  }

  .page-container {
    margin: 0 auto;
    padding: 20px 15px;
    max-width: 1200px;
  }

  .content-wrapper {
    margin: 0 auto;
  }
  
</style>

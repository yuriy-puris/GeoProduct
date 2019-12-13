<template>
  <div class="home">
    <div class="page-container">
      <Search />
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import Search from '@/components/Search.vue';

@Component({
  components: {
    Search,
  },
})

export default class Home extends Vue {}

</script>

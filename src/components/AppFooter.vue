<template>
    <footer id="footer">
        <md-bottom-bar class="md-accent" md-type="shift">
            <router-link to="/"><md-icon class="md-size-1x">home</md-icon></router-link>
      </md-bottom-bar>
    </footer>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';

@Component({

})

export default class AppFooter extends Vue {}
</script>

<style lang="scss">
    #footer {
        .md-ripple {
            padding: 5px 0;
            justify-content: center
        }  
    }
</style>
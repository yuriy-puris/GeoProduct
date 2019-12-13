<template>
    <div class="search-holder">
        <form v-on:submit.prevent="search">
            <div class="input-group">
                <md-field class="input-group-field">
                    <label>Пожалуйста, введите название товара ...</label>
                    <md-input v-model="query"></md-input>
                    <md-button 
                        class="md-raised" 
                        @click="search">
                        <md-icon>search</md-icon>
                    </md-button>
                </md-field>
            </div>
        </form>
    </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import { State, Action, Getter, Mutation } from 'vuex-class';
import { mapState } from 'vuex';
import axios from 'axios';

@Component({
    computed: {
        ...mapState({
            location: 'currentLocation'
        })
    },
})
export default class Search extends Vue {
    query = '';
    public location: object;

    search () {
        console.log(this.location)
        axios
            .post('http://127.0.0.1:8000/api/store/post_location', this.location)
            .then(response => { 
                console.log(response) })
            .catch(error => { console.log(error) })
    }

}

</script>

<style lang="scss">
    .search-holder {
        .md-field {
            align-items: center;
            &:not(.md-focused) {
                label {
                    top: 30px;
                }
            }
        }
        .md-input {
            text-align: center;
        }
    }
</style>
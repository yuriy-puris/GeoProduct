<template>
    <header id="header">
        <md-toolbar class="md-transparent">
            <!-- <span class="md-title">GeoProduct</span> -->
            <router-link to="/"><strong class="md-title">GeoProduct</strong></router-link>
            <div class="md-toolbar-section-end">
                {{ location }}
            </div>
        </md-toolbar>
    </header>
</template>

<script lang="ts">
import { State, Action, Getter, Mutation } from 'vuex-class';
import { Component, Vue } from 'vue-property-decorator';
import axios from 'axios';

@Component({

    mounted (): void {
        this.locationUser();
    }
    
})
export default class AppHeader extends Vue {
    
    location: string = '';
    geocoderApi: string = 'https://maps.googleapis.com/maps/api/geocode/json?latlng=';
    geocoderApiKey: string = '&key=AIzaSyDybVMhuvhySYB54emzIuWjt1S44P-Z_hg';
    
    locationUser(): void {
        let _self = this;
        if ("geolocation" in navigator) {
            navigator.geolocation.getCurrentPosition(
                function success(position) {
                    _self.definedAddress({ lat: position.coords.latitude, lng: position.coords.longitude });
                },
                function error(error) {
                    console.log(error);
                }
               )
        } else {
            console.log('geolocation not supported')
        }
    }

    definedAddress(Coordinates: any): void {
        let latlng = `${Coordinates.lat},${Coordinates.lng}`;
        axios
            .get(`${this.geocoderApi}${latlng}${this.geocoderApiKey}`)
            .then(response => {
                if ( response.data.status === 'OK' ) {
                    let location = response.data.results[0].formatted_address.split(',').slice(0,-3);
                    this.location = location.join(',');
                    this.$store.commit('setLocation', { item: { lat: Coordinates.lat, lng: Coordinates.lng} });
                }
            })  
            .catch(error => {
                console.log(error);
            });
    }



}

</script>
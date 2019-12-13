import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

const ParamLocationModel = () => {
  return {
    lat: '',
    lon: '',
  }
}

export default new Vuex.Store({
  state: {
    currentLocation: ParamLocationModel(),
  },
  mutations: {
    setLocation(state, {item}) {
      state.currentLocation = item;
    }
  },
  actions: {
  },
  modules: {
  },
});

import Vue from 'vue'
import Vuex from 'vuex'

// imports of AJAX functions will go here
import { authenticate, submit_article } from '@/api'
import { isValidJwt, EventBus } from '@/utils'
// to get persistent user session

Vue.use(Vuex)

const userState = JSON.parse(window.localStorage.getItem('user_state'));

const state = {
  // single source of data
  user: userState ? userState.user || {} : {},
  jwt: userState ? userState.jwt || '' : '',
}

const actions = {
  // asynchronous operations
  login (context, userData) {
    return authenticate(userData)
      .then((res) => {
        const status = res.data.status;
        const data = res.data.data;
        if (status == 'ERROR') {
          EventBus.$emit('flash-add-notification', {
            title: "Invalid User",
            text: data,
            type: "alert-danger",
          });
        } else {
          context.commit('setUserData', { 'username': userData.username })
          context.commit('setJwtToken', { jwt: data.token });
          window.localStorage.setItem('user_state', JSON.stringify({
            'user': { 'username': userData.username },
            'jwt': data.token,
          }));
        }
      })
      .catch((error) => {
        EventBus.$emit('flash-add-notification', {
          title: "Error",
          text: "Cannot connect to the server to log in",
          type: "alert-danger",
        });
      })
  },
  logout (context) {
    if (getters.isAuthenticated(state)) {
      context.commit('setUserData', {});
      context.commit('setJwtToken', '');
      window.localStorage.clear();
      EventBus.$emit('flash-add-notification', {
        title: "Success",
        text: "Logged out",
        type: "alert-success",
      });
    }
  },
  add_article (context, article_data) {
    return submit_article(article_data, context.state.jwt.token);
  }
}

const mutations = {
  // isolated data mutations
  setUserData (state, payload) {
    console.log('setUserData payload = ', payload)
    state.userData = payload.userData
  },
  setJwtToken (state, payload) {
    console.log('setJwtToken payload = ', payload)
    if (payload == '') {
      state.jwt = '';
    } else {
      localStorage.token = payload.jwt.token
      state.jwt = payload.jwt
    }
  },
}

const getters = {
  // reusable data accessors
  userData (state) {
    return state.user;
  },
  isAuthenticated (state) {
    return isValidJwt(state.jwt.token)
  },
}

const store = new Vuex.Store({
  state,
  actions,
  mutations,
  getters,
})

export default store;

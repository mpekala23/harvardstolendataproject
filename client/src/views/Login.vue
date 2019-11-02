<template>
    <div id="login">
        <h1>Login</h1>
        <form @submit.prevent="login">
          <input type="text" name="username" v-model="input.username" placeholder="Username" />
          <input type="password" name="password" v-model="input.password" placeholder="Password" />
          <button type="submit">Login</button>
        </form>
        <button @click="logout">Logout</button>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'login',
    data() {
        return {
            input: {
                username: "",
                password: "",
            }
        }
    },
    methods: {
        login() {
          console.log(window.localStorage);
            if(this.input.username != '' && this.input.password != '') {
              this.$store.dispatch('login', this.input)
                .then(() => {
                  if (this.$store.getters.isAuthenticated) {
                    this.$router.push('/add-article');
                  }
                })
            } else {
                console.log('Login requires a username and password');
                this.$eventHub.$emit('flash-add-notification', {
                  title: "Error",
                  text: "Log in requires username and password",
                  type: "alert-danger",
                })
            }
        },
        logout() {
          this.$store.dispatch('logout');
        },
    },
    created() {
      if (this.$store.isAuthenticated) {
        this.$router.push('/add-article');
      }
    }
}
</script>

<style scoped>
    #login {
        width: 500px;
        border: 1px solid #CCCCCC;
        background-color: #FFFFFF;
        margin: auto;
        margin-top: 200px;
        padding: 20px;
    }
</style>

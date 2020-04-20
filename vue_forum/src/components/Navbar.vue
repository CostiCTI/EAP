<template>
    <div class="topnav">
    <ul>
        <li>
            <router-link to="/">Home</router-link>
        </li>

        <li v-if="auth=='loggedin'">
            <router-link to="/challenges">Challenges</router-link>
        </li>

        <li v-if="auth=='loggedin'">
            <router-link to="/profile">Profile</router-link>
        </li>

        <li v-if="auth=='loggedin'">
            <router-link to="/top">Top</router-link>
        </li>

        <li v-if="auth==''" style="padding-left: 85%;">
            <router-link to="/login">Login</router-link>
        </li>

        <li v-if="auth==''">
            <router-link to="/register">Register</router-link>
        </li>

        <li v-if="auth=='loggedin'" style="padding-left: 75%;">
            <a href="" v-on:click="logout">Logout</a>
        </li>
    </ul>
    </div>
</template>

<script>
import EventBus from './EventBus'
EventBus.$on('logged-in', test => {
  console.log(test)
})
export default {
  data () {
    return {
      auth: '',
      user: '',
    }
  },
  methods: {
    logout () {
      localStorage.removeItem('usertoken')
    }
  },
  mounted () {
    EventBus.$on('logged-in', status => {
      this.auth = status
    })
  }
}
</script>

<style scoped>
.topnav {
  overflow: hidden;
  background-color: #29a355;
}

.topnav a {
  float: left;
  color: #f2f2f2;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
  font-size: 17px;
}

.topnav a:hover {
  background-color: #47bf5d;
  color: black;
}

li {
  float: left;
  text-decoration: none;
}

ul {
  list-style-type:none;
}
</style>

{{} /* 

       <nav class="navbar navbar-expand-lg navbar-dark bg-dark rounded">
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-targer="#navbar1" aria-controls="navbar1"
            aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggle-icon"></span>
        </button>

        <div id="navbar1">
            <ul class="navbar-nav">
                <li v-if="auth=='loggedin'" class="nav-item">
                    <router-link class="nav-link menucode" to="/">Home</router-link>
                </li>

                <li v-if="auth=='loggedin'" class="nav-item">
                    <router-link class="nav-link" to="/posts">Posts</router-link>
                </li>

                <li v-if="auth==''" class="nav-item">
                    <router-link class="nav-link" to="/login">Login</router-link>
                </li>

                <li v-if="auth==''" class="nav-item">
                    <router-link class="nav-link" to="/register">Register</router-link>
                </li>

                <li v-if="auth=='loggedin'" class="nav-item">
                    <router-link class="nav-link" to="/profile">Profile</router-link>
                </li>

                <li v-if="auth=='loggedin'" class="nav-item">
                    <a class="nav-link" href="" v-on:click="logout">Logout</a>
                </li>
            </ul>
        </div>
    </nav>
*/ }}
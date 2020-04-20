<template>
  <div class="container">
    <div class="row">
      <div class="col-md-6 mt-5 mx-auto">
        <form v-on:submit.prevent="register">
          <h1 class="h3 mb-3 font-weight-normal">Register</h1>
          <div class="form-group">
            <label for="username">Username</label>
            <input type="text" v-model="username" class="form-control" name="username" placeholder="Enter Username" required>
          </div>
          <div class="form-group">
            <label for="email">Email Address</label>
            <input type="email" v-model="email" class="form-control" name="email" placeholder="Enter email" required>
          </div>
          <div class="form-group">
            <label for="password">Password</label>
            <input type="password" v-model="password" class="form-control" name="password" placeholder="Enter Password" required> 
          </div>
          <button class="btn btn-lg btn-success btn-block">Register</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import router from '../router'
export default {
  data () {
    return {
      username: '',
      email: '',
      password: '',
      job: ''
    }
  },
  methods: {
    register () {
      axios.post('http://localhost:5000/users/register', {
        username: this.username,
        email: this.email,
        password: this.password,
      }).then((res) => {
        this.username = '',
        this.email = '',
        this.password = '',
        console.log(res)
        router.push({ name: 'Login' })
      }).catch((err) => {
        this.username = '',
        this.email = '',
        this.password = '',
        this.job = ''
        console.log(err)
      })
    }
  }
}
</script>
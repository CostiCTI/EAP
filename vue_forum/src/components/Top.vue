<template>
    <div>
        <br>
        <br>
        <h2 style="text-align: center; font-style: italic;"> HALL OF FAME </h2>
        <br>
        <div style="margin-left: 60px; margin-right: 60px;" v-for="(user, index) in users" :key="user">
            <div style="float: left;"> {{ index + 1}}. {{ user[0] }} </div>  <div style="float: right;"> {{ user[1] }} challenges </div>
            <br>
            <hr>
         </div>   
    </div>
</template>


<script>
import jwtDecode from 'jwt-decode'
import axios from 'axios'

export default {
  data () {
    const token = localStorage.usertoken
    const decoded = jwtDecode(token)
    return {
      username: decoded.identity.username,
      email: decoded.identity.email,
      userid: decoded.identity.userid,
      users: []
    }
  },
  methods: {
    get_top() {
      axios.get('http://localhost:5000/top', {})
      .then((res) => {
        this.users = res.data['result']
      }).catch((err) => {
        console.error(err)
      })
    }
  },
  beforeMount(){
    this.get_top()
  },
}
</script>
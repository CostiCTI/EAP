<template>
    <div class="container">
      <br>
      <br>
      <h3 id="chmsg"> Pick a challenge </h3>
      <br>
      <br>
      <div v-bind:key="challenge.id" v-for="challenge in challenges">
        <Challenge v-bind:challenge="challenge" />
      </div>    
    </div>
</template>

<script>
import jwtDecode from 'jwt-decode'
import axios from 'axios'
import Challenge from './Challenge.vue'

export default {
  data () {
    const token = localStorage.usertoken
    const decoded = jwtDecode(token)
    return {
      username: decoded.identity.username,
      email: decoded.identity.email,
      domains: '',
      challenges: ''
    }
  },
  components: {
    Challenge
  },
  methods: {
    get_challenges () {
      axios.get('http://localhost:5000/challenges', {})
      .then((res) => {
		this.challenges = res.data['result']
      }).catch((err) => {
        console.error(err)
      })
    }
  },
  beforeMount(){
    this.get_challenges()
  },

}

</script>

<style scoped>
#chmsg {
  text-align: center;
  color: green
}
</style>
<template>
    <div class="domain">
        <div class="challenge" v-on:click="openChallenge" v-bind:class="[isSolved ? 'greenc' : 'whitec']">
            <h4 style="margin-top: 20px;"> {{ challenge.title }} </h4>
            <div v-for="index in challenge.difficulty" :key="index" style="display: inline-block; opacity: 0.7; margin-bottom: 20px;">
              <img src="../assets/star2.png" height="25px" width="25px">
            </div>
        </div>
    </div>
</template>

<script>
//import axios from 'axios'
import jwtDecode from 'jwt-decode'

export default {
  name: "Challenge",
  props: ["challenge"],
   data () {
    const token = localStorage.usertoken
    const decoded = jwtDecode(token)
    return {
      email: decoded.identity.email,
      userid: decoded.identity.userid,
      schallenges: decoded.identity.schallenges,
      isSolved: false,
    }
  },
  methods: {
    openChallenge () {
      this.$router.push('/tasks/' + this.challenge.id);
    },
    get_solved() {
      if (this.schallenges.includes(this.challenge.id))
        this.isSolved = true
      else
        this.isSolved = false
    }
  },
  created: function() {
     this.get_solved()
  }

}

</script>

<style scoped>

.greenc {
  background-color: #6ed169;
}

.whitec {
  background-color: white;
}

.challenge {
    border-radius: 25px;
    float: left;
    padding-left: 20px;
    padding-right: 20px;
    margin-left: 10px;
    margin-top: 10px;
    padding-top: 10px;
    padding-bottom: 10px;
    font-family: "Times New Roman";
    border-style: solid;
    width: 250px;
    text-align: center;
    align: center;
}

.delb {
  float: right;
  background-color: rgb(255, 77, 77);
}

</style>
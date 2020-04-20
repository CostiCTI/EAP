<template>
    <div class="container">
              <div>
                <br>
                <input type="text" placeholder="answer..." ref="tf" style="float: left; width: 400px;">
                <button class="subbut" v-on:click="submit_answer" style="background-color: #8ae887; width: 100px; height: 35px;"> Submit </button>
              </div>
              <hr>
              <div v-bind:key="task.id" v-for="task in tasks">
                <Task v-bind:task="task" />
              </div>
    </div>
</template>

<script>
import jwtDecode from 'jwt-decode'
import axios from 'axios'
import Task from './Task.vue'

export default {
  data () {
    const token = localStorage.usertoken
    const decoded = jwtDecode(token)
    return {
      username: decoded.identity.username,
      email: decoded.identity.email,
      userid: decoded.identity.userid,
      tasks: '',
      chid: window.location.href.split('/').pop(),
      ans: '0'
    }
  },
  components: {
    Task
  },
  methods: {
    get_tasks () {
      axios.get('http://localhost:5000/tasks/' + this.chid, {})
      .then((res) => {
		this.tasks = res.data['result']
      }).catch((err) => {
        console.error(err)
      })
    },
     submit_answer() {
      this.ans = this.$refs.tf.value
      this.$refs.tf.value = ''
      axios.post('http://localhost:5000/chanswer', {
        userid: this.userid,
        challengeid: this.chid,
        answer: this.ans,
      })
      .then((res) => {
        if (res.data['result']['answer'] == 1) {
          console.log(res.data['result']['answer'])
          this.$refs.tf.placeholder = 'Correct'
          this.$refs.tf.style.backgroundColor = '#6ed169'
        } else {
          this.$refs.tf.placeholder = 'Wrong answer'
          this.$refs.tf.style.backgroundColor = 'pink'
        }
      }).catch((err) => {
        console.error(err)
      })
    }
  },
  beforeMount(){
    this.get_tasks()
  },

}

</script>

<style scoped>

.cc {
  font-family: TimesNewRoman;
}

.cd {
  font-size: 25px;
}

</style>
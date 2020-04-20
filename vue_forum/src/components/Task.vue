<template>
    <div class="task">
        <div class="dom" v-bind:class="[isSolved ? 'greenc' : 'whitec']">
            <h5 id="title" style="float: left"> {{ task.title }} </h5>
            <button  style="float: right" v-on:click="expand_text"> Expand </button>
            <br>
            <div v-bind:class="[isActive ? 'act' : 'noact']">
              <p> {{ task.description }} </p>
              <input type="text" placeholder="answer..." ref="tf" style="width: 80%;"><br>
              <div id='ansdiv'> ... </div>
              <button class="subbut" style="float: right;" v-on:click="submit_answer" > {{ name }} </button>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import jwtDecode from 'jwt-decode'

export default {
  name: "task",
  props: ["task"],
   data () {
    const token = localStorage.usertoken
    const decoded = jwtDecode(token)
    return {
      email: decoded.identity.email,
      userid: decoded.identity.userid,
      stasks: decoded.identity.stasks,
      name: 'Submit',
      isActive: false,
      isSolved: false,
      ans: '0'
    }
  },
  methods: {
    expand_text() {
      this.isActive = !this.isActive
    },
    submit_answer() {
      this.ans = this.$refs.tf.value
      axios.post('http://localhost:5000/answer', {
        userid: this.userid,
        taskid: this.task.id,
        answer: this.ans,
      })
      .then((res) => {
        if (res.data['result']['answer'] == 1) {
    this.isSolved = true
    this.stasks.push(this.task.id)
    this.get_solved()
        }
      }).catch((err) => {
        console.error(err)
      })
    },
    get_solved() {
      if (this.stasks.includes(this.task.id))
        this.isSolved = true
      else
        this.isSolved = false
    },
    beforeMount(){
      this.get_solved()
      console.log(this.stasks)
    },
  },
  created: function() {
     this.get_solved()
     console.log(this.stasks)
  }

}

</script>

<style scoped>

#ansdiv {
  float: left;
  margin-left: 10px;
}

.subbut {
    background-color: green;
    color: white;
    width: 100px;
    height: 40px;
}

.greenc {
  background-color: #6ed169;
}

.whitec {
  background-color: white;
}

.dom {
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
    width: 80%;
}

.act {
  display: "unset";
}

.noact {
  display: none;
}

</style>
<template>
    <div class="domain">
        <div class="comment">
            <p> Author: {{ comment.cuser }}</p>
            <p> {{ comment.text }} </p>
            <button class="delb" @click="del_comment"> Delete comment </button>
            <br>
            <hr>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import jwtDecode from 'jwt-decode'

export default {
  name: "Comment",
  props: ["comment"],
   data () {
    const token = localStorage.usertoken
    const decoded = jwtDecode(token)
    return {
      email: decoded.identity.email
    }
  },
  
  methods: {
    del_comment () {
      axios.delete('http://localhost:5000/comments', {
        data: { comid: this.comment.id,
                useremail: this.email
              }
      })
      .then((res) => {
        console.log(res.data['result'])
      }).catch((err) => {
        console.error(err)
      })
    }
  }

}

</script>

<style scoped>
.delb {
  float: right;
  background-color: rgb(255, 128, 128);
}
</style>
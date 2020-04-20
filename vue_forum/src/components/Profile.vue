<template>
    <div class="profilediv">
        <br>
        <div id="uname"> 
            {{ username }}
            <hr style="border: 1px solid green; border-radius: 1px;">
            <div id="xp"> 
                <div> XP </div>
                <div style="color: black;"> {{ this.xp }} </div> 
            </div>
            <div id="lev"> 
                <div> LEVEL </div> 
                <div style="color: black;"> {{ this.level }} </div>
            </div>
            <div id="stars"> 
                <div style="float: left; margin-left: 120px;"><img src="../assets/star2.png" height="40px" width="40px"></div>
                <div style="color: black; padding-top: 2.5px;"> {{ this.stars }} </div>
            </div>
         </div>
         <div style="clear:both;"></div>
         <hr>
         <br>
         <div style="margin-left: 200px;"> Solved challenges: {{ this.names.length }}</div>
         <br>
         <div style="margin-left: 220px; margin-right: 220px;" v-for="name in names" :key="name">
            <div id="ch"> {{ name }} </div>
         </div>
         <div style="clear:both;"></div>
        
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
      xp: 0,
      level: 0,
      stars: 0,
      names: []
    }
  },
  methods: {
    get_stats() {
      axios.post('http://localhost:5000/stats', {
        userid: this.userid
      })
      .then((res) => {
        res = res.data['result']
        this.xp = res['xp']
        this.stars = res['stars']
        this.level = res['level']
        this.names = res['names']
      }).catch((err) => {
        console.error(err)
      })
    }
  },
  beforeMount(){
    this.get_stats()
  },
}
</script>

<style scoped>

#ch {
    float: left;
    margin-left: 12px;
    font-size: 18px;
    border: 1px solid;
    border-radius: 16px;
    padding-left: 30px;
    padding-right: 30px;
    margin-top: 10px;
    background-color: #7ccbcc;
}

#uname {
    margin-left: 200px;
    font-size: 32px;
    color: green;
    margin-right: 200px;
    display: block;
}

#xp {
    width: 25%;
    margin-left: 10%;
    height: 260px;
    background-color: white;
    float: left;
    font-size: 38px;
    text-align: center;
    border-left: 2px solid green;
    padding-top: 70px;
    margin-top: 20px;
    position: relative;
}

#lev {
    width: 30%;
    height: 300px;
    background-color: white;
    float: left;
    border-left: 2px solid green;
    border-right: 2px solid green;
    padding: initial;
    font-size: 44px;
    text-align: center;
    padding-top: 80px;
    position: relative;
}

#stars {
    width: 25%;
    height: 260px;
    background-color: white;
    float: left;
    font-size: 38px;
    border-right: 2px solid green;
    padding-top: 95px;
    margin-top: 20px;
    position: relative;
}

</style>
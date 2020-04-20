<template>
  <div class="hello">
    <br> <br> <br> <br>
    <h1 id="m1"> {{ msg }} </h1>
    <br> <br> <br>
    <h2 id="m2"> {{ msg1 }} </h2>
    <br> <br> <br>
    <p id="par"> Challenge Platform is a place where you can have fun by solving various challenges that implies knowledge in areas
    like mathematics, computer science, crypto and others. By solving these challenges you get xp and can compare yourself 
    with the others. It is very important to solve the tasks by yourself but the most important thing is to learn so you should search
    for help only when you are blocked and you have no ideea how to solve them. Have fun! </p>
    <p id="par2">
    In order to solve a challenge you need to solve all tasks asigned to that challenge. The answer that solve the challenge is obtained
    from tasks answers. For example, let say that we have a challenge with 3 tasks. For the first task the answer is '15', for the second task
    the answer is '152' and for the third task the answer is 'example'. Then the answer for the challenge is {15-152-example}.
    </p>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Challenge Platform',
      msg1: 'Welcome'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#m1 {
  text-align: center;
  color: green;
}
#m2 {
  text-align: center
}
#par {
  padding-left: 8%;
  padding-right: 8%;
  color: grey;
}
#par2 {
  padding-left: 8%;
  padding-right: 8%;
  color: grey;
}
</style>
# vue practice

## App.vue

```vue
<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/random">Random</router-link> |
      <router-link to="/mymovielist">MyMovieList</router-link>
    </div>
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>

```



## index.html

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width,initial-scale=1.0">
    <link rel="icon" href="<%= BASE_URL %>favicon.ico">
    <title><%= htmlWebpackPlugin.options.title %></title>
     <!--bootstrap CDN가져옴-->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
  </head>
  <body>
    <noscript>
      <strong>We're sorry but <%= htmlWebpackPlugin.options.title %> doesn't work properly without JavaScript enabled. Please enable it to continue.</strong>
    </noscript>
    <div id="app"></div>
    <!-- built files will be auto injected -->
  </body>
</html>

```





## index.js

```js
import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../components/Home.vue'
import Random from '../components/Random.vue'
import MyMovieList from '../components/MyMovieList.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/random',
    name: 'Random',
    component: Random
  },
  {
    path: '/mymovielist',
    name: 'MyMovieList',
    component: MyMovieList
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

```



## Home.vue

```vue
<template>
  <div class='container'>
    <h1>Movies</h1>
    <div class="row">
      <MovieCard
        v-for="movie in movies"
        :movie="movie"
        :key="movie.id"
        class="col-4"
      />
    </div>
  </div>
</template>

<script>
import MovieCard from './MovieCard.vue'
import axios from 'axios'


export default {
  components: { MovieCard },
  data(){
    return {
      // 전체 영화를 담을 배열
      movies:[],
    }
  },
  created(){
    axios({
      url: 'https://gist.githubusercontent.com/eduChange-hphk/756c987fe4ecf20ef27fd1d29f90764e/raw/f5a6acfed6bbe837d7f2f173a5b84221ee54c3b2/movies.json',
      method:'GET'
    }).then((res)=>{
      // console.log(res.data)
      this.movies = res.data
      console.log(this.movies)
    }).catch((err)=>{
      console.error(err)
    })
  },
}
</script>

<style>

</style>
```



## MovieCard.vue

``` vue
<template>
  <div class="card row" style="width: 18rem;">
    <img :src="posterPath" class="card-img-top" alt="#">
    <div class="card-body">
      <h5 class="card-title text-center">{{ movie.title }}</h5>
      <p class="card-text text-center">{{ movie.overview }}</p>
      <!-- <a href="#" class="btn btn-primary">Go somewhere</a> -->
    </div>
  </div>
</template>

<script>
export default {
  props:{
    movie:Object,
  },
  computed:{
    posterPath(){
      return this.movie.poster_path
    },
  },
}
</script>

<style>

</style>
```



## MyMovieList.vue

```vue
<template>
  <div>
    <ul class="list-group">
      <!-- myListForm 컴포넌트에 데이터 myMovie를 props로 쓸수있게 보내줌  -->
      <MyListForm
      @addMovie="addMovie"/>
      
      <MyList v-for="movie in movies"
      :movie="movie"
      :key="movie.id"/>
    </ul>
  </div>
</template>

<script>
import MyListForm from './MyListForm'
import MyList from './MyList'

export default {
  //name? 
  components: {
    MyListForm,
    MyList,
  },
  data() {
    return {
      movies:[],
    }
  },
  methods:{
    addMovie(movie){
      this.movies.push(movie)
    }
  },

}
</script>

<style>

</style>
```



## MyListForm.vue

```vue
<template>
  <div>
    <h1>My Movie List</h1>
    <div>
      <div class="input-group w-75 mx-auto mb-3">
      <input type="text"
      placeholder="보고싶은 영화를 입력해주세요" 
      class="form-control"
      @keyup.enter="addMovie"
      >
      <div class="input-group-append">
        <button type="button" id="button-addn2" class="btn btn-outline-secondary" @click="addMovie">Add</button>
      </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    addMovie(event) {
      this.$emit('addMovie',event.target.value)
      event.target.value = ''
    }
  },
}
</script>

<style>

</style>
```



## MyList.vue

```vue
<template>
  <div>
    <li class="list-group-item col-8 offset-2">
      <input type="checkbox" 
      :checked="movie.isCompleted" 
      :class="{ completed: movie.completed }"
      >
      <span>{{ movie }}</span>
    </li>
  </div>
</template>

<script>
export default {
  props:{
    movie:[Object,String],
  },
  methods:{
    
  }
}
</script>

<style>

</style>
```



## Random.vue

```vue
<template>
  <div class='container'>
    <button class='btn btn-success mb-3' @click='pickOne'>Pick!</button>
    <div class='jumbotron jumbotron-fluid'>
      <div class="container">
        <h1 class="display-4">오늘의 추천 영화 : {{ selectRandomMovie }}</h1>
      </div>
    </div>
  </div>
</template>

<script>
import _ from 'lodash'
import axios from 'axios'

export default {
  data(){
    return {
      movies :[],
      selectRandomMovie: '',
    }
  },
  methods: {
    pickOne(){
      // const num = Math.floor(Math.random()*100)
      const num = _.random(this.movies.length-1)
      this.selectRandomMovie = this.movies[num]
      },
  },
  created(){
    axios({
      url:'https://gist.githubusercontent.com/eduChange-hphk/756c987fe4ecf20ef27fd1d29f90764e/raw/f5a6acfed6bbe837d7f2f173a5b84221ee54c3b2/movies.json',
      methods:'GET',
    }).then((res)=>{
      // 배열에 넣어서 movies에 넣어주지 않으면 뷰가 인식하지 못함!
      const temp = []
      res.data.forEach(function(element){
        temp.push(element.title)
      })
      this.movies = temp
    }).catch((err)=>{
      console.error(err)
    })
  },
  
}
</script>

<style>

</style>
```


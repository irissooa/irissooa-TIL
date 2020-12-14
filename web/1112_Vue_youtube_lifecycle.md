# Vue

## Vue_props,emit event활용

- App.vue

```html
<template>
  <div>
    <h1>App</h1>
    <input type="text" v-model="appData" >
    <p>appData: {{ appData }}</p>
    <p>parentData: {{ parentData }}</p>
    <p>childData: {{ childData }}</p>
    <!-- onParentDataChange라는 이름의 이벤트리스너를 달아둠 -->
    <!-- Parent에서 해당 이벤트 발생시키면 내가 필요한 일(onParentDataChange) 함 -->
    <Parent 
      :appData="appData"
      :parentData="parentData"
      :childData="childData"
      @onParentDataChange="onParentDataChange"
      @onChildDataChange="onChildDataChange"
    />
  </div>
</template>

<script>
import Parent from './components/Parent.vue'

export default {
  name:'App',
  components:{
    Parent,
  },
  data: function (){
    return {
      appData:'',
      parentData: '',
      childData: '',
    }
  },
  methods:{
    // onParentDataChange 이벤트 발생시 해야될 일
    // 이벤트 발생 시 인자 전달 받는 것 가능
    onParentDataChange: function(parentData){
      this.parentData = parentData
    },
    onChildDataChange: function(childData){
      this.childData = childData
    },
  }
}
</script>

<style>

</style>
```

- Parent.vue

```html
<template>
  <div>
    <h1>Parent</h1>
    <input type="text" @keyup="onChange">
    <p>appData: {{ appData }}</p>
    <p>childData: {{ childData }}</p>
    <Child
      :appData="appData"
      :parentData="parentData"
      @onChildDataChange="onChildDataChange"
    />
  </div>
</template>

<script>
import Child from './Child.vue'
export default {
  components:{
    Child,
  },
  // props: ['appData',], 이렇게도 가능!
  props:{
    appData: {
      type: String,
    },
    parentData: {
      type: String,
    },
    childData: {
      type: String,
    },
  },
  methods: {
    onChange: function(event){
      // 부모가 달아둔 onParentDataChange라는 이벤트 발생시킴
      // 발생시키면서 인자 전달
      this.$emit('onParentDataChange', event.target.value)
    },
    onChildDataChange(childData) {
      this.$emit('onChildDataChange', childData)
    }
  }
}
</script>

<style>

</style>
```

- Child.vue

```html
<template>
  <div>
    <h1>Child</h1>
    <input type="text" @keyup="onChildDataChange">
    <p>appData: {{ appData }}</p>
    <p>parentData: {{ parentData }}</p>
  </div>
</template>

<script>
export default {
  props:{
    appData: {
      type: String,
    },
    parentData: {
      type: String,
    },
  },
  methods: {
    onChildDataChange(event){
      this.$emit('onChildDataChange', event.target.value)
    }
  },
}
</script>

<style>

</style>
```



## Vue 실습_Youtube검색

- App.vue

```html
<template>
  <div>
    <!-- component를 아래처럼 쓰기도 함! -->
    <!-- <serarch-bar></search-bar> or <serarch-bar/>-->
    <SearchBar 
      :userInput='userInput' 
      @changeUserInput='onChangeUserInput'
    />
    <VideoList 
    :videos='videos'
    @select-video='onSelectVideo'
     />
    <VideoDetail
    :selectedVideo='selectedVideo'
    />
  </div>

</template>

<script>
import axios from 'axios'
import SearchBar from './components/SearchBar'
import VideoList from './components/VideoList'
import VideoDetail from './components/VideoDetail'

// user가 입력하는 데이터, videos -> data로 관리를 해야되는 데이터! -> 컴포넌트상 어디에 위치해야하는가!
// data로 관리하지 않아야하는 데이터
// 1.시간에 따라 변하지 않는다. 이미 data로 관리되고 있는 애로부터 계산가능한 데이터(videotitle, videothumbnail)
export default {
  name: 'App',
  components: {
    SearchBar,
    VideoList,
    VideoDetail,
  },
  data(){
    // 선생님은 보통 해당 정보가 뭔지 알게 해주는게 좋아서 selectedVideo를 string이 아니라 객체로 하는게 좋다고함
    return {
      userInput:'',
      videos:[],
      selectedVideo:'' ,
    }
  },
  methods:{
    onSelectVideo(video){
      console.log('app',video)
      this.selectedVideo = video
    },
    onChangeUserInput(input){
      this.userInput = input
      // 입력값을 할당한 뒤,
      // 유튜브 영상 검색하는 api를 사용! GET요청
      const API_URL = 'https://www.googleapis.com/youtube/v3/search'
      const API_KEY = '######'
      // 검색어가 없으면 작동안함
      if (this.userInput === ''){
        return
      }
      axios({
        url:API_URL,
        method:'GET',
        // params는 쿼리스트링으로 인자를 주고 싶다면 axios에서는 이런식으로 쓸 수 있다! 
        // key=API_KEY&part='snippet'&type='video'&q='this.userInput'
        params:{
          key:API_KEY,
          part:'snippet',
          type:'video',
          q:this.userInput,
        },
      }).then(res=>{
        this.videos = res.data.items
      }).catch(err=>{
        console.log(err)
      })
    },
  },
  // 감시하고 싶은 이름과 똑같은 이름을 만듦
  // watch는 data를 감시해서 변경되면 실행됨!!
  // 어떤 행동을 하기위해 작성
  // computed(값을 구하기위해) Vs watch(행동을 하기위해) 작성됨
  watch:{
    userInput(value){
      if (value==='bad') {
        alert('말조심!')
      }
    }
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

```

- SearchBar.vue

```html
<template>
  <div>
    <!-- change이벤트는 엔터를 치거나 포커스가 다른 곳으로 넘어가면 적용됨 -->
    <input type="text" 
      :value='userInput'
      @change='onChange'
    >
  </div>
</template>

<script>
export default {
  props:{
    // 부모에서 searchBar component를 쓸 때 데이터 타입이 string이어야하고 안넘겨주면 안된다라는걸 명시해줌!
    userInput:{
      type:String,
      required:true,
    },
    // userInput: String,
  },
  methods:{
    onChange(event){
      this.$emit('changeUserInput',event.target.value)
    },
  },
}
</script>

<style>

</style>
```

- VideoList.vue

```html
<template>
  <div>
    <ul>
      <!-- v-for를 통해서 여러 컴포넌트를 반복시킬때 반드시 바인딩 해줘야되는게
       key(고유값, 보통 string)라는 속성! 모든 video마다 중복되지 않은 고유값을 부여해줘야됨
       -->
      <VideoItem v-for='video in videos' 
      :video='video' 
      :key='video.id.videoId'
      @select-video='onSelectVideo'
      />
      
    </ul>
    
  </div>
</template>

<script>
import VideoItem from './VideoItem.vue'
export default {
  components:{
    VideoItem,
  },
  props:{
    videos:Array,
  },
  methods:{
    onSelectVideo(video){
      console.log(video, 'list')
      this.$emit('select-video',video)
    }
  },
  
}
</script>

<style>

</style>
```

- VideoItem.vue

```html
<template>
  <div @click='onClick'>
    <li>
  <!-- vue는 templates이 길어지는걸 지양함!-> computed옵션이 있음! -->
      <img 
        :src="thumbnailUrl"
        alt="thumbnail"
        width="320"
        height='180'
      >
      <span>{{ title }}</span>
    </li>
  </div>
</template>


<script>
import _ from 'lodash'

export default {
  props:{
    video:Object,
    // video:{type:Object}
  },
  methods:{
    // props에 있는 video데이터를 가져옴
    onClick(){
      console.log(this.video.id.videoId)
      this.$emit('select-video',this.video)
    }
    
  },
  // 메소드 처럼 함수..
  // 반드시 리턴값이 있어야됨, computed는 어떤 값을 구하기위해사용함!
  computed:{
    thumbnailUrl(){
      return this.video.snippet.thumbnails.medium.url
    },
    title(){
      return _.unescape(this.video.snippet.title)
    },

  },
}
</script>

<style>

</style>
```

- VideoDetail.vue

```html
<template>
<!-- id객체가 있으면 랜더링, 아니면 랜더링 안함! -->
  <div v-if="selectedVideo">
    <!-- 리스트 중에서 선택한video가 밑에 떠야한다 -->
    <!-- videoitem 클릭되면 최종적으로 app에게 video를 선택해달라고 요청,(이벤트를 보냄), selectedVideo가 설정됨 -->
  <iframe :src="videoSrc" frameborder="0"></iframe>
  <input type="text">
  <input type="text">
  </div>

</template>

<script>
export default {
  // 객체, String둘다 허용해준다는 말
props:{
  selectedVideo:[Object,String],
},
computed:{
    videoSrc(){
      const videoId = this.selectedVideo.id.videoId
      console.log(this.selectedVideo)
      return `https://www.youtube.com/embed/${videoId}`
    }
  },
}
</script>

<style>
/* 해당 컴포넌트만 style적용하고 싶으면 style scoped 라고 적고 하면됨! */
</style>
```


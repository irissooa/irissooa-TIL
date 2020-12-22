<template>
  <ul class="news-list">
    <li class="post" v-for="item in listItems" :key="item.id">
      <div class="points">
        {{item.points || 0}}
      </div>
      <div>
        <p class="news-title">
          <template v-if="item.domain">
            <a :href="item.url">{{item.title}}</a><small class="link-text" v-if="item.domain">{{item.domain}}</small>
          </template>
          <template v-else>
            <router-link :to="`/item/${item.id}`">{{item.title}}</router-link><small><a :href="item.domain" class="link-text" v-if="item.domain">{{item.domain}}</a></small>
          </template>  
        </p>
        <small class="link-text" v-if="item.user">
          by
          <router-link class="link-text" :to="`/user/${item.user}`">{{item.user}}</router-link>
        </small>
        <small class="link-text" v-if="item.time_ago">
          {{item.time_ago}}
        </small>
      </div>
    </li>
  </ul>
</template>

<script>
// 아래의 코드를 쓰면 eslint가 꺼짐 -> computed는 기본적으로 리턴값이 있어야되는데 if안에 안들어가면 return값이 없기때문에 에러가 남!
/* eslint-disable */
export default {
  // computed: {
  //   listItems() {
  //     if (this.$route.path === "/news") {
  //       return this.$store.state.news;
  //     } else if (this.$route.path === "/ask") {
  //       return this.$store.state.ask;
  //     } else if (this.$route.path === "/jobs") {
  //       return this.$store.state.jobs;
  //     }
  //   }
  // }
  computed: {
    listItems() {
      return this.$store.getters.fetchedList;
    }
  }
}
</script>

<style scoped>
.news-list {
  padding: 0;
  margin: 0;
}
.post {
  list-style: none;
  display: flex;
  align-items: center;
  border-bottom: 1px solid #eee;
}
.points {
  width: 80px;
  height: 60px;
  color: #42b883;
  display: flex;
  align-items: center;
  justify-content: center;
}
.link-text {
  color: #828282;
}
.news-title {
  margin: 0;
}
</style>

<template>
  <section>
    <transition-group name="list" tag="ul">
      <li v-for="(todo,index) in $store.state.todoItems" class="shadow" :key="todo.item">
        <i class="checkBtn fas fa-check" @click="togleComplete(todo,index)" :class="{checkBtnCompleted:todo.completed}"></i>
        <span :class="{textCompleted:todo.completed}">{{todo.item}}</span>
        <span class="removeBtn" @click="removeTodo(todo, index)">
          <i class="removeBtn fas fa-trash-alt"></i>
        </span>
      </li>
    </transition-group>
  </section>
</template>

<script>
export default {
  methods : {
    removeTodo(todo,index) {
      this.$store.commit('removeOneItem',{todo,index});
    },
    togleComplete(todo,index) {
      this.$store.commit('toggleOneItem',{todo,index});
    },

  },

}
</script>

<style scoped>
ul {
  list-style-type: none;
  padding-left: 0px;
  margin-top: 0;
  text-align: left;
}
li {
  display: flex;
  min-height: 50px;
  height: 50px;
  line-height: 50px;
  margin: 0.5rem 0;
  padding: 0 0.9rem;
  background: white;
  border-radius: 5px;
}
.checkBtn {
  line-height: 45px;
  color: #62acde;
  margin-right: 5px;
}
.checkBtnCompleted {
  color: #b3adad;
}
.textCompleted {
  text-decoration: line-through;
  color: #b3adad;
}
.removeBtn {
  margin-left: auto;
  color: #de4343;
}

/* transition css */
.list-enter-active, .list-leave-active {
  transition: all 1s;
}
.list-enter, .list-leave-to /* .list-leave-active below version 2.1.8 */ {
  opacity: 0;
  /* Y축으로 살짝 빠짐 */
  transform: translateY(30px);
}
</style>

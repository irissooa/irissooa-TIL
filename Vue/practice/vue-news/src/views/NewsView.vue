<template>
  <div>
   <list-item></list-item>
  </div>
</template>

<script>
import ListItem from '../components/ListItem.vue'
import ListMixin from '../mixins/ListMixin.js';

export default {
  components:{
    ListItem
  },
  mixins: [ListMixin],
  // created(){
  //   this.$emit('on:progress');
  //   this.$store.dispatch('FETCH_NEWS')
  //   .then(()=>this.$emit('off:progress'))
  //   .catch((error)=>console.error(error));
  // },  
}
</script>

<style>

</style>
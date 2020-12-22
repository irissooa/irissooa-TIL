import bus from '../utils/bus.js';
export default {
  created() {
    bus.$emit('start:spinner');
    bus.$emit('on:progress');
    this.$store.dispatch('FETCH_LIST',this.$route.name)
    .then(()=>{
      this.$emit('end:spinner')
      this.$emit('off:progress')
    }).catch(()=>console.log('fail'));
  }
}
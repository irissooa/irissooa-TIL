import ListView from './ListView.vue';
import bus from '../utils/bus.js';

export default function createListView(name) {
  return {
    name,
    mounted() {
      bus.$emit('off:progress');
      bus.$emit('end:spinner');
    },
    render(h) {
      return h(ListView);
    },
  };
}
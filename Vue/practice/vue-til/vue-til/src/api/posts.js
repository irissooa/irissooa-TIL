import { posts } from './index';

function fetchPosts() {
  return posts.get('posts');
}

function createPost(postData) {
  return posts.post('posts', postData);
}

export { fetchPosts, createPost };

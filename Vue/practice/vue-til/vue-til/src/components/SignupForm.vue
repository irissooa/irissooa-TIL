<template>
  <div class="contents">
    <div class="form-wrapper form-wrapper-sm">
      <form @submit.prevent="submitForm" class="form">
        <div>
          <label for="username">id: </label>
          <input type="text" id="username" v-model="username" />
        </div>
        <div>
          <label for="password">pw: </label>
          <input type="password" id="password" v-model="password" />
        </div>
        <div>
          <label for="nickname">nickname: </label>
          <input type="text" id="nickname" v-model="nickname" />
        </div>
        <button type="submit" class="btn">SIGNUP</button>
      </form>
      <!-- <p class="log">{{logMessage}}</p> -->
    </div>
  </div>
</template>

<script>
import { registerUser } from '@/api/index';

export default {
  data() {
    return {
      username: '',
      password: '',
      nickname: '',
      logMessage: '',
    };
  },
  methods: {
    async submitForm() {
      const userData = {
        username: this.username,
        password: this.password,
        nickname: this.nickname,
      };
      const { data } = await registerUser(userData);
      console.log(data.username);
      this.logMessage = `${data.usernmae} 님이 가입되었습니다`;
      this.initForm();
    },
    initForm() {
      (this.usernmae = ''), (this.password = ''), (this.nickname = '');
    },
  },
};
</script>

<style></style>

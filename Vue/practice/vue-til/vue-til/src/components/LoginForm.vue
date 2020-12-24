<template>
  <div class="contents">
    <div class="form-wrapper form-wrapper-sm">
      <form @submit.prevent="submitForm" class="form">
        <div>
          <label for="username">id: </label>
          <input type="text" id="username" v-model="username" />
          <p class="validation-text">
            <span class="warning" v-if="!isUsernameValid && username">
              Please enter an email address
            </span>
          </p>
        </div>
        <div>
          <label for="password">pw: </label>
          <input type="password" id="password" v-model="password" />
        </div>
        <button
          type="submit"
          class="btn"
          :disabled="!isUsernameValid || !password"
        >
          LOGIN
        </button>
      </form>
      <p class="log">{{ logMessage }}</p>
    </div>
  </div>
</template>

<script>
// import { loginUser } from '@/api/index';
import { validateEmail } from '@/utils/validation';

export default {
  data() {
    return {
      username: '',
      password: '',
      logMessage: '',
    };
  },
  computed: {
    isUsernameValid() {
      return validateEmail(this.username);
    },
  },
  methods: {
    async submitForm() {
      try {
        const userData = {
          username: this.username,
          password: this.password,
        };
        // const { data } = await loginUser(userData);
        // console.log(data.user.username);
        // this.$store.commit('setToken', data.token);
        // this.$store.commit('setUsername', data.user.username);
        await this.$store.dispatch('LOGIN', userData);
        this.$router.push('/main');
      } catch (error) {
        console.log(error.response.data);
        this.logMessage = error.response.data;
      } finally {
        this.initForm();
      }
    },
    initForm() {
      this.username = '';
      this.password = '';
    },
  },
};
</script>

<style></style>

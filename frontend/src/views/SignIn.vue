<script setup>
import { useSignIn } from '../composables/useSignIn'

const { username, password, submitForm } = useSignIn()
</script>

<template>
  <div class="sign-up">
    <h2>sign-in</h2>
    <form @submit.prevent="submitForm">
      <label>Username</label>
      <input type="email" name="username" v-model="username" /> <br />
      <label>Password</label>
      <input type="password" name="password" v-model="password" /><br />
      <input type="submit" value="Log in" />
    </form>
  </div>
</template>

<style lang="scss" scoped></style>

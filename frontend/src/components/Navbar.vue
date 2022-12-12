<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container-fluid">
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarTogglerDemo03"
        aria-controls="navbarTogglerDemo03"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <a class="navbar-brand" href="#">Викторина</a>
      <div class="collapse navbar-collapse" id="navbarTogglerDemo03">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <RouterLink to="/">Домой</RouterLink>
          </li>
        </ul>
        <div class="d-flex">
          <RouterLink to="/sign-up">Регистрация | </RouterLink>

          <template v-if="user">
            <RouterLink to="/sign-in">{{ user }}</RouterLink>
          </template>
          <template v-else>
            <RouterLink to="/sign-in">Войти</RouterLink>
          </template>
        </div>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { storeToRefs } from 'pinia'
import { useAuthStore } from '../stores/auth'

const store = useAuthStore()
const { user } = storeToRefs(store)
</script>

<style lang="scss" scoped></style>

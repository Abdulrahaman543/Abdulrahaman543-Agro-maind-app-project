<template>
  <div id="app">
    <header>
      <h1>Agro Maind</h1>
      <nav>
        <router-link to="/">Dashboard</router-link>
        <router-link to="/profile">Profile</router-link>
      </nav>
    </header>
    <main>
      <router-view />
    </main>
    <footer>
      <p>&copy; 2023 Agro Maind. All rights reserved.</p>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'App',
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

header {
  background-color: #42b983;
  padding: 20px;
  color: white;
}

nav {
  margin: 10px 0;
}

nav a {
  margin: 0 15px;
  color: white;
  text-decoration: none;
}

footer {
  margin-top: 20px;
  font-size: 12px;
}
</style>
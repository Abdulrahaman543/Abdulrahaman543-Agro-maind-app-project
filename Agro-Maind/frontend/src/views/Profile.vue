<template>
  <div class="profile">
    <h1>User Profile</h1>
    <div class="profile-details">
      <label for="username">Username:</label>
      <input type="text" id="username" v-model="user.username" disabled />

      <label for="age">Age:</label>
      <input type="number" id="age" v-model="user.age" disabled />

      <label for="country">Country:</label>
      <input type="text" id="country" v-model="user.country" disabled />

      <label for="id-number">Identification Number:</label>
      <input type="text" id="id-number" v-model="user.idNumber" disabled />
    </div>
    <button @click="editProfile">Edit Profile</button>
    <button @click="saveProfile">Save Changes</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      user: {
        username: '',
        age: null,
        country: '',
        idNumber: ''
      }
    };
  },
  methods: {
    editProfile() {
      // Logic to enable editing of profile details
    },
    saveProfile() {
      // Logic to save updated profile details
    }
  },
  mounted() {
    // Fetch user data from API and populate the user object
  }
};
</script>

<style scoped>
.profile {
  padding: 20px;
}

.profile-details {
  margin-bottom: 20px;
}

label {
  display: block;
  margin: 10px 0 5px;
}

input {
  width: 100%;
  padding: 8px;
  margin-bottom: 15px;
}

button {
  margin-right: 10px;
}
</style>
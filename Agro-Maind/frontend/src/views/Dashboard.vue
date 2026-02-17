<template>
  <div class="dashboard">
    <h1>Welcome to Agro Maind Dashboard</h1>
    <div class="dashboard-content">
      <section class="user-info">
        <h2>User Information</h2>
        <p>Name: {{ user.name }}</p>
        <p>Age: {{ user.age }}</p>
        <p>Location: {{ user.location }}</p>
      </section>
      <section class="crop-management">
        <h2>Your Crops</h2>
        <CropInspector :crops="user.crops" />
      </section>
      <section class="map-view">
        <h2>Your Location</h2>
        <MapView :location="user.location" />
      </section>
      <section class="chat-widget">
        <h2>AI Chat</h2>
        <ChatWidget />
      </section>
    </div>
  </div>
</template>

<script>
import CropInspector from '../components/CropInspector.vue';
import MapView from '../components/MapView.vue';
import ChatWidget from '../components/ChatWidget.vue';

export default {
  name: 'Dashboard',
  components: {
    CropInspector,
    MapView,
    ChatWidget,
  },
  data() {
    return {
      user: {
        name: 'John Doe',
        age: 30,
        location: { lat: 0, lng: 0 },
        crops: [],
      },
    };
  },
  mounted() {
    this.fetchUserData();
  },
  methods: {
    fetchUserData() {
      // Fetch user data from the backend API
      // This is a placeholder for the actual API call
      this.user.crops = [
        { id: 1, name: 'Wheat', growthStage: 'Harvest' },
        { id: 2, name: 'Corn', growthStage: 'Growing' },
      ];
      this.user.location = { lat: 12.9716, lng: 77.5946 }; // Example coordinates
    },
  },
};
</script>

<style scoped>
.dashboard {
  padding: 20px;
}

.dashboard-content {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.user-info, .crop-management, .map-view, .chat-widget {
  border: 1px solid #ccc;
  padding: 15px;
  border-radius: 8px;
}
</style>
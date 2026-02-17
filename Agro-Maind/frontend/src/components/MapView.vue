<template>
  <div class="map-view">
    <h2>Your Location</h2>
    <div id="map" ref="map" class="map-container"></div>
  </div>
</template>

<script>
export default {
  name: 'MapView',
  data() {
    return {
      map: null,
      userLocation: null,
    };
  },
  mounted() {
    this.initializeMap();
    this.getUserLocation();
  },
  methods: {
    initializeMap() {
      this.map = new google.maps.Map(this.$refs.map, {
        center: { lat: 0, lng: 0 },
        zoom: 2,
      });
    },
    getUserLocation() {
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
          (position) => {
            this.userLocation = {
              lat: position.coords.latitude,
              lng: position.coords.longitude,
            };
            this.updateMapLocation();
          },
          () => {
            alert('Unable to retrieve your location.');
          }
        );
      } else {
        alert('Geolocation is not supported by this browser.');
      }
    },
    updateMapLocation() {
      if (this.userLocation) {
        this.map.setCenter(this.userLocation);
        new google.maps.Marker({
          position: this.userLocation,
          map: this.map,
          title: 'You are here!',
        });
      }
    },
  },
};
</script>

<style scoped>
.map-container {
  height: 400px;
  width: 100%;
}
</style>
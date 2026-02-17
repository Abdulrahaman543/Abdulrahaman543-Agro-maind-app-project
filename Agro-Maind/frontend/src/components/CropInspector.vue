<template>
  <div class="crop-inspector">
    <h2>Crop Inspector</h2>
    <form @submit.prevent="submitCropData">
      <div class="form-group">
        <label for="cropName">Crop Name:</label>
        <input type="text" v-model="cropName" id="cropName" required />
      </div>
      <div class="form-group">
        <label for="growthStage">Growth Stage:</label>
        <select v-model="growthStage" id="growthStage" required>
          <option value="" disabled>Select Growth Stage</option>
          <option value="germination">Germination</option>
          <option value="vegetative">Vegetative</option>
          <option value="flowering">Flowering</option>
          <option value="harvest">Harvest</option>
        </select>
      </div>
      <div class="form-group">
        <label for="pestIssues">Pest Issues:</label>
        <textarea v-model="pestIssues" id="pestIssues" placeholder="Describe any pest issues..."></textarea>
      </div>
      <div class="form-group">
        <label for="diseaseIssues">Disease Issues:</label>
        <textarea v-model="diseaseIssues" id="diseaseIssues" placeholder="Describe any disease issues..."></textarea>
      </div>
      <button type="submit">Submit</button>
    </form>
    <div v-if="responseMessage" class="response-message">{{ responseMessage }}</div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      cropName: '',
      growthStage: '',
      pestIssues: '',
      diseaseIssues: '',
      responseMessage: ''
    };
  },
  methods: {
    async submitCropData() {
      try {
        const response = await fetch('/api/v1/crops', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            cropName: this.cropName,
            growthStage: this.growthStage,
            pestIssues: this.pestIssues,
            diseaseIssues: this.diseaseIssues
          })
        });
        const data = await response.json();
        this.responseMessage = data.message || 'Crop data submitted successfully!';
      } catch (error) {
        this.responseMessage = 'Error submitting crop data. Please try again.';
      }
    }
  }
};
</script>

<style scoped>
.crop-inspector {
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
.form-group {
  margin-bottom: 15px;
}
label {
  display: block;
  margin-bottom: 5px;
}
input, select, textarea {
  width: 100%;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
}
button {
  padding: 10px 15px;
  background-color: #28a745;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
button:hover {
  background-color: #218838;
}
.response-message {
  margin-top: 15px;
  color: #d9534f;
}
</style>
<template>
  <div class="chat-widget">
    <div class="chat-header">
      <h3>Agro Maind Chat</h3>
    </div>
    <div class="chat-body" ref="chatBody">
      <div v-for="message in messages" :key="message.id" class="chat-message" :class="{ 'user-message': message.isUser }">
        <p>{{ message.text }}</p>
      </div>
    </div>
    <div class="chat-input">
      <input v-model="userInput" @keyup.enter="sendMessage" placeholder="Type your message..." />
      <button @click="sendMessage">Send</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      userInput: '',
      messages: [],
    };
  },
  methods: {
    async sendMessage() {
      if (this.userInput.trim() === '') return;

      this.messages.push({ id: Date.now(), text: this.userInput, isUser: true });
      const response = await this.getAIResponse(this.userInput);
      this.messages.push({ id: Date.now() + 1, text: response, isUser: false });
      this.userInput = '';
      this.$nextTick(() => {
        this.$refs.chatBody.scrollTop = this.$refs.chatBody.scrollHeight;
      });
    },
    async getAIResponse(message) {
      try {
        const response = await fetch('http://localhost:8000/api/v1/ai_chat', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ message }),
        });
        const data = await response.json();
        return data.reply;
      } catch (error) {
        console.error('Error fetching AI response:', error);
        return 'Sorry, I could not get a response.';
      }
    },
  },
};
</script>

<style scoped>
.chat-widget {
  border: 1px solid #ccc;
  border-radius: 5px;
  width: 300px;
  max-height: 400px;
  display: flex;
  flex-direction: column;
}

.chat-header {
  background-color: #4caf50;
  color: white;
  padding: 10px;
  text-align: center;
}

.chat-body {
  flex: 1;
  padding: 10px;
  overflow-y: auto;
}

.chat-message {
  margin: 5px 0;
}

.user-message {
  text-align: right;
}

.chat-input {
  display: flex;
  padding: 10px;
}

.chat-input input {
  flex: 1;
  padding: 5px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.chat-input button {
  margin-left: 5px;
  padding: 5px 10px;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
</style>
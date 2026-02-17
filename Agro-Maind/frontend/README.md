# Agro Maind Frontend Documentation

## Overview
Agro Maind is an innovative agriculture application designed to assist farmers and agricultural enthusiasts with AI-driven insights, user authentication, and location-based services. This frontend documentation provides guidance on setting up and using the frontend components of the application.

## Project Structure
The frontend of Agro Maind is built using Vue.js and consists of the following key components:

- **src/**: Contains the source code for the application.
  - **main.js**: The entry point of the Vue.js application.
  - **App.vue**: The root component of the application.
  - **components/**: Contains reusable components such as:
    - **ChatWidget.vue**: A chat interface for interacting with the AI.
    - **LoginForm.vue**: A form for user authentication.
    - **MapView.vue**: Displays the user's location on a map.
    - **CropInspector.vue**: A component for managing and inspecting crops.
  - **views/**: Contains different views of the application:
    - **Dashboard.vue**: The main dashboard view for users.
    - **Profile.vue**: The user profile view.
  - **assets/**: Contains static assets like stylesheets.
    - **styles.css**: The main stylesheet for the application.
- **public/**: Contains the public assets of the application.
  - **index.html**: The main HTML file for the application.
- **package.json**: The configuration file for npm, listing dependencies and scripts.
- **README.md**: This documentation file.

## Setup Instructions
1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd Agro-Maind/frontend
   ```

2. **Install Dependencies**
   Make sure you have Node.js and npm installed. Then run:
   ```bash
   npm install
   ```

3. **Run the Application**
   To start the development server, use:
   ```bash
   npm run serve
   ```

4. **Access the Application**
   Open your browser and navigate to `http://localhost:8080` to view the application.

## Features
- **AI Chat Feature**: Interact with an AI chatbot for agricultural advice and insights.
- **User Authentication**: Secure login and registration process for users.
- **Location Checks**: Verify user location to provide relevant agricultural information.

## Contribution
Contributions to the Agro Maind project are welcome! Please follow the standard Git workflow for contributing.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
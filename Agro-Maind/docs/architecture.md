# Architecture of Agro Maind

## Overview
Agro Maind is a comprehensive agriculture application designed to assist farmers and agricultural enthusiasts with various features, including AI chat support, user validation, and location checks. The application is structured into two main components: the backend and the frontend, ensuring a clear separation of concerns.

## Backend Architecture
The backend is built using FastAPI, a modern web framework for building APIs with Python. It is organized into several modules:

- **Main Application**: The entry point of the application is located in `main.py`, where the FastAPI app is initialized and API routes are set up.

- **API Endpoints**:
  - **AI Chat**: Located in `api/v1/ai_chat.py`, this module handles AI interactions, providing endpoints for text and voice communication in multiple languages.
  - **Authentication**: The `api/v1/auth.py` module manages user registration and login, including validation of user details such as age and identification number.
  - **Location Management**: The `api/v1/location.py` module ensures that users are in the correct geographical area for app usage.
  - **Crop Management**: The `api/v1/crops.py` module provides endpoints related to crop information and management.

- **Core Services**:
  - **Configuration**: The `core/config.py` file contains application settings, including environment variables and API keys.
  - **Security**: The `core/security.py` module includes functions for password hashing and token generation.

- **Data Models**:
  - **User Model**: Defined in `models/user.py`, this model includes properties for username, age, country, and identification number.
  - **Crop Model**: The `models/crop.py` file defines properties related to crop types and growth conditions.

- **Schemas**: The `schemas/index.py` file contains Pydantic schemas for data validation and serialization of user and crop data.

- **Services**:
  - **AI Service**: The `services/ai_service.py` module contains logic for AI interactions, including language processing and response generation.
  - **Validation Service**: The `services/validation_service.py` module includes functions for validating user input.
  - **Location Service**: The `services/location_service.py` module manages location validation logic.

- **Utilities**: The `utils/design_helpers.py` file contains utility functions for design elements and UI helpers.

## Frontend Architecture
The frontend is built using Vue.js, a progressive JavaScript framework for building user interfaces. It is organized as follows:

- **Entry Point**: The application is initialized in `src/main.js`, where the Vue instance is created.

- **Main Component**: The root component of the application is `src/App.vue`, which serves as the main layout.

- **Components**:
  - **Chat Widget**: The `components/ChatWidget.vue` file contains the chat widget for user interactions with the AI.
  - **Login Form**: The `components/LoginForm.vue` file provides the login form for user authentication.
  - **Map View**: The `components/MapView.vue` file displays the user's location on a map.
  - **Crop Inspector**: The `components/CropInspector.vue` file allows users to inspect and manage crops.

- **Views**:
  - **Dashboard**: The `views/Dashboard.vue` file represents the dashboard view for users after logging in.
  - **Profile**: The `views/Profile.vue` file represents the user profile view.

- **Assets**: The `assets/styles.css` file contains the styles for the frontend application.

## Deployment
The application can be containerized using Docker. The Dockerfiles for both the backend and frontend are located in the `docker` directory, and the `docker-compose.yml` file defines the services and configurations for running the application.

## Conclusion
Agro Maind aims to provide a user-friendly experience for farmers by integrating advanced technologies such as AI and location services, ensuring that users have access to the information and tools they need to succeed in agriculture.
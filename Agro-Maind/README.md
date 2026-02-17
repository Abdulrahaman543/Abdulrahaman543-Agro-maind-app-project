# Agro Maind

Agro Maind is an innovative agriculture application designed to assist farmers and agricultural enthusiasts with various features, including AI chat support, user validation, and location checks. The application aims to enhance productivity and provide valuable insights into crop management.

## Project Structure

The project is divided into two main components: the backend and the frontend.

### Backend

The backend is built using FastAPI and includes the following key components:

- **API Endpoints**: 
  - `ai_chat.py`: Handles AI chat functionality for user interactions.
  - `auth.py`: Manages user authentication, including registration and login.
  - `location.py`: Validates user location to ensure compliance with geographical restrictions.
  - `crops.py`: Provides endpoints for crop information and management.

- **Core Services**:
  - `config.py`: Contains configuration settings and environment variables.
  - `security.py`: Implements security features such as password hashing and token generation.

- **Models**:
  - `user.py`: Defines the User model with properties like username, age, and identification number.
  - `crop.py`: Defines the Crop model with properties related to crop types and growth conditions.

- **Schemas**:
  - `index.py`: Contains Pydantic schemas for data validation and serialization.

- **Services**:
  - `ai_service.py`: Manages AI interactions and response generation.
  - `validation_service.py`: Validates user input.
  - `location_service.py`: Handles location validation logic.

- **Utilities**:
  - `design_helpers.py`: Provides utility functions for design elements and UI helpers.

### Frontend

The frontend is built using Vue.js and includes the following components:

- **Main Application**:
  - `main.js`: Entry point for the Vue.js application.
  - `App.vue`: Root component of the application.

- **User Interface Components**:
  - `ChatWidget.vue`: Chat widget for AI interactions.
  - `LoginForm.vue`: Login form for user authentication.
  - `MapView.vue`: Displays user location on a map.
  - `CropInspector.vue`: Component for inspecting and managing crops.

- **Views**:
  - `Dashboard.vue`: User dashboard after logging in.
  - `Profile.vue`: User profile view.

- **Assets**:
  - `styles.css`: Styles for the frontend application.

## Installation

To set up the project, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd Agro-Maind
   ```

2. Set up the backend:
   - Navigate to the `backend` directory.
   - Install dependencies:
     ```
     pip install -r requirements.txt
     ```
   - Run the backend server:
     ```
     uvicorn app.main:app --reload
     ```

3. Set up the frontend:
   - Navigate to the `frontend` directory.
   - Install dependencies:
     ```
     npm install
     ```
   - Run the frontend application:
     ```
     npm run serve
     ```

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
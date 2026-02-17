# Agro Maind Backend Documentation

## Overview
Agro Maind is an agriculture application designed to assist farmers and agricultural enthusiasts with various features, including AI chat support, user validation, and location checks. This backend documentation provides an overview of the backend setup, usage, and API endpoints.

## Project Structure
The backend is structured as follows:

```
backend/
├── app/
│   ├── main.py                # Entry point of the application
│   ├── api/
│   │   └── v1/
│   │       ├── ai_chat.py     # AI chat functionality
│   │       ├── auth.py        # User authentication
│   │       ├── location.py     # Location management
│   │       └── crops.py       # Crop information management
│   ├── core/
│   │   ├── config.py          # Configuration settings
│   │   └── security.py        # Security functions
│   ├── models/
│   │   ├── user.py            # User model
│   │   └── crop.py            # Crop model
│   ├── schemas/
│   │   └── index.py           # Data validation schemas
│   ├── services/
│   │   ├── ai_service.py      # AI interaction logic
│   │   ├── validation_service.py # User input validation
│   │   └── location_service.py # Location validation logic
│   └── utils/
│       └── design_helpers.py   # Design utility functions
├── tests/
│   ├── test_auth.py           # Unit tests for authentication
│   ├── test_ai_chat.py        # Unit tests for AI chat
│   └── test_location.py       # Unit tests for location validation
├── requirements.txt           # Backend dependencies
└── README.md                  # This documentation
```

## Setup Instructions
1. **Clone the Repository**
   ```
   git clone <repository-url>
   cd Agro-Maind/backend
   ```

2. **Install Dependencies**
   It is recommended to use a virtual environment. You can create one using:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
   Then install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. **Configuration**
   Update the configuration settings in `core/config.py` with your environment variables and API keys.

4. **Run the Application**
   Start the FastAPI application:
   ```
   uvicorn app.main:app --reload
   ```

## API Endpoints
The backend provides several API endpoints for different functionalities:

- **AI Chat**
  - `/api/v1/ai_chat` - Interact with the AI chat feature.

- **Authentication**
  - `/api/v1/auth/register` - Register a new user.
  - `/api/v1/auth/login` - Log in an existing user.

- **Location**
  - `/api/v1/location/check` - Validate user location.

- **Crops**
  - `/api/v1/crops` - Manage crop information.

## Testing
To run the tests, ensure you have installed the necessary testing libraries and run:
```
pytest tests/
```

## Contribution
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
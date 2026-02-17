from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1 import ai_chat, auth, location, crops

app = FastAPI()

# CORS middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update with your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(ai_chat.router, prefix="/api/v1/ai_chat", tags=["AI Chat"])
app.include_router(auth.router, prefix="/api/v1/auth", tags=["Authentication"])
app.include_router(location.router, prefix="/api/v1/location", tags=["Location"])
app.include_router(crops.router, prefix="/api/v1/crops", tags=["Crops"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Agro Maind API"}
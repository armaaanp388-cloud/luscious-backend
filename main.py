from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Ye setting Vercel (Frontend) ko is Backend se baat karne ki permission deti hai
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Appointment(BaseModel):
    name: str
    phone: str
    service: str
    date: str

@app.post("/api/appointments")
async def create_appointment(appointment: Appointment):
    # Abhi ke liye hum data ko sirf successful return kar rahe hain. 
    # Jab aap MongoDB banayenge, toh data yahan save hoga.
    return {"status": "success", "message": "Booking confirmed!"}

@app.get("/")
async def root():
    return {"message": "Luscious Salon Backend is running perfectly!"}
  

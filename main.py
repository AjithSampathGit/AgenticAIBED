from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

class UserRequest(BaseModel):
    session_id: str
    timestamp: str
    step: str

@app.post("/evaluate")
def evaluate(request: UserRequest):
    options = [
        {"status": "agent_handoff", "message": "We’re connecting you to a live agent..."},
        {"status": "schedule", "message": "Please schedule a session with a banker.", "appointment_link": f"https://bank.com/schedule/{request.session_id}"},
        {"status": "save_and_resume", "message": "Your application has been saved. You can resume later using this session ID."},
    ]
    return {**random.choice(options), "session_id": request.session_id}

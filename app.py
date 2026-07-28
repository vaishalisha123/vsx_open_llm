from fastapi import FastAPI
from pydantic import BaseModel
from llm import generate_response
app= FastAPI()
@app.get("/")
def home():
    return{"message": "Open LLM is running"}

class UserMessage(BaseModel):
    message: str

@app.post("/chat")
def chat(request: UserMessage):
    reply= generate_response(user_message= request.message)
    return {"reply": reply}
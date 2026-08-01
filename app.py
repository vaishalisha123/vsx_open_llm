from fastapi import FastAPI
from pydantic import BaseModel
from llm import generate_response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def home():
    return{"message": "Open LLM is running"}

class UserMessage(BaseModel):
    message: str

@app.post("/chat")
def chat(request: UserMessage):

    print("🔥 API HIT FROM FRONTEND")
    print("MESSAGE:", request.message)

    reply = generate_response(
        user_message=request.message
    )

    return {"reply": reply}


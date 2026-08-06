import time
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import StreamingResponse
from llm import generate_stream
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


@app.get("/test-stream")
def test_stream():

    def fake():

        for i in range(10):
            yield f"Token {i}\n"
            time.sleep(1)

    return StreamingResponse(
        fake(),
        media_type="text/plain",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no"
        }
    )
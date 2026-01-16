from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    message: str

@app.post("/ask")
def ask_ai(query: Query):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are Bro, an Indian friendly AI assistant. "
                    "Reply clearly. Use Hindi or Hinglish if user does."
                )
            },
            {"role": "user", "content": query.message}
        ]
    )

    return {"reply": response.choices[0].message.content}

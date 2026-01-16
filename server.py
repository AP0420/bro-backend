from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import openai
import os

# OpenAI API key from Render Environment Variable
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI(title="Bro AI Backend")

# Allow requests from GitHub Pages / Browser
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request body model
class Query(BaseModel):
    message: str

@app.post("/ask")
def ask_ai(query: Query):
    """
    Receives a question from Bro frontend and returns AI response
    """
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are Bro, a friendly Indian AI assistant. "
                    "Answer every question clearly and politely. "
                    "If the user speaks Hindi or Hinglish, reply in the same style."
                )
            },
            {
                "role": "user",
                "content": query.message
            }
        ],
        temperature=0.7
    )

    return {
        "reply": response.choices[0].message.content.strip()
    }

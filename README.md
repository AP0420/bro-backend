# Bro Backend 🤖

This is the AI backend for **Bro**, a voice-based personal assistant.

## Features
- Answers any question using OpenAI
- Supports English, Hindi, and Hinglish
- Built with FastAPI
- Designed for deployment on Render

## Endpoint
POST `/ask`

### Request
```json
{
  "message": "Explain artificial intelligence"
}

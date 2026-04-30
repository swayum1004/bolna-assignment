from fastapi import FastAPI, Request
import requests
import os
from dotenv import load_dotenv
import uvicorn

load_dotenv()
app = FastAPI()

SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()

    # Extract required fields
    call_id = data.get("id", "N/A")
    agent_id = data.get("agent_id", "N/A")
    status = data.get("status", "")

    # Only process completed calls
    if status != "completed":
        return {"status": "ignored"}

    telephony = data.get("telephony_data") or {}
    duration = telephony.get("duration", "N/A")

    transcript = data.get("transcript", "No transcript")

    # Slack message
    message = {
        "text": f"""📞 Call Ended

        ID: {call_id}
        Agent ID: {agent_id}
        Duration: {duration} seconds

        Transcript:
        {transcript}
        """
    }

    # Send to Slack
    requests.post(SLACK_WEBHOOK_URL, json=message)
    return {"status": "sent"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=10000)
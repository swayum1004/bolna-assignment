# 🚀 Bolna → Slack Integration

## 📌 Overview

This project implements a webhook-based integration that sends a Slack alert whenever a call handled by a Bolna AI agent is completed.

The system receives execution data from Bolna via a webhook, extracts relevant details, and forwards them to Slack in a structured format.

---

## 🎯 Features

* Receives webhook events from Bolna after call completion
* Extracts key fields:

  * Call ID
  * Agent ID
  * Duration
  * Transcript
* Sends formatted message to Slack
* Handles real-time event-driven architecture

---

## 🧩 Architecture

```
Bolna → FastAPI Webhook → Slack
```

1. Bolna sends a POST request after a call ends
2. FastAPI backend processes the payload
3. Relevant data is extracted
4. Message is sent to Slack via webhook

---

## ⚙️ Tech Stack

* Python (FastAPI)
* Requests (HTTP client)
* Render (Deployment)
* Slack Incoming Webhooks

---

## 📁 Project Structure

```
bolna-integration/
│
├── main.py
├── requirements.txt
├── .env.example
└── README.md
```

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repo-link>
cd bolna-integration
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Configure Environment Variables

Create a `.env` file:

```env
SLACK_WEBHOOK_URL=your_slack_webhook_url_here
```

---

### 4. Run the Server

```bash
uvicorn main:app --reload
```

Server will run at:

```
http://127.0.0.1:8000
```

---

## 🌍 Deployment (Render)

The application is deployed on:

```
https://bolna-assignment-enda.onrender.com/webhook
```

### Deployment Steps:

1. Push code to GitHub
2. Create a Web Service on Render
3. Set:

   * Build Command: `pip install -r requirements.txt`
   * Start Command: `uvicorn main:app --host 0.0.0.0 --port 10000`
4. Add environment variable:

   * `SLACK_WEBHOOK_URL`

---

## 🔗 Bolna Configuration

Using the Bolna dashboard:

1. Open your agent
2. Navigate to **Analytics -> Post Call Tasks**
3. Add webhook URL:

```
https://bolna-assignment-enda.onrender.com/webhook
```

4. Save changes

---

## 🧪 Testing

### 1. Using Postman

* Method: POST
* URL: `/webhook`

```json
{
  "id": "test123",
  "agent_id": "agent007",
  "status": "completed",
  "transcript": "Hello test",
  "telephony_data": {
    "duration": 30
  }
}
```

---

### 2. Using Bolna

1. Trigger a call using your agent
2. Wait for call completion
3. Backend receives webhook
4. Slack message is generated

---

## 📥 Sample Output (Slack)

```
📞 Call Ended

        ID: 9f420622-6759-40ae-8f90-da84a8addbe3
        Agent ID: ec7bda27-4c0f-4598-943c-83cad17d919f
        Duration: 91 seconds

        Transcript:
        assistant: Hi, this is a demo call from Bolna
user:  hello how are you
assistant:  Hello! I'm doing well, thank you. How can I assist you today?
user:  can you get me in all info about school
assistant:  Certainly! Could you please specify which school you are interested in? This will help me provide you with the most accurate and detailed information.
user:  what are the elements being used by bona
assistant:  It seems like you are asking about the elements used by "Bona." Could you please clarify if you are referring to a company, product, or something else named Bona? This will help me provide the correct information.
user:  you please clarify if you are the same to
assistant:  I am an AI assistant here to help you with your questions. If you are asking whether I am affiliated with Bona or any specific company, I am not. I am here to provide information and assistance based on your queries. How can I assist you further?
user:  what are the llms being used by bola
assistant:  It seems like you are asking about the Learning Management Systems (LMS) being used by "Bola." Could you please confirm if you are referring to a specific organization or platform named Bola? Providing a bit more context will help me give you accurate information.
user:  thank you for your assistance
assistant:  You're welcome! If you have any more questions or need further assistance, feel free to ask. Have a great day!
user:  thank you
assistant:  You're very welcome! Have a wonderful day!
```

---

## ⚠️ Notes

* Only calls with `status = completed` are processed
* Duration is extracted from `telephony_data.duration`
* Ensure Slack webhook URL is valid
* Render free tier may introduce slight cold-start delay

---

## 🧠 Key Concepts Demonstrated

* Webhooks and event-driven systems
* API integration (Bolna + Slack)
* Backend deployment
* JSON payload parsing
* Real-world debugging and testing

---

## 👤 Author

**Swayum Hastwala**

---

## 📄 License

This project is submitted as part of an assignment for Bolna.

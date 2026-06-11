# Mental Health Chatbot

## Overview

Mental Health Chatbot is an AI-powered conversational assistant designed to provide emotional support, stress management guidance, and practical coping strategies. The chatbot uses Google's Gemini model through LangChain and includes Langfuse observability for tracing, monitoring, and evaluation.

## Features

* Emotion detection from user messages
* Empathetic and supportive responses
* Practical coping strategies and self-care suggestions
* Crisis keyword detection for user safety
* Langfuse tracing and observability
* Streamlit-based interactive chat interface
* Gemini-powered natural language responses

## Tech Stack

* Python
* Streamlit
* LangChain
* Google Gemini API
* Langfuse
* python-dotenv

## Project Structure

```text
Mental-Health-Chatbot/
│
├── app.py
├── lang.py
├── .gitignore
└── README.md
```

## Installation

1. Clone the repository

```bash
git clone https://github.com/Adepuharshavardhan2001/Mental-Health-Chatbot.git
cd Mental-Health-Chatbot
```

2. Create a virtual environment

```bash
python -m venv venv
```

3. Activate the environment

Windows:

```bash
venv\Scripts\activate
```

4. Install dependencies

```bash
pip install -r requirements.txt
```

5. Create a .env file

```env
GOOGLE_API_KEY=your_google_api_key
LANGFUSE_PUBLIC_KEY=your_public_key
LANGFUSE_SECRET_KEY=your_secret_key
LANGFUSE_BASE_URL=https://us.cloud.langfuse.com
```

## Run the Application

```bash
streamlit run app.py
```

## Langfuse Integration

This project integrates Langfuse for:

* Trace monitoring
* Prompt management
* Dataset evaluation
* Response quality analysis
* Observability of LLM interactions

## Safety Features

* Detects crisis-related keywords
* Encourages professional support when necessary
* Avoids medical diagnosis
* Avoids medication recommendations

## Future Improvements

* Multi-language support
* Voice-based interaction
* Sentiment analytics dashboard
* Advanced evaluation pipelines
* Personalized wellness recommendations

## Author

Harsha Vardhan

## License

This project is developed for learning and educational purposes.


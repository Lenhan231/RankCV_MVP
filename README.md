# RankCV MVP

An intelligent API built with FastAPI and Google Gemini to evaluate CV-JD compatibility and generate FPT-culture technical interview questions.

## 🚀 Features

- **CV-JD Matching (`/evaluate`)**: Analyzes candidate CV against Job Descriptions to provide match scores, missing skills, and recommendations.
- **Interview Questions (`/interview-questions`)**: Generates 5 technical interview questions tailored to FPT culture based on candidate skills.

## 💻 Quick Start

### 1. Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Create .env and add your Gemini API Key
# Example: GEMINI_API_KEY=your_api_key_here

# Run the server
uvicorn app.main:app --reload --env-file .env
```
Server runs at `http://localhost:8000`. Interactive API docs are at `http://localhost:8000/docs`.

### 2. Vercel Deployment

This project is configured for Vercel deployment. 
1. Connect your GitHub repository to Vercel.
2. Add `GEMINI_API_KEY` to the Environment Variables section.
3. Deploy! Vercel will automatically host the FastAPI application using the provided `vercel.json`.

## 🔌 API Endpoints

### 1. Evaluate Match
`POST /evaluate`
```bash
curl -X POST "http://localhost:8000/evaluate" \
  -H "Content-Type: application/json" \
  -d '{"cv_text": "Candidate CV...", "job_text": "Job Description..."}'
```

### 2. Generate Interview Questions
`POST /interview-questions`
```bash
curl -X POST "http://localhost:8000/interview-questions" \
  -H "Content-Type: application/json" \
  -d '{"cv_text": "Candidate CV...", "job_text": "Job Description..."}'
```

## 🛠️ Tech Stack

- **Python 3.8+**
- **FastAPI** & **Uvicorn**
- **Pydantic**
- **Google GenAI** (Gemini)
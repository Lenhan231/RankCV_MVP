# app.py
import os
import json
from typing import List
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, conint
from google import genai
from google.genai import types

app = FastAPI(title="CV-JD Match API")

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))  # or rely on env var

class MatchRequest(BaseModel):
    cv_text: str = Field(..., min_length=50)
    job_text: str = Field(..., min_length=50)

class MatchResponse(BaseModel):
    overall_score: conint(ge=0, le=100)
    skill_match: conint(ge=0, le=100)
    experience_match: conint(ge=0, le=100)
    education_match: conint(ge=0, le=100)
    missing_skills: List[str]
    strengths: List[str]
    recommendation: str

@app.post("/evaluate")
def evaluate(req: MatchRequest):
    prompt = f"""You are a resume-job matching engine. Analyze the CV and job description below and return ONLY valid JSON (no markdown, no code blocks, no extra text).

Return JSON with these fields:
- overall_score: integer 0-100
- skill_match: integer 0-100
- experience_match: integer 0-100
- education_match: integer 0-100
- missing_skills: list of skill names as strings
- strengths: list of strength descriptions as strings
- recommendation: one sentence recommendation as string

CV:
{req.cv_text}

JOB DESCRIPTION:
{req.job_text}

RESPONSE (JSON ONLY):"""

    try:
        response = client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=MatchResponse,
            ),
        )

        # Validate and return as pure JSON
        validated = MatchResponse.model_validate_json(response.text)
        return JSONResponse(content=json.loads(validated.model_dump_json()))

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
# app/gemini_client.py
import os

from google import genai
from google.genai import types

from app.schemas import (
    MatchRequest,
    MatchData,
    InterviewQuestionsRequest,
    InterviewQuestionsResponse,
)

MODEL = "gemini-3.1-flash-lite"

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def build_prompt(req: MatchRequest) -> str:
    return f"""You are a resume-job matching engine. Analyze the CV, job description, and other context below to return ONLY valid JSON.

Return a detailed match analysis including:
- overall_score, skill_match, experience_match, education_match: integer scores 0-100
- current_cv_summary: A brief summary of the CV
- skills, experience, projects: Extracted lists
- skill_gap_analysis: Detailed gap analysis (overall verdict, strengths, weaknesses, missing skills, role match level, growth suggestions, mentor note)
- career_alignment: Career goal feasibility and next steps
- cultural_fit: Cultural alignment score (0-100), core values match, culture gaps, and work style compatibility. IMPORTANT: Evaluate this based on your knowledge of the specific company culture if COMPANY NAME is provided, otherwise infer from the job description.

CV:
{req.cv_text}

JOB DESCRIPTION:
{req.job_text}

COMPANY NAME: {req.company_name or "Not specified"}
TARGET ROLE: {req.target_role or "Not specified"}
CAREER GOAL: {req.career_goal or "Not specified"}

RESPONSE (JSON ONLY):"""


def evaluate_match(req: MatchRequest) -> MatchData:
    """Call Gemini and return a validated MatchData."""
    response = client.models.generate_content(
        model=MODEL,
        contents=build_prompt(req),
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=MatchData,
        ),
    )
    return MatchData.model_validate_json(response.text)



def build_interview_prompt(req: InterviewQuestionsRequest) -> str:
    return f"""You are a senior technical interviewer at FPT (including FPT Software, FPT Telecom).
Your task is to generate exactly 5 technical interview questions for a candidate based on their CV and the Job Description.

Guidelines:
1. Questions must be strictly technical and based on the intersection of skills found in the candidate's CV and the Job Description (e.g., Docker, Spring Boot).
2. The style and difficulty should match FPT's interview culture: focus on practical application, problem-solving, real-world project experience, and a strong willingness to learn.
3. Be safe and factual: Do NOT hallucinate skills that the candidate does not have or the job does not require.
4. Provide a suggested answer for each question to help the candidate prepare.
5. Return ONLY valid JSON (no markdown, no code blocks, no extra text).

Return JSON matching this schema:
- questions: list of objects containing:
  - skill_tag: string (e.g., "Docker", "Java")
  - question: string (the interview question)
  - suggested_answer: string (brief suggested answer)

CV:
{req.cv_text}

JOB DESCRIPTION:
{req.job_text}

RESPONSE (JSON ONLY):"""


def generate_interview_questions(req: InterviewQuestionsRequest) -> InterviewQuestionsResponse:
    """Call Gemini to generate interview questions and return validated response."""
    response = client.models.generate_content(
        model=MODEL,
        contents=build_interview_prompt(req),
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=InterviewQuestionsResponse,
        ),
    )
    return InterviewQuestionsResponse.model_validate_json(response.text)

import json
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from app.gemini_client import generate_interview_questions
from app.schemas import InterviewQuestionsRequest, InterviewQuestionsResponse

router = APIRouter(tags=["interview"])

@router.post("/interview-questions", response_model=InterviewQuestionsResponse)
def generate_questions(req: InterviewQuestionsRequest):
    try:
        return generate_interview_questions(req)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

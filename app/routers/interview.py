import json
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from app.gemini_client import generate_interview_questions
from app.schemas import InterviewQuestionsRequest

router = APIRouter(tags=["interview"])

@router.post("/interview-questions")
def generate_questions(req: InterviewQuestionsRequest):
    try:
        validated = generate_interview_questions(req)
        return JSONResponse(content=json.loads(validated.model_dump_json()))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

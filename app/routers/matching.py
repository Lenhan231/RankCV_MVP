import json
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from app.gemini_client import evaluate_match
from app.schemas import MatchRequest, MatchResponse

router = APIRouter(tags=["matching"])

@router.post("/evaluate", response_model=MatchResponse)
def evaluate(req: MatchRequest):
    try:
        return evaluate_match(req)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

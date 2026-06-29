from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from app.schemas import MatchRequest, MatchResponse
from app.services.matching_service import evaluate_cv_match

router = APIRouter(tags=["matching"])


@router.post("/evaluate", response_model=MatchResponse)
def evaluate(req: MatchRequest):
    try:
        response = evaluate_cv_match(req)
        return response

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
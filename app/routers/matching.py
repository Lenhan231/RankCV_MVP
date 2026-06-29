import hashlib
from datetime import datetime, timezone
from fastapi import APIRouter, HTTPException

from app.gemini_client import evaluate_match
from app.schemas import MatchRequest, MatchResponse

router = APIRouter(tags=["matching"])

@router.post("/evaluate", response_model=MatchResponse)
def evaluate(req: MatchRequest):
    try:
        hash_input = f"{req.cv_text}{req.job_text}{req.company_name or ''}{req.tier or ''}{req.target_role or ''}{req.career_goal or ''}"
        content_hash = hashlib.sha256(hash_input.encode('utf-8')).hexdigest()
        
        match_data = evaluate_match(req)
        
        return MatchResponse(
            status="success",
            source="ai",
            content_hash=content_hash,
            cached_at=datetime.now(timezone.utc).isoformat(),
            data=match_data
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


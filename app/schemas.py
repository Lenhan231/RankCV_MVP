# app/schemas.py
from typing import List

from pydantic import BaseModel, Field, conint


class MatchRequest(BaseModel):
    cv_text: str = Field(..., min_length=50)
    job_text: str = Field(..., min_length=50)
    company_name: str | None = None
    tier: str | None = None
    target_role: str | None = None
    career_goal: str | None = None


class CandidateFptFit(BaseModel):
    fit_level: str
    matched_culture_points: List[str]
    missing_culture_points: List[str]
    fit_explanation: str


class CvImprovementAdvice(BaseModel):
    strengths_to_highlight: List[str]
    weaknesses_to_fix: List[str]
    keywords_to_add: List[str]
    rewrite_suggestions: List[str]


class CareerAdvice(BaseModel):
    readiness_level: str
    recommended_next_steps: List[str]
    estimated_timeline: str


class MatchData(BaseModel):
    current_cv_summary: str
    fpt_culture_intro: str
    fpt_strengths: List[str]
    candidate_fpt_fit: CandidateFptFit
    cv_improvement_advice: CvImprovementAdvice
    career_advice: CareerAdvice
    mentor_note: str


class MatchResponse(BaseModel):
    status: str = "success"
    source: str = "ai"
    content_hash: str | None = None
    cached_at: str | None = None
    data: MatchData


class InterviewQuestionsRequest(BaseModel):
    cv_text: str = Field(..., min_length=50)
    job_text: str = Field(..., min_length=50)


class InterviewQuestion(BaseModel):
    skill_tag: str
    question: str
    suggested_answer: str


class InterviewQuestionsResponse(BaseModel):
    questions: List[InterviewQuestion]

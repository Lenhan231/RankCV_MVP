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


class SkillGapAnalysis(BaseModel):
    overall_verdict: str
    strengths: List[str]
    weaknesses: List[str]
    missing_skills: List[str]
    role_match_level: str
    growth_suggestions: List[str]
    mentor_note: str


class CareerAlignment(BaseModel):
    goal_feasibility: str
    readiness_level: str
    key_gaps_for_goal: List[str]
    recommended_next_steps: List[str]
    estimated_timeline: str


class CulturalFit(BaseModel):
    culture_alignment_score: int
    core_values_match: List[str]
    culture_gaps: List[str]
    work_style_compatibility: str


class MatchData(BaseModel):
    overall_score: int
    skill_match: int
    experience_match: int
    education_match: int
    current_cv_summary: str
    skills: List[str]
    experience: List[str]
    projects: List[str]
    skill_gap_analysis: SkillGapAnalysis
    career_alignment: CareerAlignment
    cultural_fit: CulturalFit


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

from fastapi import FastAPI

from app.routers import matching, interview

app = FastAPI(title="CV-JD Match API")

app.include_router(matching.router)
app.include_router(interview.router)

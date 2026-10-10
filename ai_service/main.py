from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from trend_analyzer import CognitiveTrendAnalyzer
from gemini_advisor import GeminiAdvisor

app = FastAPI(
    title="Demans Erken Teşhis & AI Trend Analiz Servisi",
    version="1.0.0",
    description="Python ML Trend & Anomaly Detection + Gemini LLM Recommendation API"
)

trend_analyzer = CognitiveTrendAnalyzer()
gemini_advisor = GeminiAdvisor()

class SessionMetrics(BaseModel):
    mean_rt_ms: float
    std_dev_ms: float
    accuracy: float
    correct_count: Optional[int] = 0
    total_trials: Optional[int] = 10

class AnalyzeRequest(BaseModel):
    user_uuid: str
    sessions: List[SessionMetrics]

@app.get("/health")
def health_check():
    return {"status": "OK", "service": "Python AI Trend Microservice"}

@app.post("/analyze")
def analyze_cognitive_trend(request: AnalyzeRequest):
    if not request.sessions:
        raise HTTPException(status_code=400, detail="Sessions list cannot be empty")

    sessions_data = [s.model_dump() for s in request.sessions]
    trend_result = trend_analyzer.analyze_user_sessions(sessions_data)
    recommendations = gemini_advisor.generate_recommendations(trend_result)

    return {
        "user_uuid": request.user_uuid,
        "analysis": trend_result,
        "recommendations": recommendations
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

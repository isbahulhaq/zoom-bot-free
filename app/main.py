from fastapi import FastAPI, Request, BackgroundTasks, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()
templates = Jinja2Templates(directory="templates")

class StartBotRequest(BaseModel):
    meeting_code: str
    passcode: str
    number_of_bots: int
    duration_minutes: int

@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})

@app.post("/api/start-bots")
async def start_bots(request: StartBotRequest, background_tasks: BackgroundTasks):
    return {"status": "accepted", "message": f"Started {request.number_of_bots} bots"}

@app.get("/health")
async def health():
    return {"status": "ok"}
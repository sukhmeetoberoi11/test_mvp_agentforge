from fastapi import FastAPI, HTTPException, Request
from .agent import parse_email, schedule_meeting
from .guardrails import guardrail_middleware
from .settings import settings

app = FastAPI()

app.middleware('http')(guardrail_middleware)

@app.get('/health')
async def health_check():
    return {'status': 'healthy'}

@app.post('/parse-email')
async def parse_email_endpoint(request: Request):
    data = await request.json()
    email_content = data.get('email_content')
    if not email_content:
        raise HTTPException(status_code=400, detail='Invalid email content format.')
    return parse_email(email_content)

@app.post('/schedule-meeting')
async def schedule_meeting_endpoint(request: Request):
    data = await request.json()
    meeting_details = data.get('meeting_details')
    if not meeting_details:
        raise HTTPException(status_code=400, detail='Invalid meeting details provided.')
    return schedule_meeting(meeting_details)

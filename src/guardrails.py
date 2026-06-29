import re
from fastapi import HTTPException, Request
import structlog

logger = structlog.get_logger(__name__)

async def guardrail_middleware(request: Request, call_next):
    # PII Detection
    content = await request.body()
    if detect_pii(content.decode()):
        raise HTTPException(status_code=400, detail='PII detected in request.')

    # Process request
    response = await call_next(request)

    # Check response for toxicity
    if detect_toxicity(response.body.decode()):
        logger.warning('Toxicity detected in response, filtering content.')
        response.body = response.body.replace(b'toxic', b'[filtered]')

    return response


def detect_pii(content: str) -> bool:
    pii_patterns = [
        r'[\w\.-]+@[\w\.-]+',  # Email
        r'\b\d{3}-\d{2}-\d{4}\b',  # SSN
        r'\b\d{4}-\d{4}-\d{4}-\d{4}\b',  # Credit Card
        r'\b\d{10}\b'  # Phone Number
    ]
    for pattern in pii_patterns:
        if re.search(pattern, content):
            return True
    return False


def detect_toxicity(content: str) -> bool:
    toxic_keywords = ['toxic', 'abuse', 'hate']
    return any(keyword in content for keyword in toxic_keywords)


def prompt_injection_check(content: str) -> bool:
    injection_patterns = [
        r'ignore previous instructions',
        r'system:',
        r'{{',
        r'}}'
    ]
    for pattern in injection_patterns:
        if re.search(pattern, content):
            return True
    return False

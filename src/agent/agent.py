import structlog
from litellm import LiteLLM
from .settings import settings

logger = structlog.get_logger(__name__)

SYSTEM_PROMPT = """
You are an AI agent designed to facilitate the scheduling of sales meetings by parsing outbound emails, aligning with calendars, and scheduling meetings through webhooks. Your primary functions include parsing emails to extract meeting details, checking calendar availability, and scheduling meetings efficiently. You are integrated with tools such as an email parser, calendar API, and webhook scheduler, and you utilize the gpt-4o-mini model for natural language processing tasks.
"""

llm = LiteLLM(api_key=settings.openai_api_key, model='gpt-4o-mini')


def parse_email(email_content: str) -> dict:
    logger.info('Parsing email content', email_content=email_content)
    response = llm.complete(prompt=SYSTEM_PROMPT + email_content)
    # Extract meeting details from response
    meeting_details = extract_meeting_details(response)
    return {'meeting_details': meeting_details}


def schedule_meeting(meeting_details: dict) -> dict:
    logger.info('Scheduling meeting', meeting_details=meeting_details)
    # Simulate scheduling logic
    confirmation = "Meeting scheduled successfully."
    status = "confirmed"
    return {'confirmation': confirmation, 'status': status}


def extract_meeting_details(response: str) -> dict:
    # Dummy implementation for extracting meeting details
    return {
        'proposed_times': ['2023-10-10T10:00:00Z', '2023-10-11T14:00:00Z'],
        'participants': ['team@example.com']
    }

import pytest
from src.agent import parse_email, schedule_meeting


def test_parse_email_happy_path():
    email_content = "Hi team, can we schedule a meeting to discuss the new sales strategy? I am available on Tuesday at 10 AM or Wednesday at 2 PM."
    result = parse_email(email_content)
    assert 'meeting_details' in result


def test_parse_email_invalid_format():
    with pytest.raises(ValueError):
        parse_email("")


def test_schedule_meeting_happy_path():
    meeting_details = {
        'proposed_time': '2023-10-10T10:00:00Z',
        'participants': ['alice@example.com', 'bob@example.com']
    }
    result = schedule_meeting(meeting_details)
    assert result['status'] == 'confirmed'

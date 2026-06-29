import pytest

@pytest.mark.asyncio
async def test_parse_email_endpoint(client):
    response = await client.post('/parse-email', json={
        'email_content': "Hi team, can we schedule a meeting to discuss the new sales strategy? I am available on Tuesday at 10 AM or Wednesday at 2 PM."
    })
    assert response.status_code == 200
    assert 'meeting_details' in response.json()


@pytest.mark.asyncio
async def test_parse_email_invalid_format(client):
    response = await client.post('/parse-email', json={})
    assert response.status_code == 400


@pytest.mark.asyncio
async def test_schedule_meeting_endpoint(client):
    response = await client.post('/schedule-meeting', json={
        'meeting_details': {
            'proposed_time': '2023-10-10T10:00:00Z',
            'participants': ['alice@example.com', 'bob@example.com']
        }
    })
    assert response.status_code == 200
    assert response.json()['status'] == 'confirmed'

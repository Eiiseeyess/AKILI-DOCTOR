import requests

def get_rasa_response(user_message, sender_id="user"):
    url = "http://localhost:5005/webhooks/rest/webhook"
    payload = {
        "sender": sender_id,
        "message": user_message
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return [{"text": "Error communicating with the Faraja AI psychiatrist."}]

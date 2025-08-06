def emotion_detector(text_to_analyze):
    import requests

    url = "https://sn-watson-emotion.labs.skills.network/v1/EmotionDetector"

    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    response = requests.post(url, data=f"text={text_to_analyze}", headers=headers)

    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    response_data = response.json()

    return {
        "anger": response_data['anger'],
        "disgust": response_data['disgust'],
        "fear": response_data['fear'],
        "joy": response_data['joy'],
        "sadness": response_data['sadness'],
        "dominant_emotion": max(response_data, key=response_data.get)
    }

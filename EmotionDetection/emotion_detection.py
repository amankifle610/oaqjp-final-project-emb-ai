import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(url, headers=headers, json=input_json)
    
    if response.status_code == 200:
        # Convert the response to a dictionary
        response_dict = response.json()
        
        # Extract emotion scores from the response structure
        try:
            emotions = response_dict['emotionPredictions'][0]['emotion']
        except (KeyError, IndexError):
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }
        
        # Extract emotion scores
        anger_score = emotions.get('anger', None)
        disgust_score = emotions.get('disgust', None)
        fear_score = emotions.get('fear', None)
        joy_score = emotions.get('joy', None)
        sadness_score = emotions.get('sadness', None)
        
        # Find the dominant emotion
        emotion_scores = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }
        
        if None in emotion_scores.values():
            dominant_emotion = None
        else:
            dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        
        # Prepare the output format
        output = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }
        return output
    else:
        # Handle blank input or other errors
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

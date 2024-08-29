"""
This module provides a Flask web server for detecting emotions from text input.
It includes an endpoint `/emotionDetector` that accepts POST requests with JSON input,
processes the input text to detect emotions using the emotion_detector function,
and returns the results in a formatted response.
"""

from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    """
    Handles POST requests to the /emotionDetector endpoint.
    Processes the input text to detect emotions and returns the results in a formatted response.
    
    Returns:
        Response object with JSON formatted results or an error message.
    """
    data = request.get_json()
    text = data.get('text', '')

    if not text:
        return jsonify("Invalid text! Please try again!"), 400

    result = emotion_detector(text)

    if result['dominant_emotion'] is None:
        return jsonify("Invalid text! Please try again!"), 400

    # Extracting and formatting the response
    response_text = (f"For the given statement, the system response is "
                     f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
                     f"'fear': {result['fear']}, 'joy': {result['joy']} and "
                     f"'sadness': {result['sadness']}. The dominant emotion is "
                     f"{result['dominant_emotion']}.")

    return jsonify(response_text)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

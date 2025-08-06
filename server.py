"""
server.py

Flask web server to provide an emotion detection endpoint
using the Watson NLP based emotion_detector function.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector", methods=["POST"])
def emotion_detector_route():
    """
    Handle POST requests for emotion detection.

    Extract text input from the form, call the emotion_detector,
    and render the result on the index.html template.

    Returns:
        Rendered HTML page with emotion detection results or error message.
    """
    text_to_analyze = request.form.get('text', '')

    response = emotion_detector(text_to_analyze)

    if response.get("dominant_emotion") is None:
        return render_template("index.html", message="Invalid text! Please try again!")

    output = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

    return render_template("index.html", message=output)


if __name__ == "__main__":
    app.run(port=5000)

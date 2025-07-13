from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    try:
        return render_template('index.html')
    except Exception as e:
        import traceback
        traceback.print_exc()
        return f"Error loading index: {e}"


@app.route("/emotionDetector")
def emo_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return ("For the given statement, the system response is "
            "'anger': {}, 'disgust': {}, 'fear': {}, 'joy': {}, 'sadness': {}. "
            "The dominant emotion is {}.").format(
                response['anger'],
                response['disgust'],
                response['fear'],
                response['joy'],
                response['sadness'],
                response['dominant_emotion']
            )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

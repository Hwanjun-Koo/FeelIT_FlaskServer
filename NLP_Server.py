# app.py
from flask import Flask, request, jsonify
from FeelIT_model import predict  # FeelIT_model.py에서 predict 함수 가져오기

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the FeelIT API!"

@app.route('/predict', methods=['POST'])
def predict_api():
    # JSON 요청을 파싱합니다.
    data = request.json
    sentence = data['sentence']
    if sentence is None:
        return 'sentence parameter is missing', 400
    # 예측을 수행합니다.
    prediction = predict(sentence)

    # JSON 응답을 반환합니다.
    return jsonify({
        'inputText': sentence,
        'fear': prediction['fear'],
        'surprised': prediction['surprised'],
        'anger': prediction['anger'],
        'sad': prediction['sad'],
        'neutral': prediction['neutral'],
        'happy': prediction['happy'],
        'disgust': prediction['disgust']
    })

if __name__=='__main__':
    app.run('0.0.0.0', port=5000, debug=True)

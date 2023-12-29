from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from AIquestion import question
from VideoToText import video_to_text
from dotenv import load_dotenv
import os

# .env 파일에서 환경 변수 로드
load_dotenv()

# 환경 변수 사용
openai_api_key = os.getenv('OPENAI_API_KEY')

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

# 자기소개서 내용을 입력받아 예상 질문 반환하는 엔드포인트
@app.route('/resume', methods=['POST'])
def generate_questions():
    data = request.json
    resume = data.get('resume')

    try:
        questions, modified_resume, length = question(openai_api_key, resume)
        # modified_resume = ''
        # length = ''
        return jsonify({
            'success': True,
            'reason': None,
            'content': {
                'results': {
                    'modified': modified_resume,
                    'length': length,
                },
                'questions': questions
            }
        })
    except Exception as e:
        print('wow',e)
        return jsonify({
            'success': False,
            'reason': str(e),
            'content': None
        }), 500


# 면접 영상을 업로드하고 텍스트로 변환하는 엔드포인트
@app.route('/video', methods=['POST'])
def upload_video():
    data = request.json
    video_path = data.get('video_path')

    if not video_path:
        return jsonify({
            'success': False,
            'reason': 'No video path provided',
            'content': None
        }), 400

    try:
        video_path = 'test.mp4'
        text = video_to_text(video_path)  # 여기에서 비디오 처리 로직이 실행됨
        return jsonify({
            'success': True,
            'reason': None,
            'content': {
                'video_path': video_path,
                'results': {
                    'text': text
                }
            },
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'reason': str(e),
            'content': None
        }), 500

if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='0.0.0.0')
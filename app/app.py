from flask import Flask, request, jsonify
from flask_cors import CORS
from AIquestion import question
from VideoToText import video_to_text

app = Flask(__name__)
CORS(app)
api_key = '' # api_key 입력

# 자기소개서 내용을 입력받아 예상 질문 반환하는 엔드포인트
@app.route('/resume', methods=['POST'])
def generate_questions():
    data = request.json
    resume = data.get('resume')

    # questions는 질문 5가지를 가진 list 형식
    try:
        questions = question(api_key, resume)
        sim_score = ''
        modified_resume = ''
        length = ''
        return jsonify({
            'success': True,
            'reason': None,
            'content': {
                'results': {
                    'similarity': sim_score,
                    'modified': modified_resume,
                    'length': length,
                },
                'questions': questions
            }
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'reason': str(e),
            'content': None
        })


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

    # 비디오 파일을 텍스트로 변환, score를 추출하는 함수 호출
    # 예: video_to_text 함수
    try:
        text, score = video_to_text(video_path) # 이 함수는 수정이 필요할 수 있음
        return jsonify({
            'success': True,
            'reason': None,
            'content': {
                'video_path': video_path,
                'results': {
                    'text': text,
                    'score': score
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
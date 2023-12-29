from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields
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
api = Api(app, version='1.0', title='API 서버', description='API 서버 문서화')

# Swagger 문서에 표시될 모델 정의
resume_model = api.model('Resume', {
    'resume': fields.String(required=True, description='자기소개서 내용')
})

video_model = api.model('Video', {
    'video_path': fields.String(required=True, description='비디오 경로')
})

ns = api.namespace('api', description='API operations')

# 자소서 첨삭 및 예상 질문 생성
@ns.route('/resume')
class ResumeQuestions(Resource):
    @api.expect(resume_model)
    def post(self):
        data = request.json
        resume = data.get('resume')

        try:
            questions, modified_resume, length = question(openai_api_key, resume)
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

# 면접 영상 업로드 
@ns.route('/video')
class VideoUpload(Resource):
    @api.expect(video_model)
    def post(self):
        data = request.json
        video_path = data.get('video_path')

        if not video_path:
            return jsonify({
                'success': False,
                'reason': 'No video path provided',
                'content': None
            }), 400

        try:
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
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
# flaskAPI
- **ML/DL 기술을 적용하기 위해 python의 flask 애플리케이션으로 API server 구현**
- Docker Image로 변환 후 **GCP(Google Cloud Platform)** push
## 로직
1. 자소서 내용을 요청 받아 자소서 기반 예상 질문 5가지 및 맞춤법 수정 결과, 글자 수를 반환
    - openAI의 API를 활용하여 사용자가 입력한 자소서 내용을 기반으로 예상 질문을 생성
    - **Google T5(Text-to-Text Transfer Transformer) model**을 활용하여 자기소개서 맞춤법 검사 및 교정

2. 면접 영상(path)를 요청받아 발화자의 텍스트를 인식하고 발화 내용을 반환
    - moviepy 라이브러리를 활용하여 영상 파일에서 wav 파일을 추출 (Video to Speech)
    - speechRecognition 라이브러리로 **Google Web Speech API**를 활용하여 wav 파일에서 텍스트를 추출 (Speech to Text)
## 추가 설명
- app.py는 html 템블릿을 활용하기 위해, app_swagger.py는 Swagger UI를 활용하기 위해 각각 따로 flask 애플리케이션을 구현
- .env 파일은 open API KEY가 들어있어 .gitignore 적용
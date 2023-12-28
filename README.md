# flaskAPI
## TO-do-list
1. VideoToText.py의 Mongo DB 연결 설정 부분 추가
```py
from pymongo import MongoClient
from moviepy.editor import VideoFileClip

# MongoDB 서버에 연결
client = MongoClient('mongodb://localhost:27017/')  # MongoDB 서버 주소와 포트를 지정

# 데이터베이스 선택
db = client['mydatabase']  # 실제 데이터베이스 이름을 사용하세요

# video_path를 사용하여 MongoDB에서 비디오 가져오기
def get_video_from_mongodb(video_path):
    # MongoDB 컬렉션 선택 (실제 컬렉션 이름을 사용하세요)
    collection = db['videos']

    # video_path를 사용하여 MongoDB에서 해당 비디오 문서 가져오기
    video_document = collection.find_one({'video_path': video_path})

    if video_document:
        # MongoDB에서 가져온 비디오 파일의 경로
        video_file_path = video_document.get('file_path')

        # VideoFileClip을 사용하여 비디오 파일 로드
        video = VideoFileClip(video_file_path)

        return video
    else:
        return None

# video_path를 사용하여 비디오를 가져옴
video_path = '/path/to/your/video.mp4'  # 요청에서 받은 video_path로 설정
video = get_video_from_mongodb(video_path)

if video:
    # 비디오를 성공적으로 가져왔을 경우
    # 여기에서 비디오 처리 수행
else:
    # MongoDB에서 비디오를 찾지 못한 경우
    # 적절한 오류 처리를 수행
```

2. requirements.txt 수정
```bash
$pip freeze
```
등을 활용하여 필요한 라이브러리를 추가

3. .env 파일 공유
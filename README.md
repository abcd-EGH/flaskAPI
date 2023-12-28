# flaskAPI
## TO-do-list
1. .env 파일 공유
2. requirements.txt 수정
```bash
$pip freeze
```
등을 활용하거나 추가로 설치했던 라이브러리를 포함시킬 것
3. AWS S3 버킷에서 비디오 파일 로드
- 비디오 파일을 로컬로 다운로드하지 않고 직접 스트리밍하여 처리
```py
import boto3
from moviepy.editor import VideoFileClip
import io

# AWS 자격 증명 설정
s3 = boto3.resource('s3', aws_access_key_id='YOUR_ACCESS_KEY', aws_secret_access_key='YOUR_SECRET_KEY')

# S3 버킷에서 파일 스트림 로드
bucket = s3.Bucket('YOUR_BUCKET_NAME')
object = bucket.Object('FILE_PATH_ON_S3')
response = object.get()
file_stream = response['Body']

# BytesIO 객체를 생성하여 moviepy가 처리할 수 있도록 함
video_stream = io.BytesIO(file_stream.read())

# 영상 파일 로드 (in VideoToText.py)
def video_to_text(video_file):
    # 영상 파일 로드
    video = VideoFileClip(video_stream)

    # 이후 비디오 파일 처리...
```
1) S3 버킷에서 파일의 내용을 읽어 BytesIO 스트림으로 변환
2) 이 스트림을 moviepy의 VideoFileClip에 전달
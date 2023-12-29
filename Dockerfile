# 기반 이미지 설정
FROM python:3.10.13

# 작업 디렉토리 생성 및 설정
WORKDIR /app

# 의존성 파일 복사
COPY requirements.txt .

# 의존성 설치
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 코드 복사
COPY ./app /app

# 포트 노출 (Flask 기본 포트: 5000)
EXPOSE 5000

# Flask 애플리케이션 실행을 위한 환경 변수 설정
ENV FLASK_APP=app_swagger.py

# Flask 애플리케이션 실행
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
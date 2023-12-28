FROM python:3.11.7

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./app /app

CMD ["python", "app/app.py"]

# docker build -t my_flask_app .
# my_flask_app -> Docker 이미지 이름
# python 버전 확인
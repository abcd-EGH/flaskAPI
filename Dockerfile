FROM python:3.11.7

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

CMD ["python", "app/app.py"]

# docker build -t my_flask_app .
# my_flask_app -> Docker 이미지 이름
# python 버전 확인
from moviepy.editor import VideoFileClip
import speech_recognition as sr
import tempfile

def video_to_text(video_file):
    # 영상 파일 로드
    video = VideoFileClip(video_file)
    
    # 오디오 추출 및 임시 파일로 저장
    with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as temp_audio_file:
        video.audio.write_audiofile(temp_audio_file.name, codec='pcm_s16le')

        # 음성 인식 객체 생성
        recognizer = sr.Recognizer()

        # 오디오 데이터를 텍스트로 변환
        with sr.AudioFile(temp_audio_file.name) as source:
            audio_data = recognizer.record(source)

        try:
            text = recognizer.recognize_google(audio_data, language="ko-KR")
            return text
        except sr.UnknownValueError:
            return "음성 인식 실패: 음성을 이해할 수 없습니다."
        except sr.RequestError as e:
            return f"음성 인식 실패: {e}"
    

# 사용 예시
# 비디오 이름이 한글일 시 호환되지 않음
video_file = '.\\app\\test.mp4'  # 변환할 비디오 파일 경로
text = video_to_text(video_file)
print(text)

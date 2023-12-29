import openai
from AImodified import CVTextProcessor

def question(api_key, resume_text):
    try:
        resume_text_ = resume_text.replace('\n', '')
        cv_processor = CVTextProcessor()
        corrected_typos, text_length = cv_processor.process_cv_text(resume_text_)
    except Exception as e:
        return ["맞춤법 검사 중 오류 발생"], str(e), 0

    # OpenAI API 키 설정
    openai.api_key = api_key

    # 질문 생성을 위한 프롬프트 설정
    prompt = f"다음은 한 지원자의 자기소개서 내용입니다:\n{resume_text_}\n\n이 지원자에게 할 수 있는 질문 5가지는 무엇인가요?"

    # OpenAI API를 통해 질문 생성 요청
    response = openai.completions.create(
        model="text-davinci-002",
        prompt=prompt,
        max_tokens=1000
    )

    return [question.strip() for question in response.choices[0].text.strip().split("\n")], corrected_typos, text_length
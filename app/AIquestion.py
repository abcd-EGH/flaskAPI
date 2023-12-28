import openai

def question(api_key, resume_text):
    # OpenAI API 키 설정
    openai.api_key = api_key

    # 질문 생성을 위한 프롬프트 설정
    prompt = f"다음은 한 지원자의 자기소개서 내용입니다:\n{resume_text}\n\n이 지원자에게 할 수 있는 질문 5가지는 무엇인가요?"

    # OpenAI API를 통해 질문 생성 요청
    response = openai.Completion.create(
    engine="davinci",
    prompt=prompt,
    max_tokens=150
    )

    return response.choices[0].text.strip()
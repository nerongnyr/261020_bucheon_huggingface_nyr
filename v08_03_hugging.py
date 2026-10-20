import os
from huggingface_hub import InferenceClient
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.markdown import Markdown

console = Console()

# 허깅페이스 클라이언트 초기화
client = InferenceClient(
    api_key=os.environ["HF_TOKEN"],
)

# 화면 정리 후 상단 헤더
console.clear()
console.print(
    Panel.fit(
        "[bold white]역사적 위인 고민 상담소[/bold white]\n"
        "[white]위인의 지혜와 현실적인 해결책을 처방해 드립니다.[/white]",
        border_style="dim",
        title="[bold white]AI MENTOR[/bold white]",
    )
)

# 사용자 입력 받기
console.print()
figure = Prompt.ask("[bold white]1. 상담받고 싶은 역사 속 위인[/bold white]")
worry = Prompt.ask("[bold white]2. 당신의 고민이나 사소한 투정[/bold white]")

console.print()

# 대화 기록 유지용 리스트 (풍부한 답변을 유도하는 지시사항 추가)
messages = [
    {
        "role": "system", 
        "content": (
            f"You are {figure}. A modern person comes to you with a modern-day problem or struggle. "
            "Provide a detailed, witty, wise, and deeply in-character response in Korean.\n\n"
            "IMPORTANT: Do NOT make your answer short. Give a thorough and rich explanation.\n\n"
            "Format your FIRST response strictly as:\n"
            "1. **[위인의 훈수]**: Write a detailed, humorous critique filled with historical color and character.\n"
            "2. **[현실적 해결책]**: Provide specific, step-by-step actionable advice they can follow today.\n\n"
            "If the user complains that the solution is too hard or asks for an easier one:\n"
            "- Tongue-click / scold them humorously in full detail (e.g. 혀를 차며 호통치고 훈계하기).\n"
            "- Provide an EVEN EASIER, ridiculously small, and effortless alternative solution (하찮을 정도로 쉬운 해결책) with a funny explanation."
        )
    },
    {
        "role": "user", 
        "content": worry
    }
]

# 1차 답변 생성 및 대화 루프
while True:
    with console.status(f"[bold white]{figure}[/bold white] [dim]답변 작성 중...[/dim]", spinner="dots"):
        response_stream = client.chat.completions.create(
            model="Qwen/Qwen2.5-72B-Instruct",
            messages=messages,
            max_tokens=1300, 
            temperature=0.7,   # 캐릭터 연기력과 풍부한 대화 생성
            stream=True
        )

        full_response = ""
        for chunk in response_stream:
            content = chunk.choices[0].delta.content or ""
            full_response += content

    # 결과 출력 패널
    console.print(Panel(f"[bold white]{figure}의 처방전[/bold white]", border_style="dim"))
    md = Markdown(full_response)
    console.print(md, style="white")
    console.print("\n[dim]--------------------------------------------------[/dim]\n")

    # 대화 기록에 AI 답변 저장
    messages.append({"role": "assistant", "content": full_response})

    # 거부권 질문 받기
    feedback = Prompt.ask(
        "[bold white]💡 해결책이 너무 어려운가요?[/bold white] [dim](엔터: 종료 / 내용 작성: '더 쉬운 거 줘' 등)[/dim]"
    )

    # 아무것도 입력하지 않고 엔터 누르면 종료
    if not feedback.strip():
        console.print(f"\n[bold white]{figure}[/bold white]: [dim]부디 실천에 옮기도록 하여라![/dim]\n")
        break

    # 사용자 꼬리 질문을 히스토리에 추가 후 재요청
    messages.append({"role": "user", "content": feedback})
    console.print()
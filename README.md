# 📜 역사적 위인 고민 상담소 (AI Mentor CLI)

> **HuggingFace Inference API** 기반의 AI 위인 페르소나 고민 상담 CLI 서비스입니다.  
> 현대인의 소소한 고민에 대해 역사 속 위인들이 위트 넘치는 훈수와 함께 **당장 실천 가능한 2차 대화형 해결책**을 제시합니다.

---

## ✨ 주요 기능 (Key Features)

1. **위인 페르소나 상담**: 세종대왕, 이순신, 정약용, 아인슈타인 등 원하는 역사 속 위인에게 고민을 상담받을 수 있습니다.
2. **2차 대화형 "해결책 거부권"**: 제시받은 해결책이 너무 어렵거나 부담스러울 경우, *"더 쉬운 거 줘!"* 라고 요청하면 위인이 혀를 차며 **하찮을 정도로 쉬운 5분 컷 해결책**으로 다시 처방해 줍니다.
3. **고속 인퍼런스 모델 적용**: `Qwen/Qwen2.5-72B-Instruct` 모델을 적용하여 기다림 없이 빠르게 답변을 streaming 형태로 받아볼 수 있습니다.
4. **가독성 최적화 UI**: `rich` 라이브러리를 통해 눈의 피로를 최소화한 흑백·그레이 모노톤 CLI UI를 제공합니다.

---

## 🛠️ 기술 스택 (Tech Stack)

* **Language**: Python 3.10+
* **LLM Model**: `Qwen/Qwen2.5-72B-Instruct` (via Hugging Face Inference API)
* **UI/UX**: `rich` (Panel, Status Spinner, Markdown)
* **API Client**: `huggingface_hub`

---

## 🚀 시작하기 (Quick Start)

### 1. 레포지토리 클론
```bash
git clone [https://github.com/nerongnyr/261020_bucheon_huggingface_nyr.git](https://github.com/nerongnyr/261020_bucheon_huggingface_nyr.git)
cd 261020_bucheon_huggingface_nyr
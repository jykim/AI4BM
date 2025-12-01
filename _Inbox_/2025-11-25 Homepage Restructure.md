---
title: "Homepage Restructure"
created: "2025-11-25T19:30:00"
status: "pending_approval"
priority: "high"
type: "content_update"
---

# Homepage Restructure Task

## 목표
AI for PKM 홈페이지를 마케팅 최적화 구조로 재편

## 대상 파일
`/Publish/AI for PKM/AI for PKM.md`

## 현재 구조 분석
```
1. Introduction + signup links (3줄)
2. AI for Better Me Challenge callout
3. 최근 발표자료 (2 PDFs)
4. Project 소개 (videos, GitHub)
5. 설치 비디오
6. PKM in AI Era 시리즈 (8개 아티클)
```

**문제점:**
- Hero section 부재 - 가치 제안 불명확
- Quick Start 없음 - 15분 내 첫 가치 경험 어려움
- 페르소나별 가이드 없음 - 모든 사용자에게 동일한 경로
- CTA 계층 불명확

---

## 제안 구조

### 1. Hero Section (신규)
```markdown
# AI for PKM

> **AI 시대, 지식이 곧 경쟁력입니다.**
>
> AI4PKM은 Claude, Gemini 등 AI 에이전트를 활용해 개인 지식 관리를 자동화하는 오픈소스 프레임워크입니다.

**15분 만에 첫 자동화 워크플로우를 경험하세요.**

[빠른 시작 가이드](#quick-start) | [Discord 참여](https://discord.gg/58cmahcbx3) | [메일링 리스트](https://substack.com/@lifidea)
```

### 2. Quick Start (신규)
```markdown
## Quick Start

### Step 1: 앱 설치 (5분)
- [Gobi Desktop 다운로드](link) - Windows/Mac 원클릭 설치
- 또는 [GitHub에서 수동 설치](https://github.com/jykim/AI4PKM)

### Step 2: 첫 워크플로우 실행 (5분)
- 샘플 아티클을 `Ingest/Clippings/`에 저장
- 자동으로 요약 + 토픽 태깅 완료

### Step 3: 결과 확인 (5분)
- `AI/Articles/`에서 처리된 콘텐츠 확인
- 첫 자동화 완료!

![Quick Start Demo Video](link)
```

### 3. 페르소나별 가이드 (신규)
```markdown
## 어디서 시작할까요?

### PKM 처음이신가요?
→ [[0. Why PKM now?]] 부터 시작하세요
- PKM의 가치와 AI 시대의 필요성 이해
- 기초 이론 (0-4번 아티클)

### 이미 PKM을 하고 계신가요?
→ [[4. PKM in Gen AI Era]] 로 바로 가세요
- AI 통합의 혁신적 가능성
- 실용 가이드 (5-7번 아티클)

### 개발자/기여자이신가요?
→ [GitHub](https://github.com/jykim/AI4PKM) + [Skills Repo](link)
- 커스텀 스킬 개발
- 워크플로우 기여
```

### 4. Core Features
```markdown
## 핵심 기능

### Multi-Agent Support
Claude Code, Gemini CLI, Codex CLI 등 다양한 AI 에이전트 지원

### Pre-built Skills
[[AI4PKM-Skills]] - 바로 사용 가능한 5개+ 스킬
- 문서 구조화, 링크 검증, 슬라이드 생성 등

### Automated Workflows
- 콘텐츠 수집 → 요약 → 토픽 연결 자동화
- 매일 자동 라운드업 생성
- 일정 기반 자동 실행
```

### 5. Community (기존 + 보강)
```markdown
## 커뮤니티

### AI for Better Me Challenge
12월~1월 한달간 AI 지식관리 실천 챌린지
[참여 신청](https://forms.gle/PyvmwjLSdnuMqssQ7)

### Discord
실시간 Q&A, 워크플로우 공유, 주간 Show & Tell
[참여하기](https://discord.gg/58cmahcbx3)

### 오픈톡방
[카카오톡 참여](https://invite.kakao.com/tc/xHzCZCnM7F)
```

### 6. 발표자료 & 개념소개 (기존 재구성)
```markdown
## 더 알아보기

### 발표자료
- **10/24 PKM Summit**: ![[2025-10-25 Agentic Future for PKM - slides.pdf]]
- **10/1 Changbal Meetup**: ![[2025-10-01 AI for Knowledge Work - slides (Changbal).pdf]]

### 영상
- [AI4PKM 소개 비디오](https://youtu.be/F9KZr0IPn1k)
- [개념과 실습 비디오](https://youtu.be/2BMOOMVTdPw)
```

### 7. Learning Resources (기존 재구성)
```markdown
## PKM in AI Era 시리즈

### 기초 이론편 (0-4)
[[0. Why PKM now?]] | [[1. PKM Overview]] | [[2. PKM Components]] | [[3. PKM Principles]] | [[4. PKM in Gen AI Era]]

### 실용 가이드편 (5-7)
[[5. PKM FAQ]] | [[6-1. Comparing AI Agents]] | [[6-2. Applying AI Agents]] | [[7-1. Field Guide]] | [[7-2. 실습]] | [[7-3. 실천]]

### 미래 전망편 (8)
[[8. Future of PKM - Self-Improving PKM]]
```

---

## 승인 요청 사항

1. **구조 변경 승인**: 위 제안대로 재구성해도 될까요?
2. **Quick Start 콘텐츠**: Gobi Desktop 링크가 아직 없으면 GitHub 수동 설치로 대체?
3. **Skills Repo 링크**: 아직 생성 전이므로 placeholder로 넣어도 될까요?

---

## 실행 계획

승인 후:
1. 현재 홈페이지 백업
2. 새 구조로 콘텐츠 재배치
3. 누락된 링크 확인 및 수정
4. Wiki link 유효성 검증

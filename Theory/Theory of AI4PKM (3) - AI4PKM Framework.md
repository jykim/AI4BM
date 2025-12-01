---
title: Theory of AI4PKM (3) - AI4PKM Framework
created: 2025-11-11
tags:
  - ai4pkm
  - knowledge-management
  - theory
  - framework
series: Theory of AI4PKM
part: 3
previous: "[[Theory of AI4PKM (2) - Using AI for PKM]]"
next: "[[Theory of AI4PKM (4) - From Knowledge to Goals]]"
dg-publish: true
---

# Theory of AI4PKM (3) - AI4PKM Framework

[[Theory of AI4PKM (2) - Using AI for PKM|이전 글]]에서 AI가 어떻게 PKM의 세 가지 장벽(수집-정리-창작)을 무너뜨렸는지 살펴봤다. 이제 실제로 어떤 시스템을 어떻게 만들어야 할지, 구체적인 프레임워크를 설계해보자.

> [!tip] 읽기 가이드
> - **빠른 스캔**: 설계 원칙과 핵심 구성요소만 (10분)
> - **심화 학습**: 각 섹션의 세부 내용까지 (40분)

---

## Design Goals

### 인간과 AI를 위한 PKM (PKM for both Human and AI)

AI4PKM 시스템은 인간 사용자와 AI 에이전트가 **함께 사용하는** 공간이다.

**핵심 전략**:
- AI가 생성한 콘텐츠는 인간이 작성한 노트와 분리하여 보관
- 인간과 AI가 함께 수정하는 파일은 Git 버전 관리로 안전하게 보호
- 자동화된 워크플로우는 `.md` 파일 기반으로 실행되어 사용자가 완전히 통제 가능

**예시 구조**:
```
PKM Vault/
├─ Ingest/          # 인간이 수집한 원본
├─ AI/              # AI가 생성한 분석
├─ Topics/          # 인간이 큐레이션한 지식
└─ Journal/         # 인간+AI 공동 작성 (Git 관리)
```

### 도구 중립성 (Tool-agnostic Approach)

특정 도구에 종속되지 않고, 여러 AI 도구와 모델을 자유롭게 실험할 수 있어야 한다.

**이유**:
- AI 기술은 빠르게 발전하고 있다
- 오늘의 최고 모델이 내일도 최고라는 보장이 없다
- 여러 AI를 비교하고 각각의 강점을 활용할 수 있어야 한다

**구현 방식**:
- 모든 콘텐츠를 표준 Markdown 형식으로 저장
- YAML frontmatter로 메타데이터 관리
- CLI 에이전트 기반으로 다양한 AI 모델 사용

### 다양한 협업 모델 (Various Human-AI Collaboration Models)

인간과 AI의 협업은 양방향이어야 한다.

**Human → AI** (사용자가 주도):
- Ad-hoc 요청: 즉시 필요한 작업 (음성/텍스트/코멘트 기반)
- 정기 워크플로우: 예정된 루틴 작업 (매일/매주)
- 트리거 워크플로우: 이벤트 기반 자동 실행

**AI → Human** (TBA - To Be Added):
- 아이디어 제안: 패턴 발견 시 제안
- 목표 리마인더: 목표 추적 및 동기부여
- 데이터 수집 요청: 부족한 정보 요청

---

## Components

### 재사용 가능한 Prompts & Skills

프롬프트는 AI를 효과적으로 활용하기 위한 핵심 레시피다.

**설계 원칙**:
- 프롬프트는 재사용 가능하고 단순하게 유지
- Skills는 재사용 가능한 작업 특화 지식을 담는다
- 파라미터를 통해 다양한 상황에 적용 가능

**실행 방식**:
- 프롬프트는 독립적으로 실행 가능
- 여러 프롬프트를 조합하여 워크플로우 구성
- CLI 에이전트에서 직접 실행

**예시**:
```markdown
# _Settings_/Prompts/Enrich Ingested Content (EIC).md

## Purpose
수집한 클리핑/녹취를 분석하여 요약과 인사이트 추가

## Input
- Ingest/Clippings/*.md 또는 Ingest/Limitless/*.md

## Output
- Summary (핵심 내용)
- Key Insights (주요 인사이트)
- Related Topics (연결할 주제)
- status: processed
```

### Agent 기반 Workflows

복잡한 작업은 여러 에이전트의 협업으로 처리한다.

**에이전트 역할**:
- **Orchestrator**: 작업을 분할하고 워커 에이전트들을 생성
- **Worker**: 개별 프롬프트를 실행하고 태스크를 업데이트
- **Evaluator** (TBA): 워커의 결과물을 평가

**장점**:
- 각 에이전트가 명확한 역할을 가짐
- 복잡한 작업을 작은 단위로 분할
- 병렬 처리로 효율성 향상
- 각 단계의 품질 관리 가능

### Knowledge Tasks

모든 워커의 작업은 `.md` 형식의 지식 태스크로 문서화된다.

**태스크 구조**:
- 작업 명세 (Job specification)
- 진행 상황 (Job progress)
- 작업 결과 (Job outcome)
- 평가 결과 (Job evaluation - TBA)

**예시**:
```markdown
# AI/Tasks/2025-11-15 Weekly Roundup.md

status: completed
workflow: WRP
created: 2025-11-15 09:00
completed: 2025-11-15 17:30

## Input
- Journal/2025-11-10 ~ 15.md
- Limitless recordings (last 7 days)

## Output
- AI/Roundup/2025-11-15 Weekly Review.md

## Result
주간 리뷰 생성 완료. 3개 주요 테마 발견.
```

### Tool Ecosystem

AI4PKM은 다양한 도구들과 호환된다.

**CLI Agents** (워커로 활용):
- Claude Code
- Codex / Gemini CLI

**Code Editor** (AI와 실시간 협업):
- VS Code
- Cursor

**Text Editor** (지식 브라우징 및 생성):
- Obsidian
- 모든 Markdown 에디터

**핵심**: 각 도구는 특정 용도에 최적화되어 있지만, 모두 같은 Markdown 파일을 사용하므로 자유롭게 전환 가능하다.

---

## 다음 글에서

지금까지 AI4PKM 시스템의 설계 원칙과 핵심 구성요소를 살펴봤다. 시스템을 "어떻게" 구축하는가에 대해 이해했다면, 이제 더 근본적인 질문으로 넘어가야 한다:

**"시스템을 완벽하게 구축했는데, 왜 내 삶은 나아지지 않을까?"**

지식은 쌓이는데 변화는 없다. 이것이 바로 **Perfect PKM Paradox**다.

[[Theory of AI4PKM (4) - From Knowledge to Goals|다음 글]]에서는 지식 관리를 넘어 **실제 삶의 변화와 목표 달성**으로 연결하는 AI4BetterMe 프레임워크를 다룬다. PKM이 단순한 정리 도구가 아닌 **성장 엔진**이 되는 방법을 살펴본다.

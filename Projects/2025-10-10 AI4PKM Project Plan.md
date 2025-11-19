---
title: AI4PKM Project Plan
created: 2025-10-10
tags:
  - project-plan
  - ai4pkm
  - pkm
related:
  - "[[2025-09-01 AI4PKM Lecture Planning]]"
  - "[[AI4PKM Brainstorming]]"
  - "[[Events/2025-10-08 Summary for Minsuk-Jin Meeting - Claude Code]]"
  - "[[Ingest/Apple Notes/2025-10-01 Scaling up AI4PKM Project]]"
---

# AI4PKM Project Plan

## 프로젝트 개요

**비전**: AI 에이전트를 활용한 차세대 Personal Knowledge Management 시스템 구축

**미션**: 자연어 프로그래밍 패러다임을 통해 누구나 쉽게 사용할 수 있는 지식 자동화 플랫폼 제공

**핵심 가치 제안**:
- **자연어 명령으로 복잡한 지식 작업 수행**: "오늘치 DIR 돌려줘", "며칠 빼먹었으니 백필 해줘"
- **Always-On 캡처와 PKM 통합**: Limitless 등을 통한 완전 자동화된 데이터 수집
- **멀티모달 데이터 처리**: 텍스트, 오디오, 비디오 통합 처리

## 1. 현황 분석 (Based on 2025-10-08 Meeting with Minsuk)

### 1.1 현재 구현 상태

**작동 중인 시스템**:
- ✅ Obsidian + Claude Code + Git 기반 PKM 환경
- ✅ 데일리 워크플로우 (DIR - Daily Ingestion and Roundup)
  - PLL (Process Life Logs)
  - EIC (Enrich Ingested Content)
  - GDR (Generate Daily Roundup)
  - TKA (Topic Knowledge Addendum)
- ✅ 태스크 큐 시스템 (Knowledge Task Processing)
- ✅ 듀얼 Todo 시스템 (개인 작업 vs AI 작업)

**실험 중인 기술**:
- 🔬 로컬 LLM (Goose + Ollama, Qwen 2.5/3 Coder)
- 🔬 클라우드 PKM 환경 (Google Cloud VM)
- 🔬 데이터 분석 애플리케이션 프로토타입

### 1.2 핵심 도전과제

> "AI한테 뭘 시켰을 때... 그게 맞는지 틀린지를 판단할 수 있는 능력이 있어야 해요. 그게 없으면 그냥 AI가 한 거를 그대로 쓰는 거잖아요."

**기술적 한계**:
1. **컨텍스트 제한**: 긴 세션에서 품질 저하 및 누락 발생
2. **신뢰성 문제**: AI 출력물의 일관성 부족, "믿고 맡기기" 어려움
3. **시간대 이슈**: 클라우드 환경에서 UTC vs PDT 혼동
4. **노이즈 필터링**: 일상 대화 vs 의미있는 콘텐츠 구분 어려움

**운영상 과제**:
1. **"지적질의 가치"**: AI 출력물 검증 및 피드백 루프 필수
2. **타이밍 딜레마**: "조금만 기다리면 AI가 더 좋아질 텐데..." vs 지금 구현
3. **하이브리드 접근 필요**: 로컬 vs 클라우드, AI vs 코드, 자동화 vs 수동 큐레이션

## 2. 기술 아키텍처

### 2.1 현재 아키텍처

```
┌─────────────────────────────────────────────────────────┐
│                    Data Sources                          │
├─────────────────────────────────────────────────────────┤
│  Limitless  │  Readwise  │  YouTube  │  Web Clipper    │
└──────┬──────┴──────┬─────┴─────┬─────┴─────┬───────────┘
       │             │           │           │
       └─────────────┴───────────┴───────────┘
                     │
       ┌─────────────▼─────────────┐
       │   Ingestion Layer          │
       │  (DIR Workflow)            │
       │  - PLL                     │
       │  - EIC                     │
       │  - GDR                     │
       │  - TKA                     │
       └─────────────┬─────────────┘
                     │
       ┌─────────────▼─────────────┐
       │   Storage Layer            │
       │  (Obsidian Vault + Git)   │
       │  - Markdown Files          │
       │  - Wiki Links              │
       │  - YAML Frontmatter        │
       └─────────────┬─────────────┘
                     │
       ┌─────────────▼─────────────┐
       │   Processing Layer         │
       │  (Task Queue System)       │
       │  - Task Generator          │
       │  - Task Processor          │
       │  - Visibility Dashboard    │
       └─────────────┬─────────────┘
                     │
       ┌─────────────▼─────────────┐
       │   Agent Layer              │
       │  (Claude Code / CLI)       │
       │  - Main Agent              │
       │  - Sub-agents (EIC, TKI)   │
       └─────────────┬─────────────┘
                     │
       ┌─────────────▼─────────────┐
       │   Output Layer             │
       │  - Daily Roundups          │
       │  - Topic Updates           │
       │  - Event Summaries         │
       └─────────────────────────────┘
```

### 2.2 제안하는 개선 아키텍처

**핵심 개선사항**:

1. **태스크 큐 자동화 (Code-based Task Routing)**
   ```
   Task Queue Manager (Code)
   ├── Task Discovery (Code + LLM)
   │   └── Scan for tagged items, file changes, calendar events
   ├── Task Routing (Code)
   │   ├── Budget allocation (token limits per agent)
   │   ├── Agent selection (Claude Code / CLI / Gemini)
   │   └── Parallel task distribution
   └── Task Monitoring (Code)
       ├── Visibility dashboard
       └── Feedback collection
   ```

2. **하이브리드 실행 환경**
   ```
   Primary Environment: Local MacBook Pro
   ├── Always-on server role
   ├── iCloud sync for file access
   └── Anydesk for remote access

   Cloud Environment: Google Cloud VM (Optional)
   ├── For heavy processing
   ├── Timezone-aware scheduling
   └── Backup execution environment
   ```

3. **신뢰성 향상 메커니즘**
   ```
   Fresh Context Strategy
   ├── Each task spawns new agent instance
   ├── Clear input/output contracts
   ├── No context carryover between tasks
   └── Lossless processing (avoid compression)

   Validation Layer
   ├── Output verification rules
   ├── Human-in-the-loop for critical tasks
   └── Feedback training data collection
   ```

## 3. 구현 로드맵

### Phase 1: 기반 안정화 (2주, ~2025-10-24)

**목표**: 현재 시스템의 신뢰성과 가시성 확보

**작업 항목**:
1. **태스크 큐 시스템 코드화**
   - [ ] Task discovery 로직 구현 (태그 스캔, 파일 변경 감지)
   - [ ] Task routing 엔진 구현 (버짓 할당, 에이전트 선택)
   - [ ] 가시성 대시보드 개선 (Obsidian 플러그인 or 별도 파일)

2. **컨텍스트 관리 개선**
   - [ ] Fresh context 전략 적용 (매 태스크마다 새 인스턴스)
   - [ ] Sub-task 분할 로직 (긴 작업 → 여러 작은 작업)
   - [ ] 입출력 계약 명확화 (각 워크플로우 단계별)

3. **피드백 루프 구축**
   - [ ] AI 출력물 검증 체크리스트
   - [ ] 피드백 데이터 수집 포맷 정의
   - [ ] 개선 사항 추적 메커니즘

**성공 지표**:
- DIR 워크플로우 성공률 > 90%
- 평균 처리 시간 < 10분
- 사용자 개입 필요 횟수 < 3회/일

### Phase 2: 자동화 확장 (3주, ~2025-11-14)

**목표**: 수동 작업 최소화, 병렬 처리 극대화

**작업 항목**:
1. **로컬 서버 환경 구축**
   - [ ] MacBook Pro 전용 서버 설정 (항상 켜져 있는 환경)
   - [ ] Anydesk 원격 접속 설정
   - [ ] iCloud 동기화 최적화
   - [ ] Cron job 스케줄링 (DIR, CKU, WRP)

2. **병렬 처리 파이프라인**
   - [ ] 여러 에이전트 동시 실행 (Claude Code, CLI, Gemini)
   - [ ] 버짓 자동 분배 시스템
   - [ ] 실패 재시도 로직
   - [ ] 진행 상황 알림 (Slack or 이메일)

3. **백필 및 점진적 업데이트**
   - [ ] "며칠 빼먹었으니 백필 해줘" 명령 구현
   - [ ] "업데이트된 것만 찾아서 돌려줘" 로직
   - [ ] 변경 감지 및 증분 처리

**성공 지표**:
- 하루 처리 가능 파일 수 > 50개
- 병렬 처리로 인한 시간 단축 > 50%
- 백필 성공률 > 95%

### Phase 3: 콘텐츠 활용 강화 (2주, ~2025-11-28)

**목표**: PKM 데이터를 활용한 가치 창출

**작업 항목**:
1. **글쓰기 지원 시스템**
   - [ ] 글감 자동 발굴 (토픽별 요약 분석)
   - [ ] 아웃라인 생성 프롬프트
   - [ ] 작문 및 퇴고 워크플로우

2. **개인 비서 기능**
   - [ ] 미팅 준비 자료 자동 생성 (과거 대화 기록 참조)
   - [ ] 미팅 후 액션 아이템 추출 및 Todo 연동
   - [ ] 이메일 초안 작성 지원

3. **데이터 분석 애플리케이션 프로토타입**
   - [ ] Generic 데이터 분석 프레임워크 (Titanic 데모)
   - [ ] 특정 유저 타게팅 (중소기업 마케터, 개인 사업자)
   - [ ] MVP 핵심 기능 3가지 정의

**성공 지표**:
- 주간 콘텐츠 생성량 > 5개
- 미팅 준비 시간 단축 > 30%
- 데이터 분석 앱 사용자 피드백 수집

### Phase 4: 강의 및 커뮤니티 (진행중)

**목표**: AI4PKM 방법론 공유 및 커뮤니티 구축

**작업 항목**:
1. **커리큘럼 완성**
   - [ ] Part 1: Foundation (강의 자료 초안 완료)
   - [ ] Part 2: Data Ingestion & Organization
   - [ ] Part 3: PKM 활용
   - [ ] Part 4: Capstone & 운영

2. **실습 환경 준비**
   - [ ] 샘플 Vault 템플릿
   - [ ] Setup 가이드 (15분 체크리스트)
   - [ ] 트러블슈팅 FAQ

3. **커뮤니티 플랫폼**
   - [ ] Discord or Slack 채널
   - [ ] 사례 공유 및 질의응답
   - [ ] 월간 오피스 아워

## 4. 핵심 의사결정 포인트

### 4.1 로컬 vs 클라우드

**결정**: 하이브리드 접근 (로컬 우선, 클라우드 백업)

**근거**:
- ✅ iCloud 동기화로 멀티 디바이스 접근 자동 해결
- ✅ 로컬 실행으로 시간대 문제 회피
- ✅ 웹 스크래핑, 플러그인 등 로컬 도구 활용 가능
- ⚠️ 클라우드는 heavy processing 용도로만 선택적 사용

### 4.2 AI vs 코드

**결정**: "코드 first, AI augmented"

**근거**:
> "조금만 기다리면 AI가 더 좋아질 텐데..." vs 지금 구현

- ✅ 태스크 발견, 라우팅, 모니터링은 코드로 구현 (신뢰성)
- ✅ 콘텐츠 생성, 요약, 분석은 AI로 수행 (유연성)
- ✅ 피드백 루프로 AI 품질 지속 개선
- ⚠️ AI 발전을 기다리지 말고, 지금 가능한 것으로 시작

**구현 원칙**:
```python
# 코드가 해야 할 일
- Task discovery (파일 스캔, 태그 찾기)
- Task routing (버짓 분배, 에이전트 선택)
- Monitoring (진행 상황, 실패 감지)
- Validation (출력물 검증 룰)

# AI가 해야 할 일
- Content summarization
- Semantic analysis
- Writing assistance
- Creative generation
```

### 4.3 프로토타입 vs 프로덕션

**결정**: "지금 하는 것의 가치" - 프로토타입으로 시작, 피드백으로 개선

**근거**:
- ✅ 학습 과정 자체가 중요
- ✅ 문제 정의와 해결 과정에서 인사이트 획득
- ✅ "만들어봐야" 무엇이 필요한지 안다
- ⚠️ 완벽한 도구를 기다리다 아무것도 안 하면 손해

**반복 전략**:
1. 프로토타입 (2주) → 2. 사용자 피드백 (1주) → 3. 개선 (1주) → 반복

## 5. 액션 아이템 (Next Steps)

### 이번 주 (2025-10-10 ~ 2025-10-16)

**최우선 순위**:

1. **로컬 서버 환경 설정** ⏰ 목표: 2025-10-11
   - [ ] MacBook Pro 전원 항상 켜기 설정
   - [ ] Anydesk 설치 및 원격 접속 테스트
   - [ ] iCloud 동기화 확인 (Obsidian Vault)

2. **태스크 큐 코드화 착수** ⏰ 목표: 2025-10-14
   - [ ] Task discovery 스크립트 작성 (Python or Bash)
   - [ ] Task queue 파일 포맷 정의 (YAML or JSON)
   - [ ] 기본 routing 로직 구현

3. **Fresh context 전략 적용** ⏰ 목표: 2025-10-16
   - [ ] DIR 워크플로우 각 단계를 독립 실행으로 분리
   - [ ] 입출력 계약 문서화 (각 프롬프트별)
   - [ ] 테스트 및 성공률 측정

### 다음 주 (2025-10-17 ~ 2025-10-23)

4. **피드백 루프 구축**
   - [ ] AI 출력물 검증 체크리스트 작성
   - [ ] 피드백 데이터 수집 템플릿 생성
   - [ ] 1주일 사용 후 개선점 분석

5. **강의 자료 보완**
   - [ ] Part 2: Data Ingestion & Organization 슬라이드
   - [ ] 실습 환경 Setup 가이드
   - [ ] 샘플 Vault 준비

## 6. 성공 지표 및 평가

### 단기 지표 (1개월)

- **시스템 신뢰성**: DIR 워크플로우 성공률 > 90%
- **생산성**: 하루 처리 가능 파일 수 > 50개
- **자동화율**: 수동 개입 필요 횟수 < 3회/일

### 중기 지표 (3개월)

- **콘텐츠 활용**: 주간 생성 콘텐츠 > 5개
- **커뮤니티**: 강의 수강생 > 20명
- **피드백**: 사용자 만족도 > 4.0/5.0

### 장기 지표 (6개월)

- **비즈니스**: MVP 검증 및 유료 전환율 > 10%
- **기술**: AI 모델 개선으로 인한 품질 향상 > 30%
- **확장성**: 타 도메인 적용 사례 > 3개

## 7. 리스크 및 대응 방안

### 기술적 리스크

**R1: AI 모델의 불안정성**
- 대응: Fresh context 전략, 검증 체크리스트, 피드백 루프

**R2: 컨텍스트 제한으로 인한 품질 저하**
- 대응: Sub-task 분할, 코드 기반 라우팅, 독립 인스턴스 실행

**R3: 시간대 및 동기화 문제**
- 대응: 로컬 우선 전략, iCloud 자동 동기화

### 운영상 리스크

**R4: 사용자의 "지적질" 피로도**
- 대응: 가시성 대시보드, 자동 검증 룰, 점진적 개선

**R5: "조금만 기다리면..." 함정**
- 대응: 명확한 마일스톤, 반복 주기 설정, 학습 과정 가치 강조

**R6: Problem-Solution Fit 불명확**
- 대응: 특정 타겟 유저 설정 (중소기업 마케터), MVP 범위 축소

## 8. 참고 자료

### 관련 문서
- [[2025-09-01 AI4PKM Lecture Planning]]
- [[AI4PKM Brainstorming]]
- [[Projects/Contents Marketing/2025-08 AI4PKM MVP 검증 프레임워크]]
- [[Projects/Contents Marketing/2025-08 AI4PKM 비즈니스 제품 로드맵 및 가격 전략]]

### 미팅 기록
- [[Events/2025-10-08 Summary for Minsuk-Jin Meeting - Claude Code]]
- [[Events/2025-08-21 AI4PKM Group Meeting Notes - Claude Code]]
- [[Events/2025-09-11 AI4PKM Repo Dev Planning Meeting]]

### 기술 문서
- [[Topics/Technology/Claude Code]]
- [[Topics/Technology/PKM]]
- [[(dep) Daily Ingestion and Roundup (DIR)]]
- [[_Settings_/Guidelines/PKM Guidelines]]

---

## 다음 단계

**즉시 실행**: 로컬 서버 환경 설정 (MacBook Pro + Anydesk)
**이번 주**: 태스크 큐 코드화 착수, Fresh context 전략 적용
**다음 주**: 피드백 루프 구축, 강의 자료 보완

**정기 리뷰**: 매주 금요일 진행 상황 점검 및 다음 주 계획 수립

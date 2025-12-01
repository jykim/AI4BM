---
title: "Google Analytics Integration"
created: "2025-11-25T19:30:00"
status: "pending_approval"
priority: "high"
type: "technical_setup"
---

# Google Analytics Integration Task

## 목표
jykim.github.io/AI4PKM Dev Docs에 Google Analytics 4 연동

## 대상
- **사이트**: https://jykim.github.io/AI4PKM/
- **리포**: https://github.com/jykim/AI4PKM (docs/ 폴더)

---

## Step 1: GA4 Property 생성 (사용자 직접)

### 필요한 작업
1. [Google Analytics](https://analytics.google.com/) 접속
2. "관리" → "계정 만들기" 또는 기존 계정 선택
3. "속성 만들기" 클릭
4. 속성 이름: `AI4PKM Dev Docs`
5. 데이터 스트림 추가 → 웹
   - URL: `jykim.github.io/AI4PKM`
   - 스트림 이름: `AI4PKM Docs`
6. **측정 ID 복사** (형식: `G-XXXXXXXXXX`)

---

## Step 2: Jekyll 설정 (자동 실행 가능)

### Option A: _config.yml 수정 (권장)

```yaml
# _config.yml에 추가
google_analytics: G-XXXXXXXXXX
```

Jekyll 테마가 GA를 지원하면 자동 적용됩니다.

### Option B: 직접 스크립트 삽입

`docs/_includes/head.html` 또는 레이아웃 파일에 추가:

```html
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

---

## Step 3: 추적할 이벤트 설정

### 기본 추적 (자동)
- Page views
- Session duration
- Bounce rate
- Traffic sources

### 커스텀 이벤트 추적 (권장)

```html
<!-- CTA 클릭 추적 -->
<a href="https://discord.gg/..." onclick="gtag('event', 'click', {
  'event_category': 'CTA',
  'event_label': 'Discord Join'
});">Discord 참여</a>

<a href="https://github.com/jykim/AI4PKM" onclick="gtag('event', 'click', {
  'event_category': 'CTA',
  'event_label': 'GitHub Repo'
});">GitHub</a>

<a href="https://substack.com/@lifidea" onclick="gtag('event', 'click', {
  'event_category': 'CTA',
  'event_label': 'Mailing List'
});">메일링 리스트</a>
```

### 추적 목표

| 이벤트 | 설명 | 목표 |
|--------|------|------|
| Discord Join Click | Discord CTA 클릭 | CTR > 5% |
| GitHub Click | GitHub 리포 방문 | CTR > 10% |
| Skills Repo Click | Skills 리포 방문 | CTR > 3% |
| Quick Start View | Quick Start 섹션 도달 | View > 50% |
| Article Click | 시리즈 아티클 클릭 | Click-through > 20% |

---

## Step 4: 대시보드 설정

### GA4 기본 리포트
- 실시간: 현재 방문자
- 획득: 트래픽 소스 (Organic, Direct, Referral)
- 참여: 페이지별 조회수, 체류시간
- 전환: 설정한 이벤트 목표

### 권장 커스텀 리포트
1. **Funnel Report**: 홈페이지 → Quick Start → GitHub Clone
2. **CTA Performance**: 각 CTA별 클릭률 비교
3. **Content Engagement**: 어떤 아티클이 가장 인기있는지

---

## 승인 요청 사항

1. **GA4 Property 생성**: 측정 ID를 알려주시면 자동 설정 진행
2. **커스텀 이벤트**: 위 이벤트들 추적해도 될까요?
3. **Privacy Policy**: 필요하면 프라이버시 정책 페이지 추가?

---

## 실행 계획

사용자가 측정 ID 제공 후:
1. `docs/_config.yml`에 GA ID 추가
2. 주요 CTA에 이벤트 추적 코드 추가
3. GitHub에 변경사항 커밋 & 푸시
4. GA4에서 실시간 리포트로 동작 확인

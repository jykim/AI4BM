---
marp: true
theme: css/moon2.css
---

## Personal Knowledge Management in AI Era
> Jinyoung Kim & #AI4PKM group

---
## 1. Why PKM?
---
### Vision: Personal Super-intelligence
![[Publish/AI for PKM/_files_/psi-zuke.png]]

---
### Reality: AI usage is still limited
- Writing good prompt *consistently* is hard 
- Limited context in AI applications (e.g. ChatGPT)

> That’s why **context engineering** is getting attention!
---
#### What if we can plug AI directly into our brain?

![[ai-plugged brain.png|608x405]]
AI knows everything I know (or think), and vice versa!

---
### Solution: AI-powered Second brain
1. Pull all my information and knowledge into a repo
2. Organize it for *both* human and AI usage
3. Enable AI-powered tasks with relevant context

This should work using technologies available in 2025!

---
### Project: Building a AI-powered PKM
What's the best we can do in 2025? 

![[PKM Workflow.excalidraw.svg]]

---
### What it enables for me
1. **Ingestion**
	- Pull contents from my reading / memo / lifelog
	- Contents formatted / enriched / summarized
2. **Organization**
	- Build daily/weekly index of all new contents
	- Build topical index of all ingested contents
3. **Creation**
	- Provide draft for social media / essays / msgs
	- Provide ad-hoc research over knowledge base

---
### How it works
Everyday usage (scheduling / writing / research)\
… powered by semi-automated workflows

![[PKM System Architecture.excalidraw.svg]]

---
### How it started
- [[생성형 AI 시대의 데이터 사이언스]] 발표 이후 본격 탐구 (4월)
- 창발 AI4PKM(#ai4pkm) 그룹에서 다른 분들과 논의하며 발전 (5~7월)
- AI4PKM 가이드라인 및 관련 컨텐츠 퍼블리시 (7-8월)

---
#### AI4PKM 그룹 탐구내용 공유
TBA

---
## 2. AI for PKM Deep Dive
![[PKM Workflow.excalidraw.svg]]

---
## Ingestion
1. Various Contents (Readwise)
	- Webpages
	- Books / Papers
	- Youtube
2. Lifelog (Limitless.AI)
	- Conversations
	- Monologues
3. Deep Research Reports
	- Ad-hoc research
	- Proactive research (WIP)

---
### Readwise
내가 읽고 시청하는 컨텐츠를 모두 저장하고 PKM으로 싱크
![[Publish/AI for PKM/_files_/readwise.png]]

---
### Contents Enrichment
![[Enrich Ingested Content (EIC)]]

---
#### Youtube Transcript Enrichment Example
![[Publish/AI for PKM/_files_/PKM in AI Era (slides) 2025-08-17 13.54.01.excalidraw.svg|630x502]]
%%[[PKM in AI Era (slides) 2025-08-17 13.54.01.excalidraw|🖋 Edit in Excalidraw]]%%
유튜브 Transcript가 자동 요약되어 PKM에 저장

---
### Limitless.AI
24시간 동안 내가 듣고 말하는 것을 저장/요약하고 이를 PKM에 저장
![[Publish/AI for PKM/_files_/limitless.png]]

%% ---
#### Connection to Personal Super-intelligence
AI는 우리가 전달하는 컨텍스트만큼 개인화되고 똑똑해진다.

![[Publish/AI for PKM/_files_/limitless-psi.png|558x314]]
Source: [Video from Limitless.AI CEO](https://www.youtube.com/watch?v=PGKc8IckdAw&ab_channel=Limitless)
 %%
---
### Key Points Extraction 
![[Publish/AI for PKM/_files_/PKM in AI Era (slides) 2025-08-17 13.16.33.excalidraw.svg]]
%%[[PKM in AI Era (slides) 2025-08-17 13.16.33.excalidraw|🖋 Edit in Excalidraw]]%%
원본 Lifelog에서 Key Point가 추출 및 요약되어 PKM에 쌓임

---
### Deep Research
AI가 특정 주제에 대해 답변한 결과를 PKM에 저장\
(같은 주제라도 웹/PKM에 물어볼 수 있는 내용이 다름)

| WEB-based Research           | PKM-based Research             |
| ---------------------------- | ------------------------------ |
| 최근 핫한 생산성 관련 책은 뭐야?          | 내가 최근에 생산성 관련해서 배운게 뭐야?        |
| 8세 아이와의 대화법에 대한 자료를 찾아줘.     | 아이와의 대화에서 내가 개선할 수 있는 부분은?     |
| Ambient AI에 대한 연구 트렌드를 요약해줘. | Ambient AI에 대해 내가 최근에 고민한 내용은? |

---
## Organization (조직화)
- Time-based Organization
	- e.g. What did I learning during day/week n?
- Topic-based Organization
	- e.g. What do I know about topic, say, PKM?

> 이런 조직화는 사용자에게 필수적이며,\
> AI의 생산성(비용+품질)에도 도움\
> (검색엔진/데이터베이스의 인덱싱)

---
### Time-based Organization
%% #TODO Create custom visualization %%
![[Publish/AI for PKM/_files_/PKM in AI Era (slides) 2025-08-17 13.26.53.excalidraw.svg|575x419]]
%%[[PKM in AI Era (slides) 2025-08-17 13.26.53.excalidraw|🖋 Edit in Excalidraw]]%%
지식과 경험이 일간/주간/월간/연간 요약되어 쌓임

---
### Topic-based Organization
![[Publish/AI for PKM/_files_/productivity-graph-obsidian.png|712x509]]
지식과 경험이 관심 주제 단위로 쌓이고 이를 그래프로 시각화

---
## Creation
![[Publish/AI for PKM/_files_/PKM in AI Era (slides) 2025-08-17 13.40.58.excalidraw.svg]]
%%[[PKM in AI Era (slides) 2025-08-17 13.40.58.excalidraw|🖋 Edit in Excalidraw]]%%
PKM can support all stages of content creation

---
### Ideation (아이디어 얻기)
매일 수집된 내용으로 Threads 포스팅 아이디어를 생성

![[Publish/AI for PKM/_files_/pkm-ideation-threads.png|650x500]]

---
### From Outlining to Publishing 
PKM 내용을 바탕으로 각종 리서치 수행 및 결과물에 바로 반영

![[PKM Writing Workflow.excalidraw.svg]]
%%[[PKM Writing Workflow.excalidraw|🖋 Edit in Excalidraw]]%%

---
### AI 협업으로 탄생한 작품 예시
TBA

---
### Things to Think Through
- 어디까지 AI에게 맞겨야 하나? 
	- AI가 글을 작성해 준다면 그것은 내 작품인가?
	- 관련) 가수 / 화백 조영남씨 위작 사건 
- 고려할 점
	- 결과물의 품질을 희생하지 않는가?
	- 창작의 경혐 및 과정에서 내가 배우는 점은?
---
## 3. What’s the future?

---
### Mobile / Agent-based PKM


---
## Where should I start?

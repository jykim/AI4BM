## Core Beliefs
1. 마크다운 파일을 이용한 지식관리는 AI가 이해하고 처리하기에 가장 적합한 포맷이다. 그러므로 모든 지식은 마크다운 포맷으로 변환하여 저장 및 관리한다.
2. 코드 데이터로 훈련된 코딩 에이전트는 파일 시스템 기반에 최적화되어 있고, 코딩 에이전트가 훈련된 코드베이스들은 우리가 지식을 관리하듯이 semantical한 구조로 되어있으므로, 코딩 에이전트를 파일 시스템에 기반한 지식 베이스에 적용하면 정확도가 올라간다.
3. 파일 시스템에 기반한 지식 베이스의 자동화는 마치 지식 근로자들이 서로 파일을 주고 받으면서 협업하는것을 모티브 삼아, 시간에 기반한 Cron expression 외에도 운영체제에서 지원하는 파일 생성, 수정, 삭제 이벤트들에 기반하여 자동화가 trigger되는 모델을 사용한다.
## Vision
Orchestrator = 유저와의 인터랙션 포인트
Raw data = 내 지식관리의 근간이 되는 모든 데이터 (마크다운 포맷)
Skills & Prompts = 내 지식관리의 자동화 코드 및 매뉴얼
Knowledge = 자동화와 유저 리뷰를 거쳐 정제된 지식
Dashboard = 내 지식들을 소비할 수 있는 데이터 비주얼라이제이션 앱
![[orch-arch-map.png]]
## Vault
볼트는 Obsidian으로부터 계승한 컨셉입니다. 나의 지식 데이터와 그 지식 데이터를 자동화 Worker 설정 파일들이 들어 있습니다.
## Orchestrator
Orchestrator는 내 볼트와 Worker들을 관장하는 최상위 AI Agent 입니다. Orchestrator가 하는 일들은 다음과 같습니다.
1. 태스크 생성, 실행, 관리
2. 유저와의 인터랙션
	1. 내 볼트에 있는 지식 데이터에 대한 QnA
	2. Worker들을 이용한 복잡한 작업 실행
	3. 기본 LLM과의 가벼운 소통
## Worker
Worker는 자신에게 해당된 작업을 수행하는 수행원 단위입니다. Worker는 다음과 같은 것들로 정의됩니다.
1. Trigger: 어떤 상황에서 작업을 수행하는지에 대한 정의
	1. File creation, File edit, File removal: 운영체제에서 알려주는 File system 이벤트
	2. Cron expression: 특정 시간에 맞게 스케쥴할수 있는 Cron expression
2. Agent: 실제 지식 작업을 하게될 CLI agent
	1. Claude Code CLI
	2. Codex CLI
	3. Gemini CLI
3. Prompt: 작업을 할때 사용하게 되는 커스텀 프롬프트
## Task
각 Worker가 일을 수행할 때에 Input과 Output과 그 작업에 해당하는 내용이 들어있는 .md 파일입니다.

## Workflow
처음 Orchestrator를 실행하면 아무일도 일어나지 않습니다. 모든 작업은 Worker의 Trigger에 의해서 발생하기 때문에, 모든 자동화의 시작은 Worker를 만드는 일입니다.
Worker 탭에 가서 Worker를 생성하는데 필요한 정보는 Trigger, Agent, Prompt 세가지 입니다. 이 세가지를 정의하고 Worker를 생성하면 자동화가 실행될 준비가 된 것입니다.
Orchestrator가 Trigger를 감지하고 실행되면 다음과 같은 작업을 수행합니다.
1. 해당 Task.md파일을 Tasks 폴더에 생성
2. Trigger에 매칭하는 Worker를 spawn하여 Prompt를 구성하여 실행
	1. 시스템 프롬프트 + 에이전트 프롬프트 본문
	2. Trigger 컨텍스트 (Event, Input Path, Task File)
	3. Output 컨텍스트 (Output Directory, Output Type, new_file / update_file 지침)

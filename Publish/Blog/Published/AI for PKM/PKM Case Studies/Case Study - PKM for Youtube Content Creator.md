## Case Study - PKM for Youtube Content Creator
### Problem
#### 1. 이미 제작된 영상 콘텐츠의 재활용 및 리패키징
- 지난 1년 반 동안 제작한 영상들이 다양한 주제를 담고 있는데,  
	지금 보니 몇 가지 큰 주제로 재구성해서 “개정판” 같은 새로운 콘텐츠를 만들 수 있겠다는 생각이 들었습니다.
- 책으로 치면, 기존 내용을 시대 흐름과 개인의 성장을 반영하여 업데이트하는 것이죠.
- 이 작업을 위해서는 기존 영상의 핵심 내용을 잘 구조화하고 연결하는 PKM 시스템이 필요합니다.  
      
#### 2. 강의 준비 시 Insight와 자료의 재활용
- 영상 촬영 당시의 나만의 깨달음이나 설명 방식은 시간이 지나면 잊혀지곤 합니다.  
- PKM을 통해 특정 주제로 강의를 준비할 때, 예전 영상 속 인사이트와 당시 참고했던 외부 자료들을  
    한 번에 모아보고 정리할 수 있기를 원합니다.  
- 이를 통해 더 일관성 있고 깊이 있는 강의 자료를 빠르게 준비할 수 있게 됩니다.  

#### 3. 다국어 콘텐츠 간 연결을 통한 홍보 콘텐츠 제작
- 최근 영어 영상들도 하나둘 업로드하고 있는데, 한국어 시청자들이 접근하기 쉽지 않습니다.  
    (언어 장벽, 자동 자막의 부정확성 등)  
- 그래서 Notebook LM 등을 활용해 영어 영상들을 한국어로 소개하는 콘텐츠(ex. 팟캐스트)로 가공하고자 합니다.  이후에는 반대로 한국어 영상을 영어로 소개하는 콘텐츠로도 확장할 수 있겠지요.  
- PKM은 이런 다국어 간 콘텐츠 연결 및 재구성을 효율적으로 도와줄 수 있을 거라고 생각합니다.  
      
결국 제가 PKM을 통해 이루고 싶은 것은  
📌 **“이미 보유한 콘텐츠와 지식을 체계적으로 연결하여, 콘텐츠 생산성과 품질을 동시에 높이는 것”입니다.**

### Proposed Solution
핵심은 기존 보유한 방대한 컨텐츠와 앞으로도 계속 쏟아질 새로운 컨텐츠를 일관된 체계로 통합하는 구조를 만드는 것이 아닐까 합니다. 이를 위해 아래 몇가지 단계를 제안드려 봅니다. (아래 다이어그램 참고)

1. 기존 강의안을 Topic Knowledge로 재구조화[^1]
	- 주제별로 나는 어떤 내용을 전달하고, 인사이트를 줄 수 있는가?
2. 새로운 지식을 Topic Knowledge에 추가하는 Workflow 구현
	- 새로운 지식이 기존 지식 체계에 자연스럽게 통합되도록
3. 이를 바탕으로 다양한 컨텐츠 제작 가능
	- 다른 포멧: 강의 자료 및 SNS 포스트
	- 다른 언어: 한글 및 영어 컨텐츠

![[Publish/AI for PKM/_files_/8. Case Studies AI-powered PKM 2025-09-03 10.21.09.excalidraw.svg]]
%%[[8. Case Studies AI-powered PKM 2025-09-03 10.21.09.excalidraw|🖋 Edit in Excalidraw]]%%

도구 측면에서는 (1,2)는 옵시디언+CLI Agent를 사용하시는게 어떨까 싶고요, (3)은 컨텐츠 포멧에 따라 적절한 도구를 사용하시면 됩니다. 저는 창작에 최대한 PKM을 활용할 수 있도록 원본 컨텐츠를 .md형식으로 만들고, (예: [[2025-08-01 PKM in AI Era (slides)]]) 이를 전문 애플리케이션으로 변환하는 (예: [gamma.app slide](https://gamma.app/docs/AI-PKM-0h4evcue8etumcu?mode=doc)) 접근법을 사용하고 있어요.

1. 기존 강의안을 Topic Knowledge로 재구조화[^1]
	- Youtube Transcript → Topic-level MD file
2. 새로운 지식을 Topic Knowledge에 추가하는 Workflow 구현
	- [[(dep) Daily Ingestion and Roundup (DIR)]] 변형
3. 이를 바탕으로 다양한 컨텐츠 제작 가능
	- Slide: https://gamma.app/
	- Podcase: Notebook LM

[^1]: Topic Index가 아니라도 구조화 방법은 여러가지가 있을것 같습니다. 그리고 Topic Index는 문자 그대로 기존 자료의 (강의 노트) 주제별 핵심 내용을 향후 재사용을 위해 발췌하는 용도라고 생각하시면 됩니다. 

### 참고자료
- [[Case Study - Youtube Creator (claude code)]]
- [[Case Study - Youtube Creator (gemini cli)]]
- [[Case Study - Youtube Creator (gpt5 via cursor)]]

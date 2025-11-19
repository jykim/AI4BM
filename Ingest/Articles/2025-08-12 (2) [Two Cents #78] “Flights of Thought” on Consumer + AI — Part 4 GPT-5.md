---
author: Substack
category: articles
source: reader
date: 2025-11-18
URL: https://twocents.xyz/p/two-cents-78-flights-of-thought-on?utm_source=unread-posts-digest-email&inbox=true&utm_medium=email&triedRedirect=true
---
Substack #reader

## Summary
Consumer AI에 대한 ‘시장의 준비’가 tipping point를 넘어 가고 있는 것으로 보인다.

## Highlights
**시나리오 2: (좀 더 wild한 상상의 나래를 펼쳐 보면)** 
아직까지 시장에 등장하지 않았지만, 나는 조만간 “각 개인의 personal data” (일정, 연락처, 이메일, 건강 데이터, 가족 연결 데이터 등) 기반으로 fine-tuned된 "‘personalized LLM’이 등장할 수 있다고 예상한다.
더 상상해 보면, 이러한 ‘personalized LLM’도 하나에 그치지 않고, 영역별로 (개인, 가족, 업무(회사/직업을 바꾸게 되면 그에 따라 또 새롭게 만들어질 수 있는) 등) 나만의 personalized LLM이 여러 개 공존할 수도 있을 것이다.
(기술적으로는 큰 장벽이 있지는 않아 보이고, 비용도 시간 문제로 각 개인이 afford할 수 있는 수준으로 내려 올 것으로 예상된다. 오히려 가장 큰 bottleneck은 각 개인의 데이터를 어떻게 모으고 이에 대하여 각 개인이 소유권/주도권을 주장할 수 있을지가 될 듯 하다. 특히 아이폰 건강 데이터, Spotify playlist 등과 같이 기존 웹/모바일 서비스에 파편화되고 silo되어 저장되어 있는 개인 데이터들)
즉, 나의 개인화된 데이터가 (매번 어떤 요청 (aka, LLM prompt)마다 제공되는) context data로 제공되는 수준을 넘어서, 나의 데이터에 특화된 (fine-tuned된) personalized LLM을 통하여 persistent하게 활용되는 개인화된 (AI) 환경을 만들 수 있다는 의미가 된다.
나에 특화된 이러한 personalized LLM(들)이 만들어지고 (나만의) Model Router가 이들을 access할 수 있게 되면, 진정한 나에게 특화된 LLM Model, 더 나아가서 나에게 특화된 personal Assistant가 만들어지는 것이 아닐까?
Model Router는 이렇게까지 개인화가 확장되는 시작점이 될 수 있을 듯 하다. ([View Highlight](https://read.readwise.io/read/01k2fh4xs239gbta0tqb7hrqge))

Free-form function call은 완전히 새로운 개념은 아니고, 기존 MCP Server가 request를 처리하는 방식과 기본적으로는 같은 구조이다. 즉 tool/function call의 input은 (prompt 방식의) free text이고, 이를 tool/function이 해석해서 필요한 action을 취하는 구조.
차이점으로는, MCP Server는 이를 외부 서비스/데이터 소스에 대한 API call로 변환하여 ‘one-shot’ 호출하는 상대적으로 단순한 구조이고, GPT-5에서의 function call은 이를 더 일반화한 구조이다. 즉, API call로 변화하여 호출하는 방식 외에도, 다른 tool/LLM에 대하여 (다시 prompt 형식으로) nested function call을 할 수 있고, API call 혹은 tool/function call의 결과 값을 분석하여 다시 새로운 API call 혹은 (nested) tool/function call을 추가로 하고, 등등.
이런 일반화된 tool call 구조을 보면, 이 tool/function call이 결국은 (단순히 API call을 prompt 요청으로 encapsulate한 MCP Server 방식 보다) 더 일반화된 agent sub-system에 대한 tool calling 구조를 띈다는 점을 깨닫게 된다.즉, GPT-5의 tool/function call은 (MCP 구조를 확장한) agent (sus-system)에 대한 tool calling으로 ‘일반화’되었다는 것을 의미한다.
([GPT-5 Hands-On: Welcome to the Stone Age](https://www.latent.space/p/gpt-5-review)에서 이러한 구조를 (LLM 기반) ‘tool’ 사용을 본격화 & 일반화의 시작점으로 보는, 그래서 GPT-5를 (인간의 문명을 가능하게 한 도구 사용의 시작점으로서의 ‘석기 시대’에 빗대어) AGI를 향한 ‘석기 시대’의 시작이라고 부르는 이유이다.) ([View Highlight](https://read.readwise.io/read/01k2fhf8037qh0v4j0755qhavt))


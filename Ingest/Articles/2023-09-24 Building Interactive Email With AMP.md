---
author: Pinterest Engineering
category: articles
source: medium
date: 2025-11-18
URL: https://medium.com/p/2a90969c0093
---
Pinterest Engineering #medium

## Highlights
When Gmail client catches a Pinterest action, it will send out the GET/POST request to Google. Google then generates and attaches a security token for this request and relays the request to Pinterest. After our service receives the request, we call Google to validate that token before we return any user info.

AMP email also gives Pinterest chances to gather user feedback more easily. For example, Pinners can let us know if they don’t like a Pin that’s been recommended, which is feedback that ultimately makes their overall Pinterest experience more relevant


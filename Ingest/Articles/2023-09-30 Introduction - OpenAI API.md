---
author: openai.com
category: articles
source: reader
date: 2025-11-18
URL: https://platform.openai.com/docs/plugins/introduction
---
openai.com #reader

## Summary
OpenAI platform allows developers to build plugins that connect ChatGPT with third-party applications, enabling the AI model to perform a wide range of actions. These plugins can retrieve real-time information, retrieve knowledge-base information, and assist users with actions. Developers create API endpoints, a manifest file, and an OpenAPI specification to define the plugin's functionality. The AI model proactively calls the APIs based on natural language descriptions and incorporates the API data into its responses. To build a plugin, developers need to create a manifest file, register the plugin in the ChatGPT UI, and activate it for users.

## Highlights
The AI model acts as an intelligent API caller. Given an API spec and a natural-language description of when to use the API, the model proactively calls the API to perform actions. For instance, if a user asks, "Where should I stay in Paris for a couple nights?", the model may choose to call a hotel reservation plugin API, receive the API response, and generate a user-facing answer combining the API data and its natural language capabilities. ([View Highlight](https://read.readwise.io/read/01hbm5e3m7jxsqx8jmbp3at3dg))


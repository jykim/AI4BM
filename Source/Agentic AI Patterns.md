---
title: "Agentic AI Patterns and Frameworks"
source: "https://www.anthropic.com/research/building-effective-agents"
author:
  - "Anthropic Research"
created: 2024-03-15
tags:
  - source
  - framework
  - ai-agent
  - architecture
status: ready
cited_by:
  - "[[Projects/New Architecture for Agentic AI]]"
  - "[[Theory/AI4PKM Framework]]"
---

## Summary
Agentic AI systems are characterized by their ability to operate autonomously, make decisions, use tools, and complete complex multi-step tasks. This framework outlines patterns for building effective AI agents including workflow orchestration, tool use, evaluation loops, and human-in-the-loop designs.

## Key Concepts
- **Autonomous Decision Making**: Agents choose actions based on context and goals rather than following fixed scripts
- **Tool Use**: Ability to invoke external functions, APIs, and services to accomplish tasks
- **Planning and Decomposition**: Breaking complex goals into executable sub-tasks
- **Memory and Context**: Maintaining state across interactions and learning from past actions
- **Evaluation and Self-Correction**: Assessing outputs and iterating to improve quality

## Agentic Workflows

### Pattern 1: Prompt Chaining
Sequential execution of specialized prompts, where each step's output feeds the next.

**Use Cases**:
- Multi-stage content processing (capture → clean → summarize → publish)
- Data pipelines with transformation steps
- Quality assurance workflows (generate → review → revise)

### Pattern 2: Routing
Directing requests to specialized sub-agents based on task type or domain.

**Use Cases**:
- Multi-domain PKM (code vs writing vs research)
- Language-specific processing (Korean vs English)
- Format-specific handlers (video vs text vs audio)

### Pattern 3: Parallelization
Running multiple independent tasks concurrently for efficiency.

**Use Cases**:
- Batch processing captured notes
- Multi-source data ingestion (Limitless + Photos + Clippings)
- Concurrent topic index updates

### Pattern 4: Orchestrator-Workers
Central coordinator delegates specialized tasks to worker agents.

**Use Cases**:
- Complex PKM workflows with multiple processing stages
- Multi-agent collaboration (Claude + Gemini + Codex)
- Task queue management with priority routing

### Pattern 5: Evaluator-Optimizer
Secondary agent evaluates primary agent's output and provides feedback for iteration.

**Use Cases**:
- Content quality control (draft → review → improve)
- Knowledge graph validation (detect errors, suggest fixes)
- Automated testing and refinement loops

## Implementation Patterns

### Human-in-the-Loop (HITL)
**Principle**: Keep humans involved at critical decision points while automating routine tasks.

**PKM Applications**:
- Final review before publishing content
- Disambiguation of ambiguous references
- Personal preference decisions (categorization, tagging)
- Quality threshold enforcement

**Benefits**: Maintains human judgment while reducing cognitive load

### Safeguards and Guardrails
**Principle**: Prevent destructive actions through validation and constraints.

**PKM Applications**:
- Read-only mode for exploratory operations
- Backup before batch modifications
- Explicit confirmation for deletions
- Dry-run mode for testing workflows

### Progressive Autonomy
**Principle**: Start with high human oversight, gradually automate as confidence builds.

**Stages**:
1. **Assisted**: Agent suggests, human executes
2. **Semi-Autonomous**: Agent executes, human reviews
3. **Autonomous**: Agent operates independently with periodic audits

## Notable Quotes
> "The most effective agents combine multiple patterns, using orchestration to coordinate specialized sub-agents."
> — On architectural composition

> "Human-in-the-loop is not a limitation but a design principle that preserves agency while leveraging automation."
> — On HITL philosophy

## Common Pitfalls

### Over-Automation
Automating tasks that benefit from human intuition or creativity.

**Solution**: Identify tasks where human judgment adds unique value (creative writing, personal reflection, strategic decisions)

### Rigid Workflows
Fixed sequences that can't adapt to varying inputs or contexts.

**Solution**: Build flexible routing with fallback mechanisms and exception handling

### Context Loss
Agents forgetting relevant information from earlier interactions.

**Solution**: Implement explicit memory systems (conversation logs, knowledge graphs, session state)

### Evaluation Gaps
No mechanism to assess quality or catch errors.

**Solution**: Add evaluator agents or validation steps before finalizing outputs

## Best Practices

### 1. Start Simple, Add Complexity
Begin with single-agent workflows, introduce orchestration only when needed.

### 2. Make Workflows Observable
Log agent decisions, intermediate outputs, and execution traces for debugging.

### 3. Design for Failure
Assume agents will make mistakes; build recovery mechanisms.

### 4. Optimize for Iteration Speed
Faster feedback loops enable quicker refinement of agent behaviors.

### 5. Measure What Matters
Define success metrics aligned with user goals (time saved, quality improved, insights generated).

## Relevance to AI4PKM
These patterns are foundational for building PKM systems where multiple agents collaborate:

**Multi-Agent Architecture**:
- Claude Code: Batch workflows, file operations
- Gemini: Video/audio processing
- Codex: Quick queries and roundups

**Workflow Automation**:
- Daily Ingestion: Parallel capture from multiple sources
- Knowledge Graph Update: Evaluator loop for link validation
- Content Production: Orchestrator chains specialized agents

**Quality Control**:
- HITL for personal content review
- Evaluator agents for factual accuracy
- Progressive autonomy as trust builds

## Related Sources
- [[Source/Claude Code]]
- [[Source/Model Context Protocol]]
- [[Source/Multi-Agent Systems]]
- [[Source/Prompt Engineering Best Practices]]

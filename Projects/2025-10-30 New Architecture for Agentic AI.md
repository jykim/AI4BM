## Background
[On-demand Knowledge Task Processing](https://jykim.github.io/AI4PKM/blog/2025/10/20/on-demand-knowledge-task.html):
* Opened door for more general Agentic AI for PKM

We thought -- Can we generalize the notion of agents still?
- What if we let users define agents from the prompts?

Future of AI4PKM
* Open source framework (agents/prompts/skills)
* Desktop app with better usability and features (@Minsuk)

## User Values (updated)
Runtime environment for user-defined knowledge tasks (prompts)
* By file system trigger / By calendar events (TBA)
* Multiple CLI agent support (Claude/Codex/Gemini)
Minimize hurdle for non-technical users (via Mac app)
* One-click install of all necessary packages
* UI for PKM config & workflow monitoring
Voice command for PKM interaction (via Mac app)
* Knowledge task management
* Quick-turnaround tasks

## Components
### Orchestrator
Orchestrator Config
- Agent-level Config
	- Input: path / type (new_file / updated_file)
	- Output: path / type
	- Preferred CLI agent (Claude/Codex/Gemini)
- System parameters
	- Concurrency level
	- Max token usage (optional)

### Task
Unit task description given to an Agent by Orchestrator
* Managed in Markdown file for transparency
* Mostly the same [as the previous architecture](https://jykim.github.io/AI4PKM/blog/2025/10/20/on-demand-knowledge-task.html)

### Agent
Runtime for each Task; Abstraction for CLI agents
Agent Config (in Task file)
- Prompts (in `Prompts` folder)
- Input/Output (in Orchestrator config)

![[Orch-Agent-Architecture.excalidraw.svg]]
%%[[Orch-Agent-Architecture.excalidraw|🖋 Edit in Excalidraw]]%%

## PKM Ecosystem
### Mac App (new)
Provide easier route for insteall/monitoring

### Obsidian
Markdown doc viewer / editor
Content link graph viewer
Content database (Base) viewer/editor

### Code Editor + CLI Agent
For interactive agentic workflow
* AI-assisted writing with diff review

## FAQ
### What prior knowledge is required?
With Mac App, most of technical hurdles are removed
1. Installing Mac App also setup environments
2. Setting up Agents will be as easy as setting up input/output in Mac App

### How do I integrate into existing Obsidian vault?
At minimum, following folders will be needed to set up the AI4PKM now.
New users can still elect to create a demo vault using the Mac App.

```
orchestrator:
  prompts_dir: "_Settings_/Prompts"
  tasks_dir: "_Settings_/Tasks"
  logs_dir: "_Settings_/Logs"
```
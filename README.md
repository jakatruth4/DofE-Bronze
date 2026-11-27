  # [Building claude code from scratch] - Bronze DofE 6-Month Skills Project

An autonomous AI coding assistant built over 6 months for my **Bronze Duke of Edinburgh's Award (Skills Section)**, designed to inspect codebases, edit files, execute shell commands, and iterate through multi-step tasks using Large Language Models (LLMs).

Progress is documented through regular Git commits across the 26-week period.

---

## DofE Overview

* **Award Level:** Bronze
* **Section:** Skills (6-month option)
* **Timeframe:** [24/11/26] - [24/5/27] (26 weeks, roughly 1 hour per week)


### Project Aim
To build a functional AI coding agent from scratch—covering REST API integration, structured tool calling, an autonomous think-act-observe loop, safe file and command execution, and advanced capabilities such as interactive mode, ACP support, and LSP integration.

---

## Core Architecture and Agent Loop

At the center of the assistant is an iterative agent loop that lets the model reason about a task, call tools to gather context or modify code, inspect tool outputs, and repeat until the goal is achieved or a stopping condition is reached.

1. **LLM REST API Integration:** Send structured prompts, conversation history, system instructions, and tool schemas to an LLM endpoint, handling responses and error states cleanly.
2. **Tool Definitions and Execution:** Expose concrete capabilities to the model (such as reading files, writing or patching code, searching repositories, and running shell commands) with strict argument validation and permission checks.
3. **Think - Act - Observe Loop:** Feed tool execution results back into the model's context so it can verify changes, catch errors from test or build commands, and self-correct across turns.

For example, given an instruction like *"Refactor `main.py` to use a class"*, the agent can read the existing file, plan the structural change, apply the updated code, and run checks to verify the result.

---

## Planned Features and Roadmap

### Phase 1: Core Agent and Tooling
* [ ] Connect to an LLM via a REST API with structured message and tool handling
* [ ] Implement core filesystem and execution tools (file reading, file creation/editing, directory/code search, and command execution)
* [ ] Build the core agent loop to think, execute tools, observe outputs, and iterate until completion
* [ ] Add basic safeguards and confirmation prompts before destructive edits or commands

### Phase 2: Context, Reliability, and Workflows
* [ ] Manage context effectively across multi-turn sessions and larger codebases
* [ ] Handle malformed tool calls, command failures, and edge cases without crashing the session
* [ ] Support diff previews and clean inspection of proposed file changes

### Phase 3: Advanced Capabilities
* [ ] **Interactive Mode:** Persistent terminal/session interaction with ongoing state, commands, and live feedback
* [ ] **ACP Support:** Implement Agent Client Protocol support for structured client-agent communication
* [ ] **LSP Servers:** Integrate Language Server Protocol support for richer code intelligence, diagnostics, symbols, and navigation

---

## 6-Month Timeline

* **Month 1 - Project Setup and REST API Client:** Initialize the repository, define project layout, and connect to an LLM REST API with basic prompt/response handling.
* **Month 2 - Tool Calling and Agent Loop:** Define tool schemas, implement file and command tools, and build the iterative think-act-observe loop.
* **Month 3 - File Editing, Diffs, and Safety:** Refine file modification workflows, error handling, and command execution guardrails.
* **Month 4 - Interactive Mode:** Build a responsive interactive mode supporting multi-step tasks, session flow, and user feedback.
* **Month 5 - ACP and LSP Integration:** Add ACP support and wire in LSP server capabilities for code diagnostics and context.
* **Month 6 - Testing, Refinement, and Sign-Off:** Test across real coding tasks, fix edge cases, document findings in `/docs` and complete assessor review.

---

## Repository Structure

```text
├── src/
│   ├── agent/          # Agent loop, prompt/message state, and orchestration
│   ├── api/            # LLM REST API client and request/response handling
│   ├── tools/          # File read/write/patch, search, and shell command tools
│   ├── acp/            # Agent Client Protocol integration
│   └── lsp/            # Language Server Protocol client and diagnostics
├── docs/               # Notes, diagrams, and testing captures
└── README.md           # Project overview, architecture, and setup guide

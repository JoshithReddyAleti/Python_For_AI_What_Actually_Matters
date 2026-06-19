# 🗺️ AI Engineering Roadmap 2026

> Full curriculum from the [AI Engineering Roadmap 2026 Newsletter](https://www.linkedin.com/newsletters/ai-engineering-roadmap-2026-7467249724752908288/)

This roadmap is designed to take you from knowing what an LLM is, to being able to build, validate, and deploy real AI systems. Each episode comes with a GitHub project, a LinkedIn carousel, and a concept explanation.

---

## The Core Idea

Most people learning AI stop at one of two places:

**Stop 1 — The Experimenter**
> "I can use ChatGPT, write prompts, and build a basic chatbot."

**Stop 2 — The Tutorial Follower**
> "I've followed some LangChain tutorials and built a RAG app."

Neither of those is an AI engineer.

An AI engineer builds **systems** — things that decide, act, validate, and recover. This roadmap teaches that.

---

## The 5-Layer Mental Model

Every episode maps back to these 5 layers. Master all 5 and you're an AI engineer.

```
┌──────────────────────────────────────────────────────┐
│  Layer 1: LLM          → The decision-maker          │
│  Layer 2: Tools        → Capabilities                │
│  Layer 3: State        → Context + memory            │
│  Layer 4: Orchestration → Workflow control           │
│  Layer 5: Validation   → Reliability                 │
└──────────────────────────────────────────────────────┘
```

Most beginners only reach layers 1–2. That's why their systems break.

---

## Full Episode Guide

### ✅ Episode 1 — What Is an LLM, Really?
**Core question:** What's actually happening when you "talk to AI"?

**What you'll learn:**
- Tokens, context windows, and temperature
- Why LLMs are probabilistic, not deterministic
- What "training" actually means
- The difference between a model and a product

**Key insight:** LLMs predict the next token. That's it. Everything else is engineering around that.

**Project:** None — conceptual foundation episode.

---

### ✅ Episode 2 — Python for AI: What Actually Matters
**Core question:** What Python do you actually need to build AI systems?

**What you'll learn:**
- Functions, classes, and modules (the essentials)
- Working with dicts and JSON (the AI data format)
- Making HTTP requests
- Using environment variables for API keys
- Reading and writing files

**Key insight:** You don't need to know all of Python. You need to know the 20% that AI systems actually use.

**Project:** A simple script that calls the OpenAI API, reads a prompt from a file, and saves the response to a JSON file.

---

### 🔥 Episode 3 — Tool Calling, APIs & Validation ← You are here
**Core question:** How do you build an AI system that does things, not just says things?

**What you'll learn:**
- Tool calling and the router pattern
- External API integration
- Structured outputs with JSON + Pydantic
- Validation and retry logic
- The 5-layer mental model of AI systems

**Key insight:** The jump from "LLM app" to "AI system" happens when your code can: Decide → Act → Validate → Recover.

**Project:** [This repo](https://github.com/YOUR_USERNAME/tool-using-ai-assistant) — a modular tool-using assistant with calculator, weather API, validation, and tests.

---

### 🔜 Episode 4 — Your First End-to-End AI Project
**Core question:** How do you go from idea to a finished project you can show in an interview?

**What you'll learn:**
- Project scoping (the #1 skill beginners lack)
- How to structure a project for GitHub
- Writing a README that impresses
- Connecting the 5 layers into one working system
- Interview storytelling

**Key insight:** A project without a story is just code. A story without code is just talk. You need both.

**Project:** An expanded version of the tool-using assistant with a proper CLI or Streamlit UI.

---

### 🔜 Episode 5 — RAG: Connecting AI to Your Data
**Core question:** How do LLMs work with your own documents and data?

**What you'll learn:**
- What RAG (Retrieval-Augmented Generation) actually is
- Vector embeddings and similarity search
- Building a simple document Q&A system
- Chunking, embedding, and retrieval strategies
- When to use RAG vs fine-tuning

**Key insight:** RAG is not magic. It's retrieval + context injection + generation. Understanding each step separately is what makes you dangerous.

**Project:** A document Q&A system — give it a PDF, ask it questions.

---

### 🔜 Episode 6 — Memory and State in AI Systems
**Core question:** How do you build an AI that remembers things across turns?

**What you'll learn:**
- The difference between short-term and long-term memory
- Conversation history management
- External memory stores (Redis, SQLite, vector DBs)
- State machines for multi-turn conversations

**Key insight:** Stateless LLMs + stateful engineering = memory. The model doesn't remember. Your code does.

---

### 🔜 Episode 7 — Agents: When AI Systems Make Decisions
**Core question:** What is an AI agent and when should you build one?

**What you'll learn:**
- ReAct pattern (Reason + Act)
- Planning and multi-step reasoning
- Tool selection under uncertainty
- When agents fail (and how to recover)
- LangGraph basics for agent orchestration

**Key insight:** An agent is just a loop: observe → think → act → observe again. The engineering challenge is making that loop reliable.

---

### 🔜 Episode 8 — Evaluation: How Do You Know Your AI Works?
**Core question:** How do you measure whether your AI system is actually doing its job?

**What you'll learn:**
- Why "it looks right" is not an evaluation strategy
- LLM-as-judge evaluation
- Building an eval dataset
- Measuring hallucination, relevance, and groundedness
- Regression testing for AI outputs

**Key insight:** If you can't measure it, you can't improve it. Eval is the most neglected skill in AI engineering.

---

### 🔜 Episode 9 — Deployment: Taking AI Systems to Production
**Core question:** How do you go from a local script to something you can share with the world?

**What you'll learn:**
- Wrapping your system in a FastAPI endpoint
- Environment management (dev, staging, prod)
- Secrets management
- Basic rate limiting and error handling
- Deploying to Railway, Render, or Fly.io

**Key insight:** A system that only runs on your laptop is a demo. A system with a URL is a product.

---

### 🔜 Episode 10 — Observability: Knowing What Your AI is Doing
**Core question:** How do you monitor an AI system in production?

**What you'll learn:**
- Logging for AI systems (structured logs)
- Tracing multi-step AI pipelines
- Tools: Langfuse, Helicone, OpenTelemetry
- Alerting on AI failures
- Cost monitoring (API spend)

**Key insight:** You can't fix what you can't see. Production AI without observability is flying blind.

---

## Skill Progression

```
Episode 1-2:   Foundation     → You understand what's happening
Episode 3-4:   Builder        → You can build systems
Episode 5-6:   Practitioner   → You can connect AI to real data
Episode 7-8:   Engineer       → You can build and measure agents
Episode 9-10:  Professional   → You can ship and operate AI systems
```

---

## Learning Principles

**Build first, understand after.**
Don't wait until you fully understand something to start building. Build, observe, then understand what you built.

**Small and working beats big and broken.**
A simple tool-using assistant that actually works is worth 10 complex "architectures" that don't run.

**Tests are documentation.**
Write tests for your AI systems. They show hiring managers you think like an engineer, not a tutorial follower.

**Systems thinking over model thinking.**
The LLM is one component. The system is what matters. Always think about the whole pipeline.

---

## Community and Resources

- 📬 [Subscribe to the newsletter](https://www.linkedin.com/newsletters/ai-engineering-roadmap-2026-7467249724752908288/)
- ⭐ Star this repo to follow along with new episodes
- 💬 Open an issue if you're stuck on anything
- 🤝 PRs welcome — add tools, fix bugs, improve tests

---

*AI Engineering Roadmap 2026 — Built for serious learners.*

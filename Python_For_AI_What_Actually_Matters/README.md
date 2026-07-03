# 🐍 Python For AI — What Actually Matters

> **Episode 2 of the [AI Engineering Roadmap 2026](https://www.linkedin.com/newsletters/ai-engineering-roadmap-2026-7467249724752908288/) Newsletter Series**
>
> *"You don't need to know all of Python. You need to know the 20% that AI systems actually use."*

---

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![Beginner Friendly](https://img.shields.io/badge/Level-Beginner%20Friendly-22C55E?style=flat-square)
![Hands On](https://img.shields.io/badge/Style-Hands%20On-F59E0B?style=flat-square)
![Episode](https://img.shields.io/badge/Episode-2%20of%2010-534AB7?style=flat-square)

**[📖 Newsletter](https://www.linkedin.com/newsletters/ai-engineering-roadmap-2026-7467249724752908288/) · [⬅️ Episode 1](https://github.com/JoshithReddyAleti/Understanding_LLMs_From_The_Inside_Out) · [➡️ Episode 3](https://github.com/JoshithReddyAleti/Building_AI_Project-Blueprint_for_Begin) · [🗺️ Roadmap](docs/ROADMAP.md)**

</div>

---

## 🎯 What Is This?

Most Python tutorials teach you Python.

This repo teaches you **Python for AI** — specifically the patterns, tools, and concepts that appear in almost every AI project you'll ever build.

You don't need to memorise Python. You need to recognise and use these patterns fluently:

| Pattern | Where You'll Use It |
|---|---|
| Functions and classes | Organising AI system logic |
| Dicts and JSON | The universal AI data format |
| HTTP requests | Calling LLM APIs and external tools |
| Environment variables | Managing API keys safely |
| File I/O | Reading prompts, saving outputs |
| Error handling | Making systems that don't crash |
| List comprehensions | Processing API responses cleanly |
| Dataclasses | Modelling system state |

Every item in this repo is something you'll use in Episode 3 and beyond.

---

## 📋 Prerequisites

- You've read [Episode 1](https://github.com/JoshithReddyAleti/Understanding_LLMs_From_The_Inside_Out) (you understand what an LLM is)
- You have Python 3.10+ installed (`python --version`)
- You have a text editor (VS Code recommended)

That's it. No prior Python required — but having seen basic Python before will help.

---

## 🗂️ What's In This Repo

```
Python_For_AI_What_Actually_Matters/
│
├── core/                          # The essential Python patterns
│   ├── 01_functions_and_classes.py    # Organising AI logic
│   ├── 02_dicts_and_json.py           # The AI data format
│   ├── 03_http_requests.py            # Calling APIs
│   ├── 04_environment_variables.py    # Managing secrets safely
│   ├── 05_file_io.py                  # Reading prompts, saving outputs
│   ├── 06_error_handling.py           # Making robust systems
│   ├── 07_list_comprehensions.py      # Cleaning API responses
│   └── 08_dataclasses.py             # Modelling state
│
├── mini_projects/                 # Apply everything together
│   ├── api_caller/
│   │   ├── llm_api_caller.py          # Make your first LLM API call
│   │   └── README.md
│   ├── prompt_runner/
│   │   ├── prompt_runner.py           # Load prompt from file, call LLM, print response
│   │   ├── prompts/
│   │   │   └── sample_prompt.txt
│   │   └── README.md
│   └── response_saver/
│       ├── response_saver.py          # Call LLM, validate response, save to JSON
│       └── README.md
│
├── exercises/
│   ├── exercises.md               # 10 exercises to solidify the concepts
│   └── solutions/                 # Solutions (try the exercises first!)
│       └── solutions.md
│
├── docs/
│   ├── ROADMAP.md                 # Full 10-episode roadmap
│   ├── CONCEPTS.md                # Deeper explanations of each concept
│   └── CHEATSHEET.md             # Quick reference — the patterns at a glance
│
├── .env.example
├── requirements.txt
└── README.md
```

---

## 🧩 The 8 Patterns You Must Know

### 1. Functions and Classes — Organise Your Logic

```python
# Functions do one thing and return something
def call_llm(prompt: str, temperature: float = 0.7) -> str:
    """Always type-hint your functions. It helps you and your readers."""
    response = client.chat.completions.create(...)
    return response.choices[0].message.content

# Classes group related data and behaviour
class AssistantConfig:
    def __init__(self, model: str, temperature: float):
        self.model = model
        self.temperature = temperature

    def to_dict(self) -> dict:
        return {"model": self.model, "temperature": self.temperature}
```

**Why it matters for AI:** Every AI system is a collection of components. Functions and classes are how you build components that are testable, reusable, and replaceable.

---

### 2. Dicts and JSON — The AI Data Format

```python
# This is what LLM API calls look like
message = {
    "role": "user",
    "content": "What is 25% of 480?"
}

# This is what responses look like
response = {
    "tool": "calculator",
    "result": 120.0,
    "confidence": 0.99
}

# Converting to/from JSON strings
import json
json_string = json.dumps(response)           # dict → string
parsed_back = json.loads(json_string)        # string → dict

# Safely accessing nested values
tool = response.get("tool", "direct")        # never use response["tool"] blindly
result = response.get("result")              # returns None if missing, not KeyError
```

**Why it matters for AI:** Every API response is a dict. Every tool output is a dict. Every system state is a dict. If you're not fluent with dicts, you'll be confused constantly.

---

### 3. HTTP Requests — Calling APIs

```python
import requests

# GET request (fetching data)
response = requests.get(
    "https://api.open-meteo.com/v1/forecast",
    params={"latitude": 51.5, "longitude": -0.1, "current": "temperature_2m"},
    timeout=10  # always set a timeout
)

response.raise_for_status()     # raises an error if status >= 400
data = response.json()          # parse JSON response
temp = data["current"]["temperature_2m"]

# POST request (sending data — like calling the OpenAI API)
response = requests.post(
    "https://api.openai.com/v1/chat/completions",
    headers={"Authorization": f"Bearer {api_key}"},
    json={"model": "gpt-4o-mini", "messages": [...]},
    timeout=30
)
```

**Why it matters for AI:** Tool calling (Episode 3) means calling APIs. Every external data source your AI uses requires an HTTP request.

---

### 4. Environment Variables — Never Hardcode Secrets

```python
# ❌ NEVER DO THIS
api_key = "sk-abc123yourrealkey"   # If you commit this to GitHub, it's compromised

# ✅ Always do this
import os
from dotenv import load_dotenv

load_dotenv()                              # reads from .env file
api_key = os.environ.get("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not set. Check your .env file.")
```

**.env file (never commit this):**
```
OPENAI_API_KEY=sk-abc123yourrealkey
```

**.env.example (commit this — shows what keys are needed, with fake values):**
```
OPENAI_API_KEY=sk-your-key-here
```

**Why it matters for AI:** Every AI project uses API keys. Leaking them costs money and gets your account banned. This is non-negotiable.

---

### 5. File I/O — Reading Prompts, Saving Outputs

```python
# Reading a prompt from a file (much cleaner than hardcoding in Python)
with open("prompts/routing_prompt.txt", "r") as f:
    prompt_template = f.read()

# Filling in the template
prompt = prompt_template.format(query=user_query, options="calculator, weather, direct")

# Saving a response to JSON
import json
from datetime import datetime

result = {"query": user_query, "response": response, "timestamp": datetime.now().isoformat()}

with open("outputs/response.json", "w") as f:
    json.dump(result, f, indent=2)
```

**Why it matters for AI:** In Episode 3, all prompts live in `.txt` files in `app/prompts/`. Keeping prompts separate from code means you can edit them without touching Python.

---

### 6. Error Handling — Making Systems That Don't Crash

```python
# Basic try/except
try:
    response = call_api()
    data = response.json()
except requests.Timeout:
    print("API timed out — try again")
except requests.HTTPError as e:
    print(f"API error: {e.response.status_code}")
except Exception as e:
    print(f"Unexpected error: {e}")

# Providing a safe fallback
def get_weather(city: str) -> dict:
    try:
        return fetch_from_api(city)
    except Exception as e:
        return {"error": str(e), "temperature": None, "condition": None}
    # Never crash — always return something

# Using finally for cleanup
def process_file(path: str):
    f = None
    try:
        f = open(path, "r")
        return f.read()
    except FileNotFoundError:
        return ""
    finally:
        if f:
            f.close()  # always runs, even if there's an error
```

**Why it matters for AI:** LLM APIs fail. Networks time out. Responses are malformed. A system without error handling will crash in production. Episode 3's validator.py is entirely built on this concept.

---

### 7. List Comprehensions — Processing Responses Cleanly

```python
# Standard pattern in AI: process a list of responses
responses = ["  Hello  ", "  World  ", "", "  AI  "]

# ❌ Verbose version
cleaned = []
for r in responses:
    if r.strip():
        cleaned.append(r.strip())

# ✅ Clean version (list comprehension)
cleaned = [r.strip() for r in responses if r.strip()]
# Result: ["Hello", "World", "AI"]

# Extracting specific fields from API response
messages = response["choices"]
texts = [msg["message"]["content"] for msg in messages]

# Filtering tool outputs
valid_results = [r for r in results if r.get("error") is None]
```

**Why it matters for AI:** API responses always come as lists. You'll constantly need to filter, extract, and transform them. List comprehensions are the idiomatic Python way.

---

### 8. Dataclasses — Modelling System State

```python
from dataclasses import dataclass
from typing import Optional

@dataclass
class QueryState:
    """Tracks everything that happens in one pipeline run."""
    user_query: str
    tool_used: Optional[str] = None
    tool_output: Optional[dict] = None
    final_response: Optional[str] = None
    is_valid: bool = False
    error: Optional[str] = None

# Usage
state = QueryState(user_query="What is 25% of 480?")
state.tool_used = "calculator"
state.tool_output = {"result": 120.0}
state.is_valid = True

print(state)
# QueryState(user_query='What is 25% of 480?', tool_used='calculator', ...)
```

**Why it matters for AI:** In Episode 3, `AssistantState` is a dataclass. State tracking is fundamental to any multi-step AI pipeline. Dataclasses give you structure, type hints, and a readable `__repr__` for free.

---

## 🔨 Mini Projects

### Project 1 — Your First LLM API Call (`mini_projects/api_caller/`)
Make a raw API call to OpenAI. No libraries, just `requests`. Understand every part of the request and response.

```bash
python mini_projects/api_caller/llm_api_caller.py "What is a vector embedding?"
```

### Project 2 — Prompt File Runner (`mini_projects/prompt_runner/`)
Load a prompt template from a file, fill in variables, call the LLM, print the response. This is exactly how Episode 3's prompts work.

```bash
python mini_projects/prompt_runner/prompt_runner.py --query "Explain temperature in LLMs"
```

### Project 3 — Response Saver (`mini_projects/response_saver/`)
Call the LLM, validate the response isn't empty, save it to a timestamped JSON file. Your first end-to-end mini system.

```bash
python mini_projects/response_saver/response_saver.py "What is tool calling in AI?"
```

---

## 📝 Exercises

See [`exercises/exercises.md`](exercises/exercises.md) for 10 hands-on challenges. Solutions are in `exercises/solutions/` — but try them yourself first.

Exercises cover:
1. Write a function that calls the OpenAI API and returns the response text
2. Parse a nested API response dict and extract specific fields
3. Load an API key from environment variables with a helpful error if missing
4. Save a list of responses to a JSON file with timestamps
5. Write error handling for a function that might timeout or return bad data
6. Use a list comprehension to clean and filter a list of LLM responses
7. Create a dataclass to model a simple chat message
8. Read a prompt from a `.txt` file and fill in template variables
9. Make an HTTP GET request to the Open-Meteo API and parse the temperature
10. Combine all of the above into a single mini pipeline

---

## ⚡ Quick Start

```bash
git clone https://github.com/YOUR_USERNAME/Python_For_AI_What_Actually_Matters.git
cd Python_For_AI_What_Actually_Matters

python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt

cp .env.example .env
# Add your OPENAI_API_KEY to .env

# Start with the core patterns
python core/01_functions_and_classes.py
python core/02_dicts_and_json.py

# Then try the mini projects
python mini_projects/api_caller/llm_api_caller.py "Hello!"
```

---

## 🗺️ Where This Fits in the Roadmap

| Episode | Topic | Status |
|---|---|---|
| 1 | What is an LLM really? | [View repo →](https://github.com/JoshithReddyAleti/Understanding_LLMs_From_The_Inside_Out) |
| **2** | **Python for AI — what actually matters** | **← You are here** |
| 3 | Tool calling, APIs & validation | [View repo →](https://github.com/JoshithReddyAleti/Building_AI_Project-Blueprint_for_Begin) |
| 4 | Your_First_End_To_End_AI_Project | [View repo →](https://github.com/JoshithReddyAleti/Episode_4_Your_First_End_To_End_AI_Project/tree/main/Your_First_End_To_End_AI_Project/Your_First_End_To_End_AI_Project) |
| 5–10 | Coming soon | [Subscribe →](https://www.linkedin.com/newsletters/ai-engineering-roadmap-2026-7467249724752908288/) |

---

## 📬 Subscribe to the Newsletter

This is Episode 2 of the **AI Engineering Roadmap 2026** — a free LinkedIn newsletter walking you through how to become an AI engineer in 2026.

Every episode: a real project + a concept deep-dive + interview prep.

**[→ Subscribe here. It's free.](https://www.linkedin.com/newsletters/ai-engineering-roadmap-2026-7467249724752908288/)**

---

<div align="center">

**If this helped you, give it a ⭐ — it helps other learners find it.**

[⬅️ Episode 1](https://github.com/JoshithReddyAleti/Understanding_LLMs_From_The_Inside_Out) · [➡️ Episode 3](https://github.com/JoshithReddyAleti/Building_AI_Project-Blueprint_for_Begin)

</div>

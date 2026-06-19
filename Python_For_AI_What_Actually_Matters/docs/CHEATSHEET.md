# ⚡ Python For AI — Quick Reference Cheatsheet

> The 8 patterns at a glance. Bookmark this.

---

## 1. Functions
```python
def call_tool(query: str, timeout: int = 10) -> dict:
    """Always: type hints + docstring + single responsibility."""
    ...
    return {"result": ..., "error": None}
```

## 2. Dicts & JSON
```python
# Safe access — always use .get()
value = data.get("key", default_value)
nested = data.get("choices", [{}])[0].get("message", {}).get("content", "")

# JSON conversion
import json
string = json.dumps(my_dict, indent=2)   # dict → string
data   = json.loads(json_string)          # string → dict
```

## 3. HTTP Requests
```python
import requests
resp = requests.get(url, params={...}, timeout=10)
resp.raise_for_status()   # raises on 4xx/5xx
data = resp.json()

resp = requests.post(url, headers={...}, json={...}, timeout=30)
```

## 4. Environment Variables
```python
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.environ.get("OPENAI_API_KEY")
if not api_key: raise ValueError("Missing OPENAI_API_KEY")
```

## 5. File I/O
```python
# Read
with open("prompts/my_prompt.txt", "r") as f:
    template = f.read()
prompt = template.format(query=user_query)

# Write JSON
import json
with open("outputs/result.json", "w") as f:
    json.dump(data, f, indent=2)
```

## 6. Error Handling
```python
try:
    result = risky_call()
except requests.Timeout:
    return {"error": "timed out", "result": None}
except Exception as e:
    return {"error": str(e), "result": None}
# Never crash — always return something
```

## 7. List Comprehensions
```python
cleaned  = [r.strip() for r in responses if r.strip()]
valid    = [r for r in results if r.get("error") is None]
contents = [m["content"] for m in messages if m["role"] == "user"]
```

## 8. Dataclasses
```python
from dataclasses import dataclass
from typing import Optional

@dataclass
class PipelineState:
    query: str
    tool_used: Optional[str] = None
    response: Optional[str] = None
    is_valid: bool = False
    error: Optional[str] = None
```

---

## The LLM API Call Pattern (memorise this)

```python
import os, requests
from dotenv import load_dotenv

load_dotenv()

def call_llm(prompt: str, temperature: float = 0.7) -> str:
    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers={"Authorization": f"Bearer {os.environ['OPENAI_API_KEY']}"},
        json={
            "model": "gpt-4o-mini",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": temperature,
            "max_tokens": 500,
        },
        timeout=30,
    )
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"].strip()
```

---

*Part of the [AI Engineering Roadmap 2026](https://www.linkedin.com/newsletters/ai-engineering-roadmap-2026-7467249724752908288/)*

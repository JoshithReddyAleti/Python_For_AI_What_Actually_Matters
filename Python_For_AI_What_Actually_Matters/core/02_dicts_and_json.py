"""
core/02_dicts_and_json.py
===========================
AI Engineering Roadmap 2026 · Episode 2

Pattern 2: Dicts and JSON

The universal language of AI systems is JSON.
Every API response, every tool output, every system state — all dicts.
Master this pattern and everything else gets easier.

Run this file:
  python core/02_dicts_and_json.py
"""

import json


# ─────────────────────────────────────────────────────────────
# SAFE ACCESS — Never trust a dict blindly
# ─────────────────────────────────────────────────────────────

def safe_get(data: dict, key: str, default=None):
    """
    The single most important dict habit: use .get() not []

    Why?
      data["missing_key"]        → KeyError (crashes your system)
      data.get("missing_key")    → None (safe, you handle it)
      data.get("missing_key", 0) → 0   (safe, with your default)
    """
    return data.get(key, default)


# ─────────────────────────────────────────────────────────────
# NESTED ACCESS — Real API responses are deeply nested
# ─────────────────────────────────────────────────────────────

SAMPLE_OPENAI_RESPONSE = {
    "id": "chatcmpl-abc123",
    "object": "chat.completion",
    "model": "gpt-4o-mini",
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "25% of 480 is 120."
            },
            "finish_reason": "stop"
        }
    ],
    "usage": {
        "prompt_tokens": 15,
        "completion_tokens": 12,
        "total_tokens": 27
    }
}


def extract_content(response: dict) -> str:
    """
    Extract the text content from an OpenAI response.
    Shows safe nested access with multiple .get() calls.
    """
    choices = response.get("choices", [])
    if not choices:
        return ""
    return choices[0].get("message", {}).get("content", "")


def extract_token_usage(response: dict) -> dict:
    """Extract token counts — useful for cost monitoring."""
    usage = response.get("usage", {})
    return {
        "input": usage.get("prompt_tokens", 0),
        "output": usage.get("completion_tokens", 0),
        "total": usage.get("total_tokens", 0),
    }


# ─────────────────────────────────────────────────────────────
# JSON — Converting between dicts and strings
# ─────────────────────────────────────────────────────────────

def dict_to_json_string(data: dict, pretty: bool = False) -> str:
    """
    Convert a dict to a JSON string.
    Use pretty=True for human-readable output (logs, files).
    Use pretty=False for API calls and storage.
    """
    if pretty:
        return json.dumps(data, indent=2)
    return json.dumps(data)


def json_string_to_dict(json_str: str) -> dict | None:
    """
    Safely parse a JSON string to a dict.
    Returns None on failure — never crashes.

    Real-world note: LLMs often return JSON wrapped in markdown fences
    (```json ... ```) — strip those before parsing.
    """
    # Strip markdown code fences if present
    cleaned = json_str.strip()
    if cleaned.startswith("```"):
        lines = cleaned.split("\n")
        cleaned = "\n".join(lines[1:-1])  # Remove first and last line

    try:
        return json.loads(cleaned)
    except json.JSONDecodeError as e:
        print(f"JSON parse failed: {e}")
        return None


# ─────────────────────────────────────────────────────────────
# BUILDING DICTS — Patterns for creating structured data
# ─────────────────────────────────────────────────────────────

def build_tool_result(tool_name: str, success: bool, data: dict = None, error: str = None) -> dict:
    """
    Standardised dict structure for tool outputs.
    Consistent structure = predictable, validatable.
    """
    return {
        "tool": tool_name,
        "success": success,
        "data": data or {},
        "error": error,
    }


def build_system_response(query: str, tool_used: str | None, response: str, is_valid: bool) -> dict:
    """Build a complete system response dict for logging and storage."""
    from datetime import datetime, timezone
    return {
        "query": query,
        "tool_used": tool_used,
        "response": response,
        "is_valid": is_valid,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


# ─────────────────────────────────────────────────────────────
# DEMO
# ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("\n=== Safe Dict Access ===\n")

    data = {"name": "Claude", "version": 4}
    print(f"data.get('name')         → {data.get('name')}")
    print(f"data.get('missing')      → {data.get('missing')}")
    print(f"data.get('missing', 'X') → {data.get('missing', 'X')}")

    print("\n=== Nested API Response ===\n")
    content = extract_content(SAMPLE_OPENAI_RESPONSE)
    usage = extract_token_usage(SAMPLE_OPENAI_RESPONSE)
    print(f"Content:  {content}")
    print(f"Usage:    {usage}")

    print("\n=== JSON Conversion ===\n")
    result = build_tool_result("calculator", True, {"result": 120.0})
    json_str = dict_to_json_string(result, pretty=True)
    print(f"Dict → JSON:\n{json_str}")

    parsed = json_string_to_dict(json_str)
    print(f"JSON → Dict: {parsed}")

    print("\n=== LLM JSON with Markdown Fences ===\n")
    # LLMs often return JSON like this — you need to handle it
    llm_response_with_fences = """
```json
{"tool": "weather", "location": "London", "temperature": 14}
```
"""
    parsed = json_string_to_dict(llm_response_with_fences)
    print(f"Parsed: {parsed}")

    print("\n✅ Pattern 2 complete. Move to core/03_http_requests.py")

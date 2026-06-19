"""
core/07_list_comprehensions.py + 08_dataclasses.py
=====================================================
Patterns 7 & 8: List Comprehensions and Dataclasses

Run: python core/07_list_comprehensions.py
"""

# ── Pattern 7: List Comprehensions ────────────────────────────

def clean_responses(raw_responses: list[str]) -> list[str]:
    """Clean and filter a list of LLM responses."""
    return [r.strip() for r in raw_responses if r.strip()]


def extract_tool_results(results: list[dict]) -> list[dict]:
    """Keep only successful tool results."""
    return [r for r in results if r.get("error") is None and r.get("result") is not None]


def get_response_lengths(responses: list[str]) -> list[int]:
    """Get character length of each response."""
    return [len(r) for r in responses]


# ── Pattern 8: Dataclasses ────────────────────────────────────

from dataclasses import dataclass, field
from typing import Optional
from datetime import datetime, timezone


@dataclass
class PipelineResult:
    """
    A complete, structured record of one pipeline run.
    This is the Pydantic-free version of ValidatedResponse from Episode 3.
    Dataclasses give you __repr__, __eq__, and type hints for free.
    """
    query: str
    tool_used: Optional[str] = None
    tool_output: Optional[dict] = None
    final_response: Optional[str] = None
    is_valid: bool = False
    error: Optional[str] = None
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

    def to_dict(self) -> dict:
        return {
            "query": self.query,
            "tool_used": self.tool_used,
            "tool_output": self.tool_output,
            "final_response": self.final_response,
            "is_valid": self.is_valid,
            "error": self.error,
            "created_at": self.created_at,
        }


if __name__ == "__main__":
    print("\n=== List Comprehensions Demo ===\n")

    raw = ["  Hello  ", "  World  ", "", "  AI Engineering  ", "  "]
    cleaned = clean_responses(raw)
    print(f"Cleaned responses: {cleaned}")

    results = [
        {"tool": "calculator", "result": 120.0, "error": None},
        {"tool": "weather", "result": None, "error": "City not found"},
        {"tool": "calculator", "result": 350.0, "error": None},
    ]
    valid = extract_tool_results(results)
    print(f"Valid results: {[r['result'] for r in valid]}")

    print("\n=== Dataclasses Demo ===\n")
    result = PipelineResult(
        query="What is 25% of 480?",
        tool_used="calculator",
        tool_output={"result": 120.0},
        final_response="25% of 480 is 120.",
        is_valid=True,
    )
    print(f"Result: {result}")
    print(f"As dict: {result.to_dict()}")

    print("\n✅ All 8 patterns complete! Now try the mini_projects/")

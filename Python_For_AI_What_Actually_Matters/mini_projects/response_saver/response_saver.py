"""
mini_projects/response_saver/response_saver.py
================================================
AI Engineering Roadmap 2026 · Episode 2

Mini Project 3: Response Saver

Call the LLM, validate the response, save to a timestamped JSON file.
Your first complete mini AI pipeline.

Usage:
  python mini_projects/response_saver/response_saver.py "What is tool calling?"
  python mini_projects/response_saver/response_saver.py --list
"""

import os
import sys
import json
import argparse
import requests
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

OUTPUTS_DIR = Path(__file__).parent / "outputs"


def call_llm(query: str) -> str | None:
    """Call LLM and return response text, or None on failure."""
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        pass

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not set.")

    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers={"Authorization": f"Bearer {api_key}"},
        json={
            "model": "gpt-4o-mini",
            "messages": [
                {"role": "system", "content": "You are a concise AI tutor. Answer in 2-3 sentences."},
                {"role": "user", "content": query},
            ],
            "max_tokens": 300,
            "temperature": 0.7,
        },
        timeout=30,
    )
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"].strip()


def validate(response: str | None) -> tuple[bool, str]:
    """
    Validate a response before saving.
    Returns (is_valid, reason).
    """
    if not response:
        return False, "Response is None or empty"
    if len(response.strip()) < 10:
        return False, f"Response too short ({len(response)} chars)"
    if response.strip().lower() in ("none", "null", "undefined"):
        return False, "Response is a null-like string"
    return True, "OK"


def save_response(query: str, response: str, is_valid: bool) -> str:
    """Save the response to a JSON file. Returns the saved path."""
    OUTPUTS_DIR.mkdir(exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    filepath = OUTPUTS_DIR / f"response_{timestamp}.json"

    record = {
        "query": query,
        "response": response,
        "is_valid": is_valid,
        "saved_at": datetime.now(timezone.utc).isoformat(),
    }

    with open(filepath, "w") as f:
        json.dump(record, f, indent=2)

    return str(filepath)


def list_saved_responses() -> None:
    """Print all saved responses."""
    if not OUTPUTS_DIR.exists():
        print("No saved responses yet.")
        return
    files = sorted(OUTPUTS_DIR.glob("response_*.json"))
    print(f"\n{len(files)} saved response(s):\n")
    for file in files:
        with open(file) as f:
            data = json.load(f)
        print(f"  {file.name}")
        print(f"  Query:    {data['query'][:60]}")
        print(f"  Response: {data['response'][:80]}...")
        print(f"  Valid:    {data['is_valid']}\n")


def main():
    parser = argparse.ArgumentParser(description="Call LLM, validate, and save response.")
    parser.add_argument("query", nargs="?", default="What is tool calling in AI?")
    parser.add_argument("--list", action="store_true", help="List all saved responses")
    args = parser.parse_args()

    if args.list:
        list_saved_responses()
        return

    print(f"\nQuery: {args.query!r}")
    print("Calling LLM...")

    try:
        response = call_llm(args.query)
        is_valid, reason = validate(response)

        print(f"\nResponse: {response}")
        print(f"Valid:    {is_valid} ({reason})")

        saved = save_response(args.query, response or "", is_valid)
        print(f"Saved:    {saved}\n")

        print("─" * 50)
        print("✅ Mini Pipeline complete:")
        print("   Call LLM → Validate → Save to JSON")
        print("   This is the foundation of Episode 3's full pipeline.")
        print("─" * 50 + "\n")

    except Exception as e:
        print(f"\n❌ Error: {e}")


if __name__ == "__main__":
    main()

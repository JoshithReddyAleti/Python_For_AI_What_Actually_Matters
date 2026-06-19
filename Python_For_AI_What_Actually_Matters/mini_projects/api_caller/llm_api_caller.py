"""
mini_projects/api_caller/llm_api_caller.py
============================================
AI Engineering Roadmap 2026 · Episode 2

Mini Project 1: Your First LLM API Call

This is the simplest possible LLM call — using requests directly,
no SDK, so you can see every part of the HTTP request and response.

Usage:
  python mini_projects/api_caller/llm_api_caller.py "What is a token?"
  python mini_projects/api_caller/llm_api_caller.py --model gpt-4o "Explain RAG simply"
"""

import sys
import os
import json
import requests
import argparse

# Make sure we can import from the project root
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


def load_api_key() -> str:
    """Load OpenAI API key from environment."""
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        pass

    key = os.environ.get("OPENAI_API_KEY")
    if not key:
        raise ValueError(
            "\n❌ OPENAI_API_KEY not found.\n"
            "   1. Copy .env.example to .env\n"
            "   2. Add your API key\n"
            "   3. Run again\n"
        )
    return key


def call_openai_api(
    prompt: str,
    model: str = "gpt-4o-mini",
    temperature: float = 0.7,
    max_tokens: int = 500,
) -> dict:
    """
    Make a raw HTTP POST to the OpenAI chat completions endpoint.

    This is exactly what openai.chat.completions.create() does under the hood.
    Learning the raw version first helps you debug when things go wrong.

    Args:
        prompt: The user's question or instruction
        model: The OpenAI model to use
        temperature: 0=deterministic, 1=creative
        max_tokens: Maximum response length in tokens

    Returns:
        The full API response dict
    """
    api_key = load_api_key()

    # This is what every LLM API call looks like
    request_body = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful, concise AI tutor for the AI Engineering Roadmap 2026 series. Answer clearly in 2-3 sentences."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": temperature,
        "max_tokens": max_tokens,
    }

    response = requests.post(
        url="https://api.openai.com/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json=request_body,
        timeout=30,
    )

    response.raise_for_status()
    return response.json()


def extract_text(api_response: dict) -> str:
    """Pull the response text out of the API response dict."""
    return api_response.get("choices", [{}])[0].get("message", {}).get("content", "")


def print_full_breakdown(prompt: str, api_response: dict) -> None:
    """Print the request and response in a way that teaches you the structure."""
    text = extract_text(api_response)
    usage = api_response.get("usage", {})

    print("\n" + "=" * 65)
    print("  LLM API CALL BREAKDOWN")
    print("=" * 65)
    print(f"\n  Prompt:     {prompt[:80]}")
    print(f"  Model:      {api_response.get('model')}")
    print(f"\n  Response:   {text[:200]}")
    print(f"\n  Token usage:")
    print(f"    Input:    {usage.get('prompt_tokens', '?')} tokens")
    print(f"    Output:   {usage.get('completion_tokens', '?')} tokens")
    print(f"    Total:    {usage.get('total_tokens', '?')} tokens")
    print(f"\n  Full response structure:")
    print(json.dumps(api_response, indent=2)[:800] + "...")
    print("=" * 65 + "\n")


def main():
    parser = argparse.ArgumentParser(description="Make a raw LLM API call and see the full response.")
    parser.add_argument("prompt", nargs="?", default="What is a large language model?")
    parser.add_argument("--model", default="gpt-4o-mini")
    parser.add_argument("--temperature", type=float, default=0.7)
    parser.add_argument("--max-tokens", type=int, default=200)
    args = parser.parse_args()

    print(f"\nCalling OpenAI API with: {args.prompt!r}")
    try:
        response = call_openai_api(
            prompt=args.prompt,
            model=args.model,
            temperature=args.temperature,
            max_tokens=args.max_tokens,
        )
        print_full_breakdown(args.prompt, response)
    except requests.HTTPError as e:
        print(f"\n❌ API error: {e.response.status_code} — {e.response.text}")
    except Exception as e:
        print(f"\n❌ Error: {e}")


if __name__ == "__main__":
    main()

"""
mini_projects/prompt_runner/prompt_runner.py
=============================================
AI Engineering Roadmap 2026 · Episode 2

Mini Project 2: Prompt File Runner

Load a prompt template from a .txt file, fill in variables,
call the LLM, print the response.

This is exactly how Episode 3's prompts/ folder works.

Usage:
  python mini_projects/prompt_runner/prompt_runner.py --query "Explain temperature"
  python mini_projects/prompt_runner/prompt_runner.py --list-prompts
"""

import os
import sys
import argparse
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


def load_prompt_template(prompt_name: str) -> str:
    """Load a prompt template from the prompts/ directory."""
    prompts_dir = Path(__file__).parent / "prompts"
    filepath = prompts_dir / f"{prompt_name}.txt"

    if not filepath.exists():
        available = [f.stem for f in prompts_dir.glob("*.txt")]
        raise FileNotFoundError(
            f"Prompt '{prompt_name}' not found.\n"
            f"Available prompts: {available}"
        )

    with open(filepath, "r") as f:
        return f.read()


def fill_template(template: str, **variables) -> str:
    """Fill in {variable} placeholders in the template."""
    try:
        return template.format(**variables)
    except KeyError as e:
        raise ValueError(f"Template requires variable {e} but it wasn't provided.")


def call_llm(prompt: str) -> str:
    """Simple LLM call — returns response text."""
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        pass

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not set. See .env.example")

    import requests
    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers={"Authorization": f"Bearer {api_key}"},
        json={
            "model": "gpt-4o-mini",
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 400,
            "temperature": 0.7,
        },
        timeout=30,
    )
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"].strip()


def list_available_prompts() -> list:
    """List all .txt files in the prompts directory."""
    prompts_dir = Path(__file__).parent / "prompts"
    return [f.stem for f in prompts_dir.glob("*.txt")]


def main():
    parser = argparse.ArgumentParser(description="Run a prompt template from file.")
    parser.add_argument("--query", default="What is an LLM?", help="The query to fill into the template")
    parser.add_argument("--prompt", default="sample_prompt", help="Name of the prompt template file (without .txt)")
    parser.add_argument("--list-prompts", action="store_true", help="List available prompt templates")
    args = parser.parse_args()

    if args.list_prompts:
        prompts = list_available_prompts()
        print(f"\nAvailable prompts: {prompts}\n")
        return

    print(f"\nRunning prompt: {args.prompt!r}")
    print(f"Query: {args.query!r}\n")

    try:
        template = load_prompt_template(args.prompt)
        filled_prompt = fill_template(template, query=args.query)

        print("─" * 50)
        print("Filled prompt:")
        print(filled_prompt)
        print("─" * 50)

        print("\nCalling LLM...")
        response = call_llm(filled_prompt)

        print(f"\nResponse:\n{response}\n")

    except FileNotFoundError as e:
        print(f"\n❌ {e}")
    except ValueError as e:
        print(f"\n❌ {e}")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")


if __name__ == "__main__":
    main()

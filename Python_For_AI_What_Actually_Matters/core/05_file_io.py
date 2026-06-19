"""
core/05_file_io.py
===================
Pattern 5: File I/O — Reading Prompts, Saving Outputs

Run: python core/05_file_io.py
"""

import json
import os
from datetime import datetime, timezone
from pathlib import Path


def read_prompt(filepath: str, **kwargs) -> str:
    """Read a prompt template from file and fill in variables."""
    with open(filepath, "r") as f:
        template = f.read()
    return template.format(**kwargs) if kwargs else template


def save_response(response: dict, output_dir: str = "outputs") -> str:
    """Save an LLM response dict to a timestamped JSON file."""
    Path(output_dir).mkdir(exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    filepath = f"{output_dir}/response_{timestamp}.json"
    with open(filepath, "w") as f:
        json.dump(response, f, indent=2)
    return filepath


def load_responses(output_dir: str = "outputs") -> list:
    """Load all saved response files from the outputs directory."""
    path = Path(output_dir)
    if not path.exists():
        return []
    files = sorted(path.glob("response_*.json"))
    responses = []
    for file in files:
        with open(file) as f:
            responses.append(json.load(f))
    return responses


if __name__ == "__main__":
    print("\n=== File I/O Demo ===\n")

    # Save a sample response
    sample = {
        "query": "What is 25% of 480?",
        "response": "25% of 480 is 120.",
        "tool_used": "calculator",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
    saved_path = save_response(sample)
    print(f"✅ Saved to: {saved_path}")

    # Load it back
    loaded = load_responses()
    print(f"✅ Loaded {len(loaded)} response(s) from outputs/")
    print(f"\n✅ Pattern 5 complete. Move to core/06_error_handling.py")

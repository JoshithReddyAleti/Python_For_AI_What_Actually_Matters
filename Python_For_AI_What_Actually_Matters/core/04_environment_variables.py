"""
core/04_environment_variables.py
===================================
Pattern 4: Environment Variables — Managing Secrets

Run: python core/04_environment_variables.py
"""

import os


def load_api_key(key_name: str, required: bool = True) -> str | None:
    """
    Load an API key from environment. Warn clearly if missing.
    Always use this pattern — never hardcode keys.
    """
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        pass  # dotenv optional — env vars might be set by the system

    value = os.environ.get(key_name)

    if not value and required:
        raise ValueError(
            f"\n❌ Missing required environment variable: {key_name}\n"
            f"   1. Copy .env.example to .env\n"
            f"   2. Add your {key_name} value\n"
            f"   3. Run again\n"
        )
    return value


if __name__ == "__main__":
    print("\n=== Environment Variables Demo ===\n")
    print("Trying to load OPENAI_API_KEY...")
    try:
        key = load_api_key("OPENAI_API_KEY", required=True)
        masked = key[:7] + "..." + key[-4:] if key and len(key) > 11 else "too short to mask"
        print(f"✅ Found key: {masked}")
    except ValueError as e:
        print(e)
    print("\n✅ Pattern 4 complete. Move to core/05_file_io.py")

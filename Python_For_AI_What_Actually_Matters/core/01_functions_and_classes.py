"""
core/01_functions_and_classes.py
==================================
AI Engineering Roadmap 2026 · Episode 2

Pattern 1: Functions and Classes

Every AI system is a collection of components.
Functions and classes are how you build components that are:
  - Testable (you can test each piece independently)
  - Reusable (use the same component in multiple places)
  - Replaceable (swap one component for another easily)

Run this file:
  python core/01_functions_and_classes.py
"""


# ─────────────────────────────────────────────────────────────
# FUNCTIONS — Do one thing, return something, type-hint always
# ─────────────────────────────────────────────────────────────

def clean_response(text: str) -> str:
    """
    Remove leading/trailing whitespace from an LLM response.

    Notice:
    - The function name says exactly what it does
    - Type hints tell you what goes in (str) and comes out (str)
    - The docstring explains WHY this exists, not just WHAT it does
    - It does ONE thing only
    """
    return text.strip()


def is_valid_response(response: str, min_length: int = 5) -> bool:
    """
    Check whether a response is worth returning to the user.

    Args:
        response: The text from the LLM
        min_length: Minimum number of characters to be considered valid

    Returns:
        True if the response is usable, False otherwise
    """
    if not response:
        return False
    if len(response.strip()) < min_length:
        return False
    return True


def build_message(role: str, content: str) -> dict:
    """
    Build a chat message dict in the format the OpenAI API expects.

    Args:
        role: 'system', 'user', or 'assistant'
        content: The text content of the message

    Returns:
        A dict like {"role": "user", "content": "Hello"}
    """
    valid_roles = ("system", "user", "assistant")
    if role not in valid_roles:
        raise ValueError(f"Invalid role: {role!r}. Must be one of {valid_roles}")
    return {"role": role, "content": content}


def extract_response_text(api_response: dict) -> str:
    """
    Safely extract the text content from an OpenAI API response dict.

    Notice the nested .get() calls — never assume the key exists.
    """
    choices = api_response.get("choices", [])
    if not choices:
        return ""
    first_choice = choices[0]
    message = first_choice.get("message", {})
    return message.get("content", "")


# ─────────────────────────────────────────────────────────────
# CLASSES — Group related data and behaviour together
# ─────────────────────────────────────────────────────────────

class LLMConfig:
    """
    Configuration for an LLM API call.

    Why use a class instead of loose variables?
    - Groups related settings together
    - Can validate values in __init__
    - Can add methods like to_dict() for serialisation
    - Easy to pass around as a single object
    """

    def __init__(
        self,
        model: str = "gpt-4o-mini",
        temperature: float = 0.7,
        max_tokens: int = 500,
    ):
        # Validate on creation — fail fast with a clear error
        if not 0.0 <= temperature <= 2.0:
            raise ValueError(f"Temperature must be 0-2, got {temperature}")
        if max_tokens < 1:
            raise ValueError(f"max_tokens must be positive, got {max_tokens}")

        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens

    def to_dict(self) -> dict:
        """Serialise config for use in an API call or for logging."""
        return {
            "model": self.model,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
        }

    def __repr__(self) -> str:
        return f"LLMConfig(model={self.model!r}, temp={self.temperature}, max_tokens={self.max_tokens})"


class ConversationHistory:
    """
    Manages a list of messages for a multi-turn conversation.

    This is a simplified version of what real chat systems use.
    In Episode 6, this grows into a full memory system.
    """

    def __init__(self, system_prompt: str = "You are a helpful assistant."):
        self.messages = [
            {"role": "system", "content": system_prompt}
        ]

    def add_user_message(self, content: str) -> None:
        """Add a user message to the conversation."""
        self.messages.append({"role": "user", "content": content})

    def add_assistant_message(self, content: str) -> None:
        """Add an assistant response to the conversation."""
        self.messages.append({"role": "assistant", "content": content})

    def get_messages(self) -> list:
        """Return the full message list (what you send to the API)."""
        return self.messages

    def token_estimate(self) -> int:
        """
        Rough estimate of total tokens in this conversation.
        Rule of thumb: 1 token ≈ 4 characters.
        """
        total_chars = sum(len(m["content"]) for m in self.messages)
        return total_chars // 4

    def clear_history(self, keep_system: bool = True) -> None:
        """Clear conversation history (keep system prompt by default)."""
        if keep_system and self.messages:
            self.messages = [self.messages[0]]
        else:
            self.messages = []

    def __len__(self) -> int:
        """Return number of messages (useful for checks)."""
        return len(self.messages)

    def __repr__(self) -> str:
        return f"ConversationHistory({len(self.messages)} messages, ~{self.token_estimate()} tokens)"


# ─────────────────────────────────────────────────────────────
# DEMO — Run this file to see it all in action
# ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("\n=== Functions Demo ===\n")

    # clean_response
    raw = "  Hello, world!  \n"
    cleaned = clean_response(raw)
    print(f"clean_response({raw!r})")
    print(f"  → {cleaned!r}\n")

    # is_valid_response
    print(f"is_valid_response('Hello') → {is_valid_response('Hello')}")
    print(f"is_valid_response('')      → {is_valid_response('')}")
    print(f"is_valid_response('Hi')    → {is_valid_response('Hi', min_length=5)}\n")

    # build_message
    msg = build_message("user", "What is a vector embedding?")
    print(f"build_message(...) → {msg}\n")

    print("\n=== Classes Demo ===\n")

    # LLMConfig
    config = LLMConfig(model="gpt-4o-mini", temperature=0.0, max_tokens=20)
    print(f"Config: {config}")
    print(f"As dict: {config.to_dict()}\n")

    # ConversationHistory
    history = ConversationHistory("You are a helpful AI tutor.")
    history.add_user_message("What is a token?")
    history.add_assistant_message("A token is a chunk of text — roughly 0.75 words on average.")
    history.add_user_message("Why does it matter?")

    print(f"History: {history}")
    print(f"Messages:")
    for msg in history.get_messages():
        print(f"  [{msg['role']:10}] {msg['content'][:60]}")

    print("\n✅ Pattern 1 complete. Move to core/02_dicts_and_json.py")

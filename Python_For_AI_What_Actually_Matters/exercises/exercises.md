# 📝 Exercises — Python For AI

> 10 hands-on exercises. Try each one before looking at the solutions.
> These are the exact patterns you'll use in Episode 3 and beyond.

---

## Exercise 1 — Write a Function That Calls the LLM

Write a function called `ask_llm(question: str) -> str` that:
- Takes a question as input
- Calls the OpenAI API using `requests`
- Returns the response text as a plain string
- Returns `""` (empty string) on any error — never raises

```python
# Expected usage:
response = ask_llm("What is a context window?")
print(response)  # "A context window is the total..."
```

---

## Exercise 2 — Parse a Nested API Response

Given this dict (a real OpenAI API response structure), extract:
- The response text
- The total tokens used
- The model name

```python
response = {
    "id": "chatcmpl-abc",
    "model": "gpt-4o-mini",
    "choices": [{"message": {"role": "assistant", "content": "Hello!"}, "finish_reason": "stop"}],
    "usage": {"prompt_tokens": 10, "completion_tokens": 5, "total_tokens": 15}
}

# Your code here:
text = ???
tokens = ???
model = ???
```

---

## Exercise 3 — Safe API Key Loading

Write a function `get_api_key(name: str) -> str` that:
- Loads the `.env` file
- Gets the key by name from environment variables
- Raises a `ValueError` with a HELPFUL message if the key is missing
- The error must tell the user exactly what to do to fix it

---

## Exercise 4 — Save and Load JSON

Write two functions:
- `save_to_json(data: dict, filename: str) -> None` — saves a dict to a JSON file
- `load_from_json(filename: str) -> dict` — loads and returns a dict, returns `{}` if file not found

---

## Exercise 5 — Error Handling for API Calls

Rewrite this fragile function to never crash:

```python
# Fragile version — crashes on any error
def get_weather(city: str) -> dict:
    resp = requests.get(f"https://api.example.com/weather?city={city}")
    return resp.json()

# Your task: make it return {"error": "reason", "temperature": None}
# on any failure, instead of crashing
```

---

## Exercise 6 — List Comprehension Practice

Given a list of LLM responses:
```python
responses = [
    "  The answer is 42.  ",
    "",
    "  Tool calling is when an AI uses external functions.  ",
    "   ",
    "RAG stands for Retrieval-Augmented Generation.",
]
```

Using a single list comprehension, produce a list of cleaned, non-empty strings.

---

## Exercise 7 — Create a Dataclass

Create a dataclass called `LLMCall` that tracks:
- `prompt` (str) — the question sent
- `response` (str, default `""`) — the answer received
- `model` (str, default `"gpt-4o-mini"`) — the model used
- `tokens_used` (int, default `0`) — total tokens
- `success` (bool, default `False`) — did it work?

Add a method `to_dict()` that returns all fields as a dictionary.

---

## Exercise 8 — Prompt Template

Create a file `prompts/explain_concept.txt` with a template that:
- Has a `{concept}` placeholder
- Has a `{level}` placeholder (beginner/intermediate/advanced)
- Instructs the LLM to explain the concept at the right level

Then write a function `run_prompt(concept: str, level: str) -> str` that:
1. Reads the template
2. Fills in the placeholders
3. Calls the LLM
4. Returns the response

---

## Exercise 9 — Real API Call (No LLM)

Using `requests`, call the Open-Meteo geocoding API to get the coordinates for "Berlin":
```
https://geocoding-api.open-meteo.com/v1/search?name=Berlin&count=1
```

Extract and print:
- The city name
- Latitude
- Longitude
- Country

Handle the case where the city isn't found.

---

## Exercise 10 — Mini Pipeline

Combine everything:

Write a function `mini_pipeline(query: str) -> dict` that:
1. Validates the query isn't empty
2. Loads the API key from environment
3. Calls the LLM with a prompt template
4. Validates the response (not empty, at least 10 chars)
5. Returns a dict: `{"query", "response", "is_valid", "error"}`
6. On any failure, returns the dict with `is_valid=False` and `error=<reason>`
7. Never raises — always returns a dict

This is a simplified version of the full Episode 3 pipeline.

---

## Solutions

Solutions are in [`solutions/solutions.md`](solutions/solutions.md).

But try each exercise yourself first. The struggle is where the learning happens.

"""
core/06_error_handling.py
===========================
Pattern 6: Error Handling — Systems That Don't Crash

Run: python core/06_error_handling.py
"""


def safe_api_call(query: str) -> dict:
    """
    Always return a dict — success or failure. Never raise to the caller.
    This is the contract every tool function in Episode 3 follows.
    """
    import requests
    try:
        resp = requests.get("https://httpbin.org/get", params={"q": query}, timeout=5)
        resp.raise_for_status()
        return {"success": True, "data": resp.json(), "error": None}
    except requests.Timeout:
        return {"success": False, "data": None, "error": "Request timed out"}
    except requests.HTTPError as e:
        return {"success": False, "data": None, "error": f"HTTP {e.response.status_code}"}
    except Exception as e:
        return {"success": False, "data": None, "error": str(e)}


def call_with_retry(fn, max_retries: int = 3, *args, **kwargs):
    """
    Call a function and retry on failure.
    The same retry pattern used in llm_client.py in Episode 3.
    """
    import time
    for attempt in range(1, max_retries + 1):
        try:
            return fn(*args, **kwargs)
        except Exception as e:
            if attempt == max_retries:
                raise
            print(f"  Attempt {attempt} failed: {e}. Retrying...")
            time.sleep(attempt)


if __name__ == "__main__":
    print("\n=== Error Handling Demo ===\n")
    result = safe_api_call("hello")
    print(f"API call result: success={result['success']}, error={result['error']}")
    print("\n✅ Pattern 6 complete. Move to core/07_list_comprehensions.py")

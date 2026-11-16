"""A tiny greeting package."""


def greet(name: str) -> str:
    """``Hello, <name>!`` 형식의 인사말을 반환한다."""
    return f"Hello, {name.strip() or 'world'}!"

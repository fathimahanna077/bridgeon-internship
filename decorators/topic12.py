from typing import Optional
def greet(name: Optional[str])->str:
    if name is None:
        return "Hello Guest"
    return f"Hello {name}"
print(greet("Hanna"))
print(greet(None))
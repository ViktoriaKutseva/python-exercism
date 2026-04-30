# `@property` - Explained Simply

**Category:** Python / Object-Oriented Programming  
**Difficulty:** Intermediate  
**Created:** 2026-04-29

---

## What Is It? (One-Line Summary)

`@property` lets you access a method like an attribute — no parentheses needed — while keeping full control over reads, writes, and deletes.

## Why It Matters

Without it, you'd choose between:
- **Public attribute** — simple but unprotected (anyone can set `obj.age = -999`)
- **Getter/setter methods** — safe but ugly (`obj.get_age()`, `obj.set_age(25)`)

`@property` gives you both: clean dot-access syntax **and** validation logic behind the scenes.

---

## Breaking It Down

Think of it like a **smart vending machine display**. The screen shows the number of remaining items. You can *look* at it, but you can't just reach in and change the number — there's logic controlling that.

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius   # _ means "private by convention"

    @property
    def radius(self):           # getter — called when you READ obj.radius
        return self._radius

    @radius.setter
    def radius(self, value):    # setter — called when you WRITE obj.radius = x
        if value < 0:
            raise ValueError("Radius can't be negative")
        self._radius = value

c = Circle(5)
print(c.radius)   # 5  ← calls the getter, no ()
c.radius = 10     # ← calls the setter, validates input
c.radius = -1     # ← raises ValueError
```

---

## How It Works

| Decorator | Triggers when… | Purpose |
|---|---|---|
| `@property` | you **read** `obj.attr` | getter — return the value |
| `@attr.setter` | you **write** `obj.attr = x` | validate & store |
| `@attr.deleter` | you **delete** `del obj.attr` | cleanup logic |

The `@property` alone (without a setter) makes the attribute **read-only**.

```python
@property
def lst(self):
    pass   # read-only; assigning obj.lst = x raises AttributeError
```

---

## When To Use It

✅ **Use `@property` when:**
- You need to validate data on assignment
- A value should be computed dynamically (e.g., `area = pi * r²`)
- You want to make an attribute read-only
- You're refactoring a public attribute to add logic without breaking existing code

❌ **Don't use it when:**
- There's no special logic needed — a plain attribute is simpler
- The computation is expensive — callers won't expect `obj.name` to be slow

---

## Common Mistakes

**1. Forgetting `self._attr` vs `self.attr`**  
Inside the setter, writing `self.radius = value` calls the setter again → infinite recursion. Always store to the *private* `self._radius`.

**2. Expecting a setter without defining one**  
```python
@property
def name(self): return self._name
# No @name.setter defined

obj.name = "Alice"  # AttributeError: can't set attribute
```

**3. Thinking `@property` is the same as a regular method**  
It *is* a method under the hood, but called without `()`. This is intentional — it looks like attribute access to the caller.

---

## Try It Yourself

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Below absolute zero!")
        self._celsius = value

    @property
    def fahrenheit(self):           # computed property — no setter needed
        return self._celsius * 9/5 + 32

t = Temperature(100)
print(t.fahrenheit)   # 212.0 — computed on the fly
t.celsius = 0
print(t.fahrenheit)   # 32.0
```

---

## Quick Reference

```python
class MyClass:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):          # GETTER (required)
        return self._value

    @value.setter
    def value(self, v):       # SETTER (optional)
        self._value = v

    @value.deleter
    def value(self):          # DELETER (optional)
        del self._value
```

- Access: `obj.value` → calls getter  
- Assign: `obj.value = x` → calls setter  
- Delete: `del obj.value` → calls deleter  
- Read-only: omit the setter  

## What's Next?

- `__slots__` — restrict attributes for memory efficiency  
- Descriptors (`__get__`, `__set__`) — what `@property` is built on  
- `dataclasses.field` — modern alternative for simple data classes  
- `functools.cached_property` — like `@property` but computed only once  

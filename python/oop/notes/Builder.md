---
tags: [python, oop, patterns, builder]
status: complete
source: src/request_builder.py
---

# Builder

> Builder separates object assembly from the final object so complex construction can stay readable and validated.

## Why Builder exists

Builder helps when a constructor would otherwise become a long unreadable parameter list or when construction must happen in stages.

The key idea is that the product stays simple while the builder carries the assembly workflow.

## Stepwise construction

In the request example, URL, method, headers, payload, and timeout are configured incrementally.

That makes the call site read like a setup flow instead of a positional-argument puzzle.

## Validation boundary

Builder is also a good place to validate partial choices before the final object exists.

Examples from the showcase:

- URL must look like a real HTTP URL
- method must be one of the allowed verbs
- timeout must stay positive

The final `Request` can then stay small and stable.

## Reset behavior

Reusable builders usually reset after `build()`. That prevents accidental leakage of previous state into the next object.

Without reset, the second build often inherits headers or payload from the first and turns into a subtle bug source.

## Source files

- `src/request_builder.py` — fluent builder for a request object with validation and reset semantics

## See also

- [[Factory Method & Abstract Factory]]
- [[Python OOP Basics]]

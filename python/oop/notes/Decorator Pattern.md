---
tags: [python, oop, patterns, decorator]
status: complete
source: src/notifier_decorator.py
---

# Decorator Pattern

> The Decorator pattern adds behavior by wrapping an object that exposes the same interface; it is not the same thing as Python's `@decorator` syntax.

## The pattern, not the syntax

Python function decorators and the Decorator design pattern share the same general intuition: wrap something to extend behavior.

But the object-oriented pattern is specifically about wrapping a component object inside another object with the same interface.

## Why it exists

Decorator solves combinatorial explosion.

Without it, a notification system that can email, text, post to Slack, and audit sends quickly becomes a mess of subclass combinations or feature flags.

With decorators, each concern stays separate and can be stacked at runtime.

## Same interface, extra behavior

Every notifier still answers to `send(message)`. That sameness is what makes wrapping work.

The wrapper delegates to the inner notifier and adds something before or after delegation.

## Why this is different from Proxy

Proxy mainly controls access, lifecycle, or indirection while preserving the same responsibility.

Decorator adds responsibilities to the object itself. In the notifier example, SMS, Slack, and audit are new outward behaviors, not just guarded access to the original email sender.

## Source files

- `src/notifier_decorator.py` — email notifier wrapped with SMS, Slack, and audit decorators

## See also

- [[Adapter & Proxy]]
- [[Strategy, Command & Observer]]

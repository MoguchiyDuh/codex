---
tags: [python, oop, patterns, structural]
status: complete
source: src/payment_gateway.py
---

# Adapter & Proxy

> Adapter changes an interface so two pieces can collaborate; Proxy keeps the same interface but controls access to the real object.

## Adapter

Adapter exists for incompatibility.

The payment example expects `pay(amount: float)`, but the legacy gateway exposes `make_payment(cents: int)`. `LegacyPayAdapter` translates units, method shape, and result language so the client can stay clean.

The important point is that the client no longer knows legacy details.

## Proxy

Proxy exists for control.

`PaymentProxy` exposes the same `pay()` interface as the wrapped processor, but adds authorization and lazy initialization of the expensive secure service.

The client still talks to a `PaymentProcessor`. The extra behavior sits in front of the real work.

## Key distinction

Adapter changes what the object looks like to the client.

Proxy preserves what the object looks like to the client and changes when or whether access is allowed.

## Stacking behavior

The showcase also adds `LoggingProxy` on top of `PaymentProxy`. That shows one useful property of interface-preserving wrappers: they compose naturally.

## Source files

- `src/payment_gateway.py` — adapter for a legacy payment API plus authorization and lazy-init proxies

## See also

- [[Decorator Pattern]]
- [[Factory Method & Abstract Factory]]

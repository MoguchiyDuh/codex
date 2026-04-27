---
tags: [python, oop, classes, composition]
status: complete
source: src/library.py
---

# Python OOP Basics

> Python OOP starts with state and behavior on objects, but good design comes from choosing the right boundaries: what inherits, what composes, and what must be validated.

## Class design

Python classes are lightweight by default. The hard part is not syntax but deciding what invariants the object owns.

In `Book`, the important invariant is that `pages` stays positive. In `Library`, the important invariant is that collection operations stay consistent with the domain model.

## Inheritance vs composition

`EBook` inherits from `Book` because it is still the same conceptual thing with extra state: file size and format.

`Library` uses composition because a library is not a book. It contains books and coordinates operations across them.

That is the first useful OOP filter: use inheritance for an actual `is-a` relationship and composition for a `has-a` relationship.

## Properties and validation

Python properties are a controlled attribute boundary. They let the object keep simple attribute syntax while still enforcing rules.

The important point is not the `@property` syntax itself. The point is that invalid state never enters the object in the first place.

## State transitions

OOP is usually more about valid transitions than about raw data storage.

`checkout()` and `return_back()` are state-transition methods. They encode which moves are legal and reject impossible transitions like double checkout.

This is where methods are better than open mutation: `book.is_checked_out = True` changes data, but `checkout()` enforces business rules.

## Dunder methods that matter

Useful dunder methods make objects easier to work with in normal Python flows.

In `Library`, `__len__`, `__contains__`, `__iter__`, and `__getitem__` make the object act like a real collection. That is better than forcing users through a custom API for every basic operation.

The rule is simple: add dunders when they make the object behave more naturally, not to show off language tricks.

## Source files

- `src/library.py` — `Book`, `EBook`, and `Library` as the baseline OOP showcase

## See also

- [[Abstract Classes vs Protocols]]
- [[Factory Method & Abstract Factory]]

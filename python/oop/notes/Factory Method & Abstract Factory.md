---
tags: [python, oop, patterns, creational]
status: complete
source: src/report_export.py
---

# Factory Method & Abstract Factory

> Factory Method creates one product; Abstract Factory creates a family of products that must stay compatible.

## Factory Method

Factory Method moves object creation behind a boundary so client code does not instantiate concrete classes directly.

In the report export example, `create_renderer()` chooses one renderer from a format string. The client asks for `html`, `md`, or `txt` and gets a `Renderer` back.

That is a one-product decision: choose one implementation of one abstraction.

## Abstract Factory

Abstract Factory matters when one choice implies several related object choices.

An HTML export does not need just an HTML renderer. It also needs an HTML-compatible file name policy and metadata formatter. Those pieces belong together as one family.

The core benefit is consistency. Once the client has an `HtmlExportFactory`, every created product stays in the same family.

## Pattern boundary

If you only need one object, Abstract Factory is too much.

If selecting one mode must create multiple coordinated objects, Factory Method is too little. That is where Abstract Factory earns its complexity.

## Python-specific caution

Python often lets you solve small creation problems with plain functions or dictionaries of constructors. That is fine.

The patterns become worth naming when creation logic starts carrying architectural meaning: consistency, substitution, or product-family boundaries.

## Source files

- `src/report_export.py` — one-off renderer selection plus coordinated export families

## See also

- [[Builder]]
- [[Singleton]]

# OOP — Course Roadmap

Python-first track. Focus: object design, contracts, and the design patterns that still
matter in idiomatic Python.
Primary structured courses: Coursera Packt `Intermediate Python and OOP` and
`Mastering Python Design Patterns`. Reference material: Refactoring.Guru Python catalog,
Python `abc` / `typing` docs, and PEP 544 for `Protocol`.

---

## Phases

### Phase 1 — Core Python OOP

Topics: classes, instances, class vs instance attributes, inheritance, composition,
`super()`, `@property`, dunder methods, dataclasses, when composition beats inheritance.

---

### Phase 2 — Interfaces, Abstract Classes, Protocols

Topics: `abc.ABC`, `@abstractmethod`, nominal vs structural typing,
`typing.Protocol`, PEP 544, runtime enforcement vs static typing, when to use `ABC`
vs `Protocol`, interface design in Python without Java-style overengineering.

---

### Phase 3 — Creational Patterns

Topics: simple factory, Factory Method, Abstract Factory, Builder, Prototype,
Singleton, dependency injection basics, Pythonic alternatives to heavyweight factories,
why Singleton is often overused in Python.

---

### Phase 4 — Structural Patterns

Topics: Adapter, Proxy, Decorator, Facade, Composite, Bridge, Flyweight,
wrapping incompatible interfaces, access control and lazy loading, delegation,
when Python's dynamic features make a classic pattern simpler.

---

### Phase 5 — Behavioral Patterns & Refactoring Practice

Topics: Strategy, Template Method, Observer, Command, State, Chain of Responsibility,
Mediator, Iterator, Visitor, refactoring condition-heavy code into objects,
pattern selection from code smells, when not to use a pattern in Python.

---

## Recommended Resources

- Coursera: `Intermediate Python and OOP` (Packt)
- Coursera: `Mastering Python Design Patterns` (Packt)
- Refactoring.Guru: Python design patterns catalog
- Python docs: `abc` module
- Python docs: `typing` module
- PEP 544: Protocols / structural subtyping
- Optional theory supplement: Coursera `Design Patterns` (University of Alberta, Java-oriented but conceptually strong)
